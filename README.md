# phony-SSL

The Python script will serve an HTTPS server using a randomly generated `certificatename.pem` and `privatekeyname.pem` on localhost. This allows for the creation of a fake, yet seemingly legitimate, login page. This script serves as a Proof of Concept (POC), particularly useful for registering evidence by demonstrating the ability to forge an HTTPS webpage, such as for phishing attacks.

#### Usage

```bash
sudo python3 https-server.py 
```
<br>
The script will bring up a webpage that can be modified according to the specific use case:
<br>
<br>
<p align="center"><img src="https://raw.githubusercontent.com/k4rkarov/phony-SSL/refs/heads/main/poc.png"></p>

<br>

> [!NOTE]  
> You can use these files on your web server to set up a secure connection using HTTPS. Keep in mind that, as this is a self-signed certificate, browsers will display a security warning when accessing your site since it was not issued by a trusted certificate authority. It is suitable for use only in a development, testing or POC environment. For a production environment, it is recommended to obtain a certificate from a trusted certificate authority.

<br>

# 1. Creating your own .key and .crt files

You can generate a self-signed SSL certificate using the `openssl` tool, which is available in most Linux distributions and also on Windows. Here are the steps to generate a self-signed SSL certificate:

1. Open a terminal or command prompt.

2. Navigate to the directory where you want to store the self-signed SSL certificate.

3. Run the following `openssl` command to generate a private key (replace `privatekeyname.key` with the desired name for the private key file):

   ```shell
   openssl genpkey -algorithm RSA -out privatekeyname.key
   ```

4. Now, you can generate the self-signed certificate using the private key you created in the previous step. Replace `certificatename.crt` with the desired name for the certificate file:

   ```shell
   openssl req -new -key privatekeyname.key -x509 -days 365 -out certificatename.crt
   ```

   This command will prompt for some information, such as country, state, city, organization, etc. You can fill them in or leave them blank since this is a self-signed certificate, and the information is not verified by a certificate authority.

5. Now you have a `privatekeyname.key` file containing the private key and a `certificatename.crt` file containing the self-signed certificate.

<br>

# 2. Converting the .key and .crt files to .pem

To convert the private key (.key) and the self-signed certificate (.crt) into separate .pem files, you can do so using OpenSSL:

#### Converting the private key (.key) to .pem:

```shell
openssl rsa -in privatekeyname.key -out privatekeyname.pem
```

#### Converting the self-signed certificate (.crt) to .pem:

```shell
openssl x509 -in certificatename.crt -out certificatename.pem
```

<br>
<br>

# 3. Modifying the https-server.py file

If you have renamed the .pem files, ensure to update their names accordingly on line 7 within the `https-server.py` file:

```python
context.load_cert_chain(certfile='certificatename.pem', keyfile='privatekeyname.pem')
```
