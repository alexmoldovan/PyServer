from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class ServerPy (BaseHTTPRequestHandler):
    # def _set_headers (self):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/html')
    #     self.end_headers()

    # def do_HEAD (self):
    #     self._set_headers()
        
    def do_GET (self):
        self._set_headers()
        self.wfile.write("<html><body><h1> GET </h1></body></html>")


    def do_POST (self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        # do something with data
        print post_data

        self._set_headers()
        self.wfile.write("<html><body><h1> POST </h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print 'Starting server'
    
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
