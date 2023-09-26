import tarfile
from Crypto.Cipher import AES
from Sender import assinarDoc
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(2048)
public_key = private_key.public_key()

private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                            encryption_algorithm=serialization.NoEncryption())
public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                         format=serialization.PublicFormat.SubjectPublicKeyInfo)

with open('private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_key_pem)
with open('public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_key_pem)

opcao = input("Digite um tipo de transmissão:\n 1 - Texto + Assinatura\n 2 - Texto Cifrado + Assinatura ")
match opcao:
    case '1':
        signature_pem = assinarDoc('Mensagem.txt')
        file_out = open('signature.pem', 'wb')
        file_out.write(signature_pem)
        file_out.close()
        with tarfile.open ('PastaArq.tar', 'w') as tar:
            tar.add('Mensagem.txt')
            tar.add('signature.pem')
    case '2':
        key = get_random_bytes(32)
        file_out = open('key.data', 'wb')
        file_out.write(key)
        file_out.close()
        signature_pem = assinarDoc('Mensagem.txt')
        file_out = open('signature.pem', 'wb')
        file_out.write(signature_pem)
        file_out.close()
        with open('Mensagem.txt', 'rb') as arq:
            texto = arq.read()
        cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
        textocifrado = cipher.encrypt(texto)
        file_out = open('textocifrado.txt', 'wb')
        file_out.write(textocifrado)
        file_out.close()
        with tarfile.open('PastaArqCifrado.tar', 'w') as tar:
            tar.add('textocifrado.txt')
            tar.add('signature.pem')
