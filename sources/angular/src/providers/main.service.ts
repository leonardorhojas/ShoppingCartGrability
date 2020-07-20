import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppComponent } from '../app/app.component';
import { AuthenticationService } from './authentication.service';
import { map } from 'rxjs/operators';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MainService {

	constructor(
        public http: HttpClient,
        private authService: AuthenticationService
    ) {
		console.log('Hello MainServiceProvider Provider');
	}

    async get(request: string, data: any){
        let params='';
        for(let key in data){
            params+='&'+encodeURIComponent(String(key))+'='+encodeURIComponent(String(data[key]));
        }
        let access_token = await this.authService.getAuthToken();

        try{
            let result = await this.http.get(
                environment.API_ENDPOINT+request+'?access_token='+access_token+params
            ).pipe(map((res) => res)).toPromise();

            return result;
        }catch (error){
            return this.handleError(error);
        }
    }

    async post(request: string, data: any){
        let access_token = await this.authService.getAuthToken();

         try{
            let result = await this.http.post(environment.API_ENDPOINT+request+'?access_token='+access_token,data)
            .pipe( map((res) => res)).toPromise();

            return result;
        }catch (error){
            return this.handleError(error);
        }
    }

    async put(request: string, id: number, data: any){
        let access_token = await this.authService.getAuthToken();

        try{
            let result = await this.http.put(
                environment.API_ENDPOINT+request+( id ? '/'+id : '')+'?access_token='+access_token,
                data
            ).pipe(map((res) => res)).toPromise();

            return result;
        }catch (error){
            return this.handleError(error);
        }
    }

    async delete(request: string, id: number){
        let access_token = await this.authService.getAuthToken();

        try{
            let result = await this.http.delete(
                environment.API_ENDPOINT+request+'/'+id+'?access_token='+access_token
            ).pipe(map((res) => res)).toPromise();
            return result;
        }catch (error){
            return this.handleError(error);
        }
    }

    private handleError(error){
        if(error.status == 401){
            this.authService.logout('Tu Sesión ha expirado.');
            return null;
        }
        return error._body;
    }

}
