import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AuthenticationService } from '../providers/authentication.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticatedGuard implements CanActivate {
	
	constructor(
		private router: Router,
		private authService: AuthenticationService
	) { }

	canActivate() {
		if (this.authService.isLogin())
			return true;

		// not logged in so redirect to login page
		this.router.navigate(['/login']);
		return false;
	} 
}
