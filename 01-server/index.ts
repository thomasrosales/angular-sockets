import Server from './classes/server';
import router from './routes/router';
import bodyParser from 'body-parser';
import cors from 'cors';

const server = Server.instance;

// BODY PARSER
server.app.use(bodyParser.urlencoded({ extended: true }));
server.app.use(bodyParser.json());

// CORS
server.app.use(cors());

// ROUTES
server.app.use('/', router);

server.start(() => {
  console.log(`Server Running: [PORT: ${server.port}]`);
});
