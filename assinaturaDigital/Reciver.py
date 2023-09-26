import tarfile
from Crypto.Cipher import AES
from Crypto.Util import Counter
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

with open('public_key.pem', 'rb') as public_key_file:
    public_key_pem = public_key_file.read()
public_key = serialization.load_pem_public_key(public_key_pem)

opcao = input("Digite um tipo de recebimento:\n 1 - Texto + Assinatura\n 2 - Texto Cifrado + Assinatura ")
match opcao:
    case '1':
        with tarfile.open('PastaArq.tar', 'r') as arquvo_tar:
            arquvo_tar.extractall('NovaPastaArq')
        with open('NovaPastaArq/signature.pem', 'rb') as signature_file:
            signature_pem = signature_file.read()
            signature = bytes.fromhex(signature_pem.decode('utf-8'))
        with open('NovaPastaArq/Mensagem.txt', 'rb') as arq:
            texto = arq.read()
    case '2':
        with tarfile.open('PastaArqCifrado.tar', 'r') as arquivo_tar:
            arquivo_tar.extractall('NovaPastaArqCifr')
        with open('NovaPastaArqCifr/signature.pem', 'rb') as signature_file:
            signature_pem = signature_file.read()
            signature = bytes.fromhex(signature_pem.decode('utf-8'))
        with open('NovaPastaArqCifr/textocifrado.txt', 'rb') as arq:
            textocifrado = arq.read()
        with open('key.data', 'rb') as arq:
            key = arq.read()
        dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
        texto = dcipher.decrypt(textocifrado)

try:
    public_key.verify(signature, texto, hashes.SHA256())
    print("A assinatura é válida. A mensagem é autêntica.")
except dsa.InvalidSignature:
    print("A assinatura é inválida. A mensagem pode ter sido alterada ou a chave pública está incorreta.")