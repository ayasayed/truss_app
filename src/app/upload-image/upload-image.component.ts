import { Component, OnInit } from '@angular/core';
import{ImageService}from "../image.service"
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';//node
class ImageSnippet {
  pending: boolean = false;
  status: string = 'init';
  constructor(public src: string, public file: File) {}
}
const URL = 'http://localhost:3000/api/upload';

@Component({
  selector: 'app-upload-image',
  templateUrl: './upload-image.component.html',
  styleUrls: ['./upload-image.component.scss']
})
 export class UploadImageComponent  {


//   public uploader: FileUploader = new FileUploader({url: URL, itemAlias: 'photo'});

    selectedFile: ImageSnippet;

    constructor(private imageService: ImageService){}

    private onSuccess() {
      this.selectedFile.pending = false;
      this.selectedFile.status = 'ok';
    }

    private onError() {
      this.selectedFile.pending = false;
      this.selectedFile.status = 'fail';
      this.selectedFile.src = '';
    }

    processFile(imageInput: any) {
      const file: File = imageInput.files[0];
      const reader = new FileReader();

      reader.addEventListener('load', (event: any) => {

        this.selectedFile = new ImageSnippet(event.target.result, file);

        this.selectedFile.pending = true;
        this.imageService.uploadImage(this.selectedFile.file).subscribe(
          (res) => {
            this.onSuccess();
          },
          (err) => {
            this.onError();
          })
      });

      reader.readAsDataURL(file);
    }
  }
//   ngOnInit() {

//     this.uploader.onAfterAddingFile = (file) => { file.withCredentials = false; };
//     this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {

//          console.log('ImageUpload:uploaded:', item, status, response);
//           alert('File uploaded successfully');


//      };


//  }

// }




