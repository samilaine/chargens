#!/usr/bin/python

import random, socketserver, string, threading

class Handler(socketserver.BaseRequestHandler):
  printable = (string.punctuation +
               string.ascii_lowercase +
               string.ascii_uppercase +
               string.digits)
  xs = ''.join([chr(y) for y in sorted([ord(x) for x in printable])])

  def handle(self):
    bs = ':'.join([str(x) for x in self.client_address])
    print('{0} connected'.format(bs))

    p = 0
    while True:
      try:
        self.request.recv(1024)

        if p + 72 < len(self.xs):
          slice = self.xs[p:p + 72]
        else:
          slice = self.xs[p:] + self.xs[0:72 - (94 - p)]
                  
        self.request.sendall(bytes(slice, 'utf-8'))
        p = p + 1 if p < len(self.xs) else 0

      except ConnectionError:
        break

    print('{0} disconnected'.format(bs))


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
  pass

if __name__ == '__main__':
  srv = Server(('localhost', 1919), Handler)
  thrd = threading.Thread(target = srv.serve_forever)
  thrd.daemon = True
  thrd.start()
  try:
    while True:
      pass
  except KeyboardInterrupt:
    pass

  srv.shutdown()
  srv.server_close()

# end of file.
