import tarfile
from Funcs import *
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa, ec


with open('Arquivo.txt', 'rb') as arq:
        data = arq.read()

hashArq = calchash256(data)

with open('hashArq.txt', 'w') as hash:
    hash.write(hashArq)

#Geração de um Salt aleatorio
salt = get_random_bytes(16)
# Geração da Chave simetrica
key = get_random_bytes(32)


opcao = input("Digite um tipo de transmissão: ")
while opcao != 's':
    match opcao:
        case 'a':
            ########### SENDER ##########
            # Geração do arquivo tar
            with tarfile.open('PastaA.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('hashArq.txt')
            # Criptografia do arquivo tar
            with open('PastaA.tar', 'rb') as file_in:
                data3 = file_in.read()
            # Criptografia AES no modo CTR com counter de 128 bits
            cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            c = cipher.encrypt(data3)
            # Escreve o arquivo criptografado
            file_out = open('criptoPastaA.tar', 'wb')
            file_out.write(c)
            file_out.close()

            ########### RECIVER ##########
            # Descriptografia do arquivo tar
            with open('criptoPastaA.tar', 'rb') as arqdecript:
                    data2 = arqdecript.read()
            # Descriptografia AES no modo CTR com counter de 128 bits
            dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            d = dcipher.decrypt(data2)
            # Escreve o arquivo descriptografado
            file_out = open('decriptoPastaA.tar', 'wb')
            file_out.write(d)
            file_out.close()
            # Extrai o arquivo tar
            with tarfile.open('decriptoPastaA.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovaPastaA')
            # Calcula o hash do arquivo descriptografado
            with open('NovaPastaA/Arquivo.txt', 'rb') as arq:
                dataA = arq.read()
            hash2 = calchash256(dataA)
            # Le o hash do arquivo descriptografado
            with open('NovaPastaA/hashArq.txt', 'rb') as arq:
                hash2A = arq.read()
            # Comparação dos hashes
            print(hash2.hex())
            print(hash2A.decode('utf-8'))

        case 'b':
            ########### SENDER ##########
            # Criptografia do hash do arquivo
            cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            c = cipher.encrypt(hashArq)
            # Escreve o hash criptografado
            file_out = open('hashCripto.txt', 'wb')
            file_out.write(c)
            file_out.close()
            # Geração do arquivo tar
            with tarfile.open('PastaB.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('hashCripto.txt')

            ########### RECIVER ##########
            # Extrai o arquivo tar
            with tarfile.open('PastaB.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovapastaB')
            # Calcula o hash do arquivo descriptografado
            with open('NovapastaB/Arquivo.txt', 'rb') as arq:
                dataB = arq.read()
            hash2 = calchash256(dataB)
            # Descriptografia do hash do arquivo
            with open('NovapastaB/hashCripto.txt', 'rb') as arqdecript:
                    data2B = arqdecript.read()
            dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            d = dcipher.decrypt(data2B)
            # Comparação dos hashes
            print(d.hex())
            print(hash2.hex())
        case 'c':
            # Gerar chaves RSA
            geraChaveRSA()
            ########### SENDER ##########
            # Criptografia do hash do arquivo
            with open("public_rsa_key.pem", "rb") as arquivo_chave_publica_RSA:
                public_key_RSA = serialization.load_ssh_public_key(
                    arquivo_chave_publica_RSA.read(), backend=None)
            hash_crypto = public_key_RSA.encrypt(hashArq, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                        algorithm=hashes.SHA256(),
                                                                        label=None))
            # Escreve o hash criptografado
            file_out = open('hashCriptoRSA.txt', 'wb')
            file_out.write(hash_crypto)
            file_out.close()
            # Geração do arquivo tar
            with tarfile.open('PastaC.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('hashCriptoRSA.txt')

            ########### RECIVER ##########
            # Extrai o arquivo tar
            with tarfile.open('PastaC.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovapastaC')
            # Calcula o hash do arquivo 
            with open('NovapastaC/Arquivo.txt', 'rb') as arq:
                dataC = arq.read()
            hash2 = calchash256(dataC)
            # Descriptografia do hash do arquivo
            with open('NovapastaC/hashCriptoRSA.txt', 'rb') as arqdecript:
                    data2C = arqdecript.read()
            with open("private_rsa_key.pem", "rb") as arquivo_chave_privada_RSA:
                private_key_RSA = serialization.load_pem_private_key(arquivo_chave_privada_RSA.read(), password=None)
            hash_decryto = private_key_RSA.decrypt(data2C, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(),
                                                        label=None))
            # Comparação dos hashes
            print(hash2.hex())
            print(hash_decryto.hex())

        case 'd':
            # Gerar chaves RSA
            geraChaveRSA()
            ########### SENDER ##########
            # Criptografia do hash do arquivo
            with open("public_rsa_key.pem", "rb") as arquivo_chave_publica_RSA:
                public_key_RSA = serialization.load_ssh_public_key(
                    arquivo_chave_publica_RSA.read(), backend=None)
            hash_crypto = public_key_RSA.encrypt(hashArq, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                    algorithm=hashes.SHA256(),
                                                                    label=None))
            # Escreve o hash criptografado
            file_out = open('hashCriptoRSA.txt', 'wb')
            file_out.write(hash_crypto)
            file_out.close()
            # Geração do arquivo tar
            with tarfile.open('PastaD.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('hashCriptoRSA.txt')
            # Criptografia do arquivo tar
            with open('PastaD.tar', 'rb') as pasta:
                arquivoD = pasta.read()
            cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            c = cipher.encrypt(arquivoD)
            # Escreve o arquivo criptografado
            file_out = open('CriptoPastaD.tar', 'wb')
            file_out.write(c)
            file_out.close()

            ########### RECIVER ##########
            # Descriptografia do arquivo tar
            with open('CriptoPastaD.tar', 'rb') as arq:
                dataCriptD = arq.read()
            dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            d = dcipher.decrypt(dataCriptD)
            # Escreve o arquivo descriptografado
            file_out = open('DecriptPastaD.tar', 'wb')
            file_out.write(d)
            file_out.close()
            # Extrai o arquivo tar
            with tarfile.open('PastaD.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovaPastaD')
            # Calcula o hash do arquivo descriptografado
            with open('NovapastaD/Arquivo.txt', 'rb') as arq:
                dataD = arq.read()
            hashD = calchash256(dataD)
            # Descriptografia do hash do arquivo
            with open('NovapastaD/hashCriptoRSA.txt', 'rb') as arqdecript:
                    data2D = arqdecript.read()
            with open("private_rsa_key.pem", "rb") as arquivo_chave_privada_RSA:
                private_key_RSA = serialization.load_pem_private_key(arquivo_chave_privada_RSA.read(), password=None)
            hash_decryto = private_key_RSA.decrypt(data2D, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(),
                                                        label=None))
            # Comparação dos hashes
            print(hashD.hex())
            print(hash_decryto.hex())

        case 'e':
            ########### SENDER ##########
            # Gerar hash do arquivo + salt
            with open('Arquivo.txt', 'rb') as arq:
                dataE = arq.read()
            hashE = calchash256(dataE+salt)
            # Escreve o hash criptografado
            file_out = open('HashE.txt', 'wb')
            file_out.write(hashE)
            file_out.close()
            # Geração do arquivo tar
            with tarfile.open('PastaE.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('HashE.txt')

            ########### RECIVER ##########
            # Extrai o arquivo tar
            with tarfile.open('PastaE.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovaPastaE')
            # Calcula o hash do arquivo descriptografado
            with open('NovaPastaE/Arquivo.txt', 'rb') as arq:
                novodataE = arq.read()
            hashE = calchash256(novodataE+salt)
            with open('NovaPastaE/HashE.txt', 'rb') as arq:
                HashE2 = arq.read()
            # Comparação dos hashes
            print(hashE.hex())
            print(HashE2.hex())

        case 'f':
            ########### SENDER ##########
            # Gerar hash do arquivo + salt
            with open('Arquivo.txt', 'rb') as arq:
                dataF = arq.read()
            hashF = calchash256(dataF+salt)
            # Escreve o hash criptografado
            file_out = open('HashF.txt', 'wb')
            file_out.write(hashF)
            file_out.close()
            # Geração do arquivo tar
            with tarfile.open('PastaF.tar', 'w') as tar:
                tar.add('Arquivo.txt')
                tar.add('HashF.txt')
            # Criptografia do arquivo tar
            with open('PastaF.tar', 'rb') as pasta:
                arquivoF = pasta.read()
            cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            c = cipher.encrypt(arquivoF)
            # Escreve o arquivo criptografado
            file_out = open('CriptoPastaF.tar', 'wb')
            file_out.write(c)
            file_out.close()
            
            ########### RECIVER ##########
            # Descriptografia do arquivo tar
            with open('CriptoPastaF.tar', 'rb') as arq:
                dataCriptF = arq.read()
            dcipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(nbits=128))
            d = dcipher.decrypt(dataCriptF)
            # Escreve o arquivo descriptografado
            file_out = open('DecriptPastaF.tar', 'wb')
            file_out.write(d)
            file_out.close()
            # Extrai o arquivo tar
            with tarfile.open('DecriptPastaF.tar', 'r') as arquivo_tar:
                arquivo_tar.extractall('NovaPastaF')
            # Calcula o hash do arquivo descriptografado
            with open('NovaPastaF/Arquivo.txt', 'rb') as arq:
                novodataF = arq.read()
            hashF = calchash256(novodataF+salt)
            with open('NovaPastaF/HashF.txt', 'rb') as arq:
                HashF2 = arq.read()

            # Comparação dos hashes
            print(hashF.hex())
            print(HashF2.hex())
    opcao = input("Digite um tipo de transmissão: ")

