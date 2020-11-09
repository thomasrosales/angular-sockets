import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { environment } from '../environments/environment';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

// SOCKET IO
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { FooterComponent } from './components/footer/footer.component';

const config: SocketIoConfig = { url: 'http://localhost:5000', options: {} };

@NgModule({
  declarations: [AppComponent, FooterComponent],
  imports: [BrowserModule, SocketIoModule.forRoot(config), HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
