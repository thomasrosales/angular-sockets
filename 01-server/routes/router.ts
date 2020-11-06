import { Router, Request, Response } from 'express';

const router = Router();

/**
 * API REST
 */

router.get('/messages', (request: Request, response: Response) => {
  response.json({
    ok: true,
    message: 'Everything good.',
  });
});

router.post('/messages', (request: Request, response: Response) => {
  response.json({
    ok: true,
    message: '[POST] Everything good.',
  });
});

export default router;
