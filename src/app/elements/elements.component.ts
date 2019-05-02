import { Component, OnInit } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-elements',
  templateUrl: './elements.component.html',
  styleUrls: ['./elements.component.scss']
})
export class ElementsComponent implements OnInit {
  members=[];
  loads=[];
  constructor(private http:HttpClient) { }
url:string= "http://localhost:8080";
ps;
 
 public list_ml(n:Number,m:any[]){

  for( let i=0;i<n;i++){
    m[i]=i;
  }
 }

  ngOnInit():void {
    
     this.http.get(this.url).subscribe(response => {
          this.ps=response;
            console.log(this.ps);
           this.list_ml(this.ps.m,this.members);
           console.log(this.members[0]);
        });
  }
}
