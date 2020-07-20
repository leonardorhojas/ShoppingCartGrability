import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { FormBuilder, Validators, AbstractControl } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

import { AuthenticationService } from '../../providers/authentication.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

	public msg_string:String;
	public msg:boolean;
	public userForm: any;

  constructor(private router:Router, private formBuilder:FormBuilder, private toastr: ToastrService, public authService: AuthenticationService) {
  	this.userForm = this.formBuilder.group({
  		username : ['', [Validators.required,Validators.email]],
  		password : ['', Validators.required]
  	});
  }

  ngOnInit(): void {
  }

  login(){
  	if(this.userForm.valid){
  		this.authService.login(this.userForm.controls.username.value, this.userForm.controls.password.value).then((res)=>{
  			if(res){
  				this.router.navigate(['/']);
  			}
  		}).catch((error)=>{
  			this.msg = true;
  			this.msg_string = "The username or password entered is incorrect, try again!"
  		});
  	}
  }

}
