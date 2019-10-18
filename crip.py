import os, time
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from optparse import *



print("""
\t
\t             Feito por Emerson Max 
\t               
\t          
\t                                                  
          
""")
 
def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename+".emerson"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename.split('.emerson')[0]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
 
def getkey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()
 
def main():
    choice = input("Select One of the following\n> 1. Criptografar \n> 2. Descriptografar\n>>> ")
    if choice == "1":
        filename = input("Digite o Nome do arquivo para Criptografar >> ")
        password = input("Enter the password >>")
        
        print (password)
        encrypt(getkey(password), filename)
        print ("Criptografando")
        print("[+] removing file......")
        time.sleep(1.5)
        os.remove(filename)
        print ("Pronto!\n%s ==> %s"%(filename, filename+".emerson"))
    elif choice == "2":
        filename = input("Arquivo a ser Descriptografado > ")
        password = input("Password: ")
        
        decrypt(getkey(password), filename)
        print ("Descriptografando")
        print("[+] removing file......")
        os.remove(filename)
        time.sleep(1.5)
        print ("Pronto\n%s ==> %s"%(filename, filename[:-8]))
    else:
        print ("Nenhuma opcao selecionada")
 
if __name__ == "__main__":
    main()