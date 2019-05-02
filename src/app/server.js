//import {PythonShell} from 'python-shell'
let {PythonShell} = require('python-shell');
const path = require('path');
const fs = require('fs');
const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser')
const app = express();
const router = express.Router();

const DIR = '';

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

app.get('/api', function (req, res) {
 
  res.end('file catcher example');
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
              console.log(data.toString());
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
var http = require('http');


http.createServer(function (req, res) {

  res.writeHead(200, { 'Content-Type': 'text/plain', 'Access-Control-Allow-Origin': '*' });
  var data = JSON.stringify({"m":2,"n" :2});
  res.end(data);

}).listen(8080);
console.log("Server running on port 8080.");