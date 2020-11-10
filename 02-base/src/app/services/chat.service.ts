import { Injectable } from '@angular/core';
import { WebsocoketService } from './websocoket.service';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  constructor(private webSocketService: WebsocoketService) {}

  sendMessage(message: string): any {
    const payload = {
      from: 'Akos',
      body: message,
    };
    this.webSocketService.emit('message', payload);
  }
}
