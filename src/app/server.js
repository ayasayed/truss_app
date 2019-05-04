let {PythonShell} = require('python-shell');
const path = require('path');
const fs = require('fs');
const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser')
const app = express();
const router = express.Router();

const DIR = '';
let  com ='';



let name_photo="";
let storage = multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, DIR);
    },
    filename: (req, file, cb) => {
      cb(null, name_photo= file.fieldname + '-' + Date.now() +path.extname(file.originalname));

    }
});
let upload = multer({storage: storage});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use(function (req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4200');
  res.setHeader('Access-Control-Allow-Methods', 'POST');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  next();
});



app.post('/api/upload',upload.single('image'), function (req, res) {
    if (!req.file) {
        console.log("No file received");
        return res.send({
          success: false
        });

      } else {
        console.log('file received'+ ":" + name_photo);

            /////python part

            let {PythonShell} = require('python-shell');

            const spawn = require("child_process").spawn;
            const pythonProcess = spawn('python',["src/app/pre_process.py", name_photo]);

            pythonProcess.stdout.on('data', (data) => {
              // Do something with the data returned from python script DA FADY :D
              com=data.toString();
              app.get('/api/upload', function (req, res){
                res.write(JSON.stringify({"m":com.slice(1,com.indexOf(",")),"n":com.slice(com.indexOf(",")+2,com.indexOf("]"))}));
                res.end();
              });
              console.log(com);


            });

/////////////////////////////////////////////////////////////////////////
return res.send({
          success: true
          });

      }
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, function () {
  console.log('Node.js server is running on port ' + PORT);
});

/////

