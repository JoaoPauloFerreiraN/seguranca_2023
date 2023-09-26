import hashlib

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec


def calchash256(arq):
    sha256 = hashlib.sha256()
    sha256.update(arq)
    return sha256.hexdigest()


def geraChaveRSA():
    # Geração das Chave RSA
    chave_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    c_privada_rsa = chave_rsa.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                            serialization.NoEncryption())
    c_publica_rsa = chave_rsa.public_key().public_bytes(serialization.Encoding.OpenSSH,
                                                        serialization.PublicFormat.OpenSSH)
    file_out = open("private_rsa_key.pem", 'wb')
    file_out.write(c_privada_rsa)
    file_out.close()
    file_out = open("public_rsa_key.pem", 'wb')
    file_out.write(c_publica_rsa)
    file_out.close()
