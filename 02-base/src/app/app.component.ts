import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import { WebsocoketService } from './services/websocoket.service';
import { ChatService } from './services/chat.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  constructor(public webSocketService: WebsocoketService) {}

  ngOnInit(): void {}
}
