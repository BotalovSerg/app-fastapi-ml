```
python3 -m venv venv
sourse venv/bin/activate
pip install poetry
poetry install
python3 main.py
```

```shell
# Create directory certs
mkdir certs
cd certs
```

```shell
# Generate an RSA private key, of size 2048
openssl genrsa -out jwt-private.pem 2048
```
```shell
# Extract the public key from the key pair, which can be used in a certificate
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```
```
docker build -t app-fastapi .
docker run --rm -d -p 80:80 app-fastapi
```