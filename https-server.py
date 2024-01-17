from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ('0.0.0.0', 443)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='certificate_name.pem', keyfile='key_name.pem')

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"HTTPS server running at https://{server_address[0]}:{server_address[1]}/")
httpd.serve_forever()

