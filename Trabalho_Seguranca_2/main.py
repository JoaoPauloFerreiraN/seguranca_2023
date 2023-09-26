from Crypto import Cipher
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

escolha = input("Escolha a opção para criptografar:\n 1 - Texto \n 2 - Arquivo Binário\n")
escolhaChave = input("Escolha a opção para a quantidade de bits da chave:\n 1 - 128 \n 2 - 256\n")
escolhaModo = input("Escolha o modo para criptografar:\n1 - ECB\n2 - CBC\n3 - CFB\n4 - OFB\n5 - CTR")

iv = os.urandom(16) #Criação de um vetor de inicialização, utilizado por alguns modos.
if escolhaChave == '1':
    key = get_random_bytes(16)
else:
    key = get_random_bytes(32)

if escolha == "1":
    textoNormal = input("Escreva o texto a ser criptografado: ").encode() # Pega o texto digitado pelo usuario.
    textoNormal2 = "Texto direto do codigo".encode() # texto direto no codigo
    match escolhaModo:
        case '1':
            #ECB - Cifra direta em blocos, por isso a utilização de um PAD para incrementar um bloco que pode não ter o numero sulficiente de bits
            cipher = AES.new(key, AES.MODE_ECB)
            c = cipher.encrypt(pad(textoNormal, AES.block_size))
            c2 = cipher.encrypt(pad(textoNormal2, AES.block_size))
            print(c)
            print(c2)
            dcipher = AES.new(key, AES.MODE_ECB)
            d = unpad(dcipher.decrypt(c), AES.block_size)
            d2 = unpad(dcipher.decrypt(c2), AES.block_size)
            print(d)
            print(d2)
        case '2':
            #CBC - Igual o ECB porem utiliza um vetor de inicialização (iv)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            c = cipher.encrypt(pad(textoNormal, AES.block_size))
            c2 = cipher.encrypt(pad(textoNormal2, AES.block_size))
            print(c)
            print(c2)
            dcipher = AES.new(key, AES.MODE_CBC, iv)
            d = unpad(dcipher.decrypt(c), AES.block_size)
            d2 = unpad(dcipher.decrypt(c2), AES.block_size)
            print(d)
            print(d2)
        case '3':
            # CFB -  pseudo random stream depends on the plaintext,
            # a different nonce or random IV is needed for every message,
            # like with CTR and OFB using nonces message encryption is possible without per message
            # randomness, decryption is parallelizable /
            # encryption is not, transmission errors completely destroy the
            # following block, but only effect the wrong bits in the current block
            cipher = AES.new(key, AES.MODE_CFB, iv)
            c = cipher.encrypt(textoNormal)
            c2 = cipher.encrypt(textoNormal2)
            print(c)
            print(c2)
            dcipher = AES.new(key, AES.MODE_CFB, iv)
            d = dcipher.decrypt(c)
            d2 = dcipher.decrypt(c2)
            print(d)
            print(d2)
        case '4':
            # OFB
            cipher = AES.new(key, AES.MODE_OFB, iv)
            c = cipher.encrypt(textoNormal)
            c2 = cipher.encrypt(textoNormal2)
            print(c)
            print(c2)
            dcipher = AES.new(key, AES.MODE_OFB, iv)
            d = dcipher.decrypt(c)
            d2 = dcipher.decrypt(c2)
            print(d)
            print(d2)
        case '5':
            # CTR
            cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            c = cipher.encrypt(textoNormal)
            c2 = cipher.encrypt(textoNormal2)
            print(c)
            print(c2)
            dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            d = dcipher.decrypt(c)
            d2 = dcipher.decrypt(c2)
            print(d)
            print(d2)
        case _:
            print("Informacao nao identificada")
else:
    with open('Foto.png', 'rb') as file:
        original = file.read()
        match escolhaModo:
            case '1':
                # ECB -
                cipher = AES.new(key, AES.MODE_ECB)
                c = cipher.encrypt(pad(original, AES.block_size))
                file_out = open('FotoCifrada.png', 'wb')
                file_out.write(c)
                file_out.close()
                dcipher = AES.new(key, AES.MODE_ECB)
                d = unpad(dcipher.decrypt(c), AES.block_size)
                file_out = open('FotoDecifrada.png', 'wb')
                file_out.write(d)
                file_out.close()
            case '2':
                # CBC -
                cipher = AES.new(key, AES.MODE_CBC, iv)
                c = cipher.encrypt(pad(original, AES.block_size))
                file_out = open('FotoCifrada.png', 'wb')
                file_out.write(c)
                file_out.close()
                dcipher = AES.new(key, AES.MODE_CBC, iv)
                d = unpad(dcipher.decrypt(c), AES.block_size)
                file_out = open('FotoDecifrada.png', 'wb')
                file_out.write(d)
                file_out.close()
            case '3':
                # CFB
                cipher = AES.new(key, AES.MODE_CFB, iv)
                c = cipher.encrypt(pad(original, AES.block_size))
                file_out = open('FotoCifrada.png', 'wb')
                file_out.write(c)
                file_out.close()
                dcipher = AES.new(key, AES.MODE_CFB, iv)
                d = unpad(dcipher.decrypt(c), AES.block_size)
                file_out = open('FotoDecifrada.png', 'wb')
                file_out.write(d)
                file_out.close()
            case '4':
                # OFB
                cipher = AES.new(key, AES.MODE_OFB, iv)
                c = cipher.encrypt(pad(original, AES.block_size))
                file_out = open('FotoCifrada.png', 'wb')
                file_out.write(c)
                file_out.close()
                dcipher = AES.new(key, AES.MODE_OFB, iv)
                d = unpad(dcipher.decrypt(c), AES.block_size)
                file_out = open('FotoDecifrada.png', 'wb')
                file_out.write(d)
                file_out.close()
            case '5':
                # CTR
                cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
                c = cipher.encrypt(original)
                c2 = cipher.encrypt(original)
                file_out = open('FotoCifrada.png', 'wb')
                file_out.write(c)
                file_out.close()
                dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
                d = dcipher.decrypt(c)

                d2 = dcipher.decrypt(c2)
                file_out = open('FotoDecifrada.png', 'wb')
                file_out.write(d)
                file_out.close()
            case _:
                print("Informacao nao identificada")