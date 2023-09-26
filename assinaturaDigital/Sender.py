
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


def assinarDoc(arquivo):
    with open('private_key.pem', 'rb') as private_key_file:
        private_key_pem = private_key_file.read()
        private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    with open(arquivo, 'rb') as arq:
        texto = arq.read()
    signature = private_key.sign(texto, hashes.SHA256())
    signature_pem = signature.hex().encode('utf-8')

    return signature_pem


