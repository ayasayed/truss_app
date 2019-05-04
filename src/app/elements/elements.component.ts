import { Component, OnInit } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import{ImageService}from "../image.service"


@Component({
  selector: 'app-elements',
  templateUrl: './elements.component.html',
  styleUrls: ['./elements.component.scss']
})
export class ElementsComponent implements OnInit {
  members=[];
  loads=[];
  obs =new Observable;
  constructor(private http:HttpClient,private ImageService: ImageService) { }

ms:any;
ns:any;
nodeLocation:any=[];
loadvalue:any=[];
 public list_ml(n:Number,m:any[]){
  m.length=0;
  for( let i=0;i<n;i++){
    m[i]=i;
  }
 }

 onEntern(value: string,i) {
   this.nodeLocation[i] = value;
   console.log(this.nodeLocation[0]);
}
onEnterl(value: string,i) {
  this.loadvalue[i] = value;

}
onsubmit(){
if(this.nodeLocation.length== this.members.length&&this.loadvalue.length== this.loads.length){
  console.log("submitted");

}else{alert("please input all missing fields");}

}


    ngOnInit() {
      this.ImageService.getListener().subscribe(loggedIn => {
      if(loggedIn==true){this.ms=this.ImageService.test.m;

          this.list_ml(this.ms,this.members);
          this.ns=this.ImageService.test.n;

          this.list_ml(this.ns,this.loads);
         }
      });
     }
}
