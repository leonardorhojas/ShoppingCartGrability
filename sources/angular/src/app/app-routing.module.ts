import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

/* Components */
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { ProductComponent } from './product/product.component';
import { ShoppingCartComponent } from './shopping-cart/shopping-cart.component';

/* Guards */
import { UnauthenticatedGuard } from '../guards/unauthenticated.guard';
import { AuthenticatedGuard } from '../guards/authenticated.guard';

const routes: Routes = [
	{
		path: '',
		//canActivate: [ AuthenticatedGuard ],
		component: HomeComponent
	},
	{
		path: 'login',
		//canActivate: [ UnauthenticatedGuard ],
		component: LoginComponent
	},
  {
		path: 'shopping-cart',
		//canActivate: [ AuthenticatedGuard ],
		component: ShoppingCartComponent
	},
	{
		path: 'product/:id',
		//canActivate: [ AuthenticatedGuard ],
		component: ProductComponent
	}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
