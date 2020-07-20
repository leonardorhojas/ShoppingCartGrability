import { Injectable } from '@angular/core';
import { MainService } from './main.service'


@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  constructor(
    private mainService: MainService
  ) { }

  async getAllProducts(params){
    return this.mainService.get('/products', params);
  }

  async getProduct(id: string, params ){
    return this.mainService.get(`/products/${id}`, params);
  }


}


