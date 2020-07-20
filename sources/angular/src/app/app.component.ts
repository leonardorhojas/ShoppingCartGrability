import * as $ from 'jquery';
import { Component, OnInit } from '@angular/core';
import {ProductsService}  from  '../providers/products.service';
import { renderFlagCheckIfStmt } from '@angular/compiler/src/render3/view/template';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'ShoppinCart';
  public Products;
constructor(
  private productsService: ProductsService
)
{}

ngOnInit(){
this.fetchProducts();
}

async fetchProducts(){

  this.Products = await this.productsService.getAllProducts();
  console.log(this.Products);
 /*  this.productsService.getAllProducts()
  .subscribe(products => {
    console.log(products);
  }) */
  
  }
}





