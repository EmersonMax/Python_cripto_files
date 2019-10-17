import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
 
def encrypt(key, filename):
    chunk_size = 64*1024
    output_file = filename+".enc"
    file_size = (os.path.getsize(filename))
    IV =get_random_bytes(16)

   
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(filename, 'rb') as inputfile:
        with open(output_file, 'wb') as outf:
            
            outf.write(IV)
            while True:
                chunk = inputfile.read(chunk_size)
                cr=16 - len(chunk)%16
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    
                    length = 16 - (len(chunk) % 16)
                    chunk = str(chunk)+str(length)*length
                    chunk=str(chunk)
                outf.write(encryptor.encrypt(chunk))
 
def decrypt(key, filename):
        chunk_size = 64*1024
        output_file = filename[:-4]
        with open(filename, 'rb') as inf:
            
            IV = inf.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            with open(output_file, 'wb') as outf:
                while True:
                    chunk = inf.read(chunk_size)
                    if len(chunk)==0:
                        break
                    outf.write(decryptor.decrypt(chunk))
                
 
def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
 
def main():
    choice = input("Select One of the following\n> 1. Criptografar \n> 2. Descriptografar\n>>> ")
    if choice == "1":
        filename = input("Digite o Nome do arquivo para Criptografar >> ")
        password = input("Enter the password >>")
        password = str.encode(password)
        print (password)
        encrypt(getKey(password), filename)
        print ("Criptografando")
        print ("Pronto!\n%s ==> %s"%(filename, filename+".enc"))
    elif choice == "2":
        filename = input("Arquivo a ser Descriptografado > ")
        password = input("Password: ")
        password = str.encode(password)
        decrypt(getKey(password), filename)
        print ("Descriptografando")
        print ("Pronto\n%s ==> %s"%(filename, filename[:-4]))
    else:
        print ("Nenhuma opcao selecionada")
 
if __name__ == "__main__":
    main()