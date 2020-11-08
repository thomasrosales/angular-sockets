import Server from './classes/server';
import router from './routes/router';
import bodyParser from 'body-parser';
import cors from 'cors';

const server = Server.instance;

// BODY PARSER
server.app.use(bodyParser.urlencoded({ extended: true }));
server.app.use(bodyParser.json());

// CORS
// var whitelist = ['http://localhost:5010', 'http://127.0.0.1:4200'];
// var corsOptions = {
//   origin: function (origin: any, callback: any) {
//     if (whitelist.indexOf(origin) !== -1) {
//       callback(null, true);
//     } else {
//       callback(new Error('Not allowed by CORS'));
//     }
//   },
//   credentials: true,
// };

server.app.use(cors());

// ROUTES
server.app.use('/', router);

server.start(() => {
  console.log(`Server Running: [PORT: ${server.port}]`);
});
