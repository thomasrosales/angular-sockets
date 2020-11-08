import express from 'express';
import { SERVER_PORT } from '../global/environment';
import socketIO from 'socket.io';
import http from 'http';

let webSocketIO = require('socket.io');

export default class Server {
  private static _instance: Server;

  public app: express.Application;
  public port: number;
  public io: socketIO.Server;
  private httpServer: http.Server;

  private constructor() {
    this.app = express();
    this.port = SERVER_PORT;
    this.httpServer = new http.Server(this.app);
    this.io = webSocketIO(this.httpServer);

    this.listenToSockets();
  }

  private listenToSockets() {
    console.log('Listen Conexion - Scokets');
    this.io.on('connection', (socket) => {
      console.log('New Client Listening');

      this.io.on('disconnect', function () {
        console.log('user disconnected');
      });
    });
  }

  public static get instance() {
    return this._instance || (this._instance = new this());
  }

  start(callback: (...args: any[]) => void) {
    this.httpServer.listen(this.port, callback);
  }
}
