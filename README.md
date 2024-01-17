# phony-SSL

The Python script will serve an HTTPS server using a randomly generated 'certificate.pem' and 'key.pem' on localhost. This allows for the creation of a fake, yet seemingly legitimate, login page. This script serves as a Proof of Concept (POC), particularly useful for registering evidence by demonstrating the ability to forge a webpage, such as for phishing attacks.

#### Usage

```bash
sudo python3 https-server.py 
```
<br>
The script will bring up a webpage that can be modified according to the specific use case:
<h1 align="center"><img src="https://raw.githubusercontent.com/k4rkarov/phony-SSL/main/poc.png"></h1>
