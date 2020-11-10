import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Injectable({
  providedIn: 'root',
})
export class WebsocoketService {
  socketStatus = false;

  constructor(private socket: Socket) {
    this.healthCheck();
  }

  healthCheck(): void {
    this.socket.on('connect', () => {
      console.log('Connected to the server.');
      this.socketStatus = true;
    });
    this.socket.on('disconnect', () => {
      console.log('Desconectado del servidor');
      this.socketStatus = false;
    });
  }

  // tslint:disable-next-line: ban-types
  emit(event: string, payload?: any, callback?: Function): void {
    // EMIT EVENT TO SERVER
    this.socket.emit(event, payload, callback);
  }
}
