import * as $ from 'jquery';
import { Component, OnInit } from '@angular/core';
import { renderFlagCheckIfStmt } from '@angular/compiler/src/render3/view/template';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'ShoppinCart';
  public Products;
constructor()
{}

ngOnInit(){
}


public static get API_ENDPOINT(): string { return 'http://127.0.0.1:8000/api'; }
}





