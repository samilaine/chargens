#!/usr/bin/python

import os, random, socketserver, string, threading

class Handler(socketserver.BaseRequestHandler):
  def handle(self):
    bs = ':'.join([str(x) for x in self.client_address])
    print('{0} connected'.format(bs))
    while True:
      try:
        self.request.recv(1024)
        chrs = random.choices(string.ascii_lowercase +
                              string.ascii_uppercase +
                              string.digits, k = random.randint(0, 512))
        self.request.sendall(bytes(''.join(chrs), 'utf-8'))
      except:
        print('{0} disconnected'.format(bs))
        break


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
  pass

if __name__ == '__main__':
  srv = Server(('localhost', os.environ.get('PORT', 1919)), Handler)
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
