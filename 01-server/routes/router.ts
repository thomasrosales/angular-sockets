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
  const body = request.body.cuerpo;
  const from = request.body.from;

  response.json({
    ok: true,
    body,
    from,
  });
});

router.post('/messages/:id', (request: Request, response: Response) => {
  const body = request.body.cuerpo;
  const from = request.body.from;
  const id = request.params.id;

  response.json({
    ok: true,
    body,
    from,
    id,
  });
});

export default router;
