from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec
import subprocess
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import hashlib

def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# def load_ec_key_pair():
#     with open("private_key.pem", "rb") as private_key_file, open("public_key.pem", "rb") as public_key_file:
#         private_key = serialization.load_pem_private_key(
#             private_key_file.read(),
#             password=None
#         )
#         public_key = serialization.load_pem_public_key(
#             public_key_file.read()
#         )
#     return private_key, public_key

# # ##GERANDO POR SSH_KEYGEN
# #Chaves geradas pelo SSH ja vem em par
# # RSA
# comando_SSH = ["ssh-keygen", "-t", "rsa", "-b", "2048", "-f", "chave_RSA_gerada_por_SSH_Keygen", "-q", "-N", " "]
# #Chama o terminal e passa o tipo RSA, quantidade de bits 2048, o nome do arquivo e o Passphrase como null.
# subprocess.run(comando_SSH)
# # EC
# comando_SSH = ["ssh-keygen", "-t", "ecdsa", "-b", "256", "-f", "chave_EC_gerada_por_SSH_Keygen", "-q", "-N", " "]
# #Chama o terminal e passa o tipo EC, quantidade de bits 256 [ele aceita apenas 256,384 e 521], o nome do arquivo  e o Passphrase como null.
# subprocess.run(comando_SSH)
#
# ##GERANDO POR OPENSSL
# #OpenSSL precisa ser invocada 2 vezes para criar a chave publica.
# # RSA
# comando_OPENSSL = ["openssl", "genrsa", "-out", "chave_privada_rsa_OPENSSL.pem", "2048"]
# #Chama o terminal e passa o tipo RSA, nome de saida do arquivo e a quantidade de bits.
# subprocess.run(comando_OPENSSL)
# comando_OPENSSL_publica = ["openssl", "rsa", "-in", "chave_privada_rsa_OPENSSL.pem", "-outform", "PEM", "-pubout", "-out", "chave_publica_rsa_OPENSSL.pem"]
# #Chama o terminal para extrair a chave publica da chave privada.
# subprocess.run(comando_OPENSSL_publica)
# # EC
# comando_OPENSSL = ["openssl", "ecparam", "-name", "secp256k1", "-genkey", "-noout", "-out", "chave_privada_EC_OPENSSL.pem"] #Gera a chave privada via OPENSSL
# #Chama o terminal e passa o tipo EC, o modo SECP256K1 (256bits) e nome de saida do arquivo.
# subprocess.run(comando_OPENSSL)
# comando_OPENSSL_publica = ["openssl", "ec", "-in", "chave_privada_EC_OPENSSL.pem", "-pubout", "-out", "chave_publica_EC_OPENSSL.pem"]#Gera a chave publica via OPENSSL
# #Chama o terminal para extrair a chave publica da chave privada.
# subprocess.run(comando_OPENSSL_publica)

##GERADO POR CODIGO
#RSA
chave_RSA = rsa.generate_private_key(public_exponent=65537, key_size=1024)
#Cria uma chave passando o expoente e o tamanho da chave
c_privada_RSA = chave_RSA.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
c_publica_RSA = chave_RSA.public_key().public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)
#Cria as chaves publicas e privadas passando o tipo de codificação e padrao (PKCS8)

with open("private_rsa_key.pem", "wb") as private_file:
    private_file.write(c_privada_RSA)
with open("public_rsa_key.pem", "wb") as private_file:
    private_file.write(c_publica_RSA)
#salva as chaves criadas
#
# #EC
# chave_EC = ec.generate_private_key(ec.SECP256R1())
# #gera a chave EC escolhendo a curva, nesse caso a SECP256R1
# Privada_PEM_EC = chave_EC.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
# Publica_SSH_EC = chave_EC.public_key().public_bytes(encoding=serialization.Encoding.OpenSSH, format=serialization.PublicFormat.OpenSSH)
# #Cria as chaves publicas e privadas passando o tipo de codificação e padrao (PKCS8)
#
# with open("privada_ec_key.pem", "wb") as private_file:
#     private_file.write(Privada_PEM_EC)
# with open("publica_ec_key.pub", "wb") as public_file:
#     public_file.write(Publica_SSH_EC)
# #salva as chaves criadas

#### utilizando as chaves
##Cifrando
with open('mensagem.txt', 'rb') as arquivo_mensagem:
    mensagem = arquivo_mensagem.read()


sha256 = hashlib.sha256()
sha256.update(mensagem)
arq_hash = sha256.digest()

with open('mensagem.txt', 'rb') as arquivo_mensagem:
    mensagem = arquivo_mensagem.read()
with open("public_rsa_key.pem", "rb") as arquivo_chave_publica_RSA:
    public_key_RSA = serialization.load_ssh_public_key(
        arquivo_chave_publica_RSA .read(), backend=None)
print(public_key_RSA)
texto_cryto = public_key_RSA.encrypt(arq_hash, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                     algorithm=hashes.SHA256(),
                                     label=None)
                                     )
print(texto_cryto.hex())
##Decifrando
#with open("private_rsa_key.pem", "rb") as arquivo_chave_privada_RSA:
 #   private_key_RSA = serialization.load_pem_private_key(
  
  #      arquivo_chave_privada_RSA.read(), password=None)
#texto_decryto = decrypt_message(private_key_RSA, texto_cryto)
#print(texto_decryto)
