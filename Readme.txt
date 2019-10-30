Comandos necessario para python criptografia.
instalar o python e colocar o mesmo no path no windows

Atualizar a versão do PIP:
python -m pip install --upgrade pip

instalar o Modulo pycripto:
pip install pycryptodome

para instalar o modulo necessario para criar o arquivo executavel no windows
pip install cx_freeze
criar o arquivo setup.py de acordo com o que está no Git, dentro do diretorio onde esta o arquivo crip.py
e criar o executavel executando a seguinte linha:
setup.py build

caso apresente erro de module crypto :

pip uninstall crypto
Delete "crypto" Folder [C:\Users\AppData\Local\Programs\Python\Python37\Lib\site-packages]
pip install crypto
pip uninstall pycryptodome
pip install pycryptodome

Rename Folder "crypto" to "Crypto" [C:\Users\AppData\Local\Programs\Python\Python37\Lib\site-packages]

Then You Use "from Crypto.Cipher import AES" in Code
