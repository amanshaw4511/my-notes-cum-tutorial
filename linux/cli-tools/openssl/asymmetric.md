
# generate keys
## generate keypair
openssl genrsa -out private.pem

## generate keypair with keysize of 4096
openssl genrsa -out private.pem 4096

## generate keypair with protected password
openssl genrsa -aes-256-cbc -out private.pem

## extract public key from private key
openss rsa -in private.pem -pubout -out public.pem


# encrypt - decrypt
## encrypt
openssl pkeyutl --encrypt -inkey private.pem -pubin -in message.txt -out message.txt.enc

## decrypt
openssl pkeyutl --decrypt -inkey private.pem in message.txt.enc -out message.txt


# sign - verify
## sign
openssl pkeyutl -sign -inkey private.pem in message.txt -out message.txt.sig

## verify
openssl pkeyutl -verify -inkey public.pem -pubin -sigfile message.txt.sig -in message.txt
