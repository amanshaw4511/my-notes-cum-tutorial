## list available command , ciphers, digest
openssl -help



## symmetric encryption
    openssl enc -e <cipher> -in <unencrypted_file> <<options>> 
### options
+ input options 
    + by defalut stdin
    + -in <file_to_encrypt>

+ output options
    + by default stdout
    + -out <decrypted_text_file>

+ password options
    + by defalut prompt for password (stdin)
    + -pass pass:<password>
    + -k <key_file>

    openssl enc -e <cipher> -in <unencrypted_file> -out <encrypted_file>

+ provide password from stdin
    openssl enc -e <cipher> -in <unencrypted_file> -out <encrypted_file>
    openssl enc -e -aes-256-cbc -in plain.txt -out encrypted.bin

+ provide password form a file
    openssl enc -e <cipher> -in <unencrypted_file> -out <encrypted_file> -k <key_file>
    
## symmetric decryption

+ unencrypted and save to file
    openssl enc -d <cipher> -in <encrypted_file> -pass pass:<password> -out <unencrypted_file>

+ prompt for password, shows unencrypted_text on stdout
    openssl enc -d <cipher> -in <encrypted_file> 

+ shows unencrypted_text on stdout
openssl enc -d <cipher> -in <encrypted_file> -pass pass:<password>

+ provide password form a file
    openssl enc -d <cipher> -in <encrypted_file> -k <key_file> 


