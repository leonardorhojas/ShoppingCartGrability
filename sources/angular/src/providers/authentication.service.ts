import { Inject, Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { AppComponent } from '../app/app.component';
import { map } from 'rxjs/operators';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
	constructor(
        private http: HttpClient
    ) {
        console.log('Hello AuthServiceProvider Provider');
    }

    async login(user: string, password: string) {
        console.log("intento iniciar sesion");
        let request = await this.http.post<any>('http://localhost:8000/api-auth/login/',
            {
                "username":user.toLowerCase().trim(),
                "password":password
            }
        )
        .pipe(map((res) => res)).toPromise();

        if (!request.error) {
            console.log(request)
            localStorage.setItem('auth_token', request.id);
            localStorage.setItem('id-user', request.userId);
        }

        return request;
    }

    isLogin(){
        let id_user = localStorage.getItem('id-user');
        return id_user ? true : false;
    }

    getAuthToken(){
        return localStorage.getItem('auth_token')
    }

    getIdUser(){
        return localStorage.getItem('id-user');
    }

    getUser(){
        return JSON.parse(localStorage.getItem('user'));
    }

    setUser(user){
        let name_array = user.full_name.split(" ");
        user['display_name'] = name_array.length > 1 ? name_array[0] : user.full_name;
        localStorage.setItem('user', JSON.stringify(user));
    }

    logout(msg=undefined){
        localStorage.clear();
    }
}
