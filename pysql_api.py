import os
import _mssql
import json , requests 
import time
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from optparse import *

conn = _mssql.connect(server='suporte', user='sa', password='MISTERCHEFNET', 
    database='MISTERCHEFNET') #conexão banco sql 
conn.execute_query('SELECT CNPJ FROM LOJAS') #seleciona o cnpj no banco de dados 
for row in conn:
    cnpj=row[0] #salva o cnpj em uma variavel 
    print(cnpj)
cnpj=cnpj.replace('.','')
cnpj=cnpj.replace('/','')
cnpj=cnpj.replace('-','')
print(cnpj)
response = requests.get("http://licencas.anibaltec.com.br/restapi/?db=restapi&table=tbl_LicSoft&column=cnpj&value=%s"%cnpj)#conecta a api
comments = json.loads(response.content)#salva o json em uma lista
sitfin=comments[0]['stfin'] #pega da lista apenas a informação financeira
print(sitfin)  

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename+".anb"
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
    outputFile = filename.split('.anb')[0]

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
    
    if sitfin == "Inadimplente 2":
        filename = input("Digite o Nome do arquivo para Criptografar >> ")
        password = input("Enter the password >>")
        
        print (password)
        encrypt(getkey(password), filename)
        print ("Criptografando")
        print("[+] removing file......")
        time.sleep(1.5)
        os.remove(filename)
        print ("Pronto!\n%s ==> %s"%(filename, filename+".anb"))
    if sitfin == "Adimplente":
        filename = input("Arquivo a ser Descriptografado > ")
        password = input("Password: ")
        
        decrypt(getkey(password), filename)
        print ("Descriptografando")
        print("[+] removing file......")
        os.remove(filename)
        time.sleep(1.5)
        print ("Pronto\n%s ==> %s"%(filename, filename[:-8]))
 
 
if __name__ == "__main__":
    main()
