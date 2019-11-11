import hashlib
import sys


def brute_force(wordlist,hash1,op2):
	if op2 == 1:
		with open(wordlist) as file:
			for line in file:
				brute_hash = hashlib.md5(line.rstrip().encode())
				brute_hash = brute_hash.hexdigest()
				if brute_hash == hash1:
					print("\n<-> Decodificacao do Hash MD5 - " + line)
					cont = 1
				else:
					cont = 0
	if op2 == 2:
		with open(wordlist) as file:
			for line in file:
				brute_hash = hashlib.sha1(line.rstrip().encode())
				brute_hash = brute_hash.hexdigest()
				if brute_hash == hash1:
					print("\n<-> Decodificacao do Hash Sha1 - " + line)
					cont = 1
				else:
					cont = 0
	if op2 == 3:
		with open(wordlist) as file:
			for line in file:
				brute_hash = hashlib.sha256(line.rstrip().encode())
				brute_hash = brute_hash.hexdigest()
				if brute_hash == hash1:
					print("\n<-> Decodificacao do Hash Sha256- " + line)
					cont = 1
				else:
					cont = 0
	if op2 == 4:
		with open(wordlist) as file:
			for line in file:
				brute_hash = hashlib.sha512(line.rstrip().encode())
				brute_hash = brute_hash.hexdigest()
				if brute_hash == hash1:
					print("\n<-> Decodificacao do Hash Sha512- " + line)
					cont = 1
				else:
					cont = 0
	if cont == 0:
		print("\n>-< Nenhum Hash encontrado.")

			
def main():
	print("############################################")
	print("############## O p c o e s #################")
	print("############################################")
	print("\n 1 - Text to MD5 \n 2 - Text to Sha1 \n 3 - Text to Sha256 \n 4 - Text to Sha512 \n 5 - Brute Force \n 0 - Exit")
	op1 = input("[+][+] ")

	if op1 == 1:
		string_limpa = raw_input("Informe o texto original: ")
		string_hash = hashlib.md5(string_limpa.encode())
		print(">>Hash: " + string_hash.hexdigest())
	elif op1 == 2:
		string_limpa = raw_input("Informe o texto original: ")
		string_hash = hashlib.sha1(string_limpa.encode())
		print(">>Hash: " + string_hash.hexdigest())
	elif op1 == 3:
		string_limpa = raw_input("Informe o texto original: ")
		string_hash = hashlib.sha256(string_limpa.encode())
		print(">>Hash: " + string_hash.hexdigest())
	elif op1 == 4:
		string_limpa = raw_input("Informe o texto original: ")
		string_hash = hashlib.sha512(string_limpa.encode())
		print(">>Hash: " + string_hash.hexdigest())
	elif op1 == 5:
		wordlist = raw_input(">> Informe a wordlist: ")	
		hash1 = raw_input(">> Informe o hash: ")
		op2 = input(">> Informe o tipo do Hash \n 1 - MD5 \n 2 - Sha1 \n 3 - Sha256 \n 4 - Sha512 \n")
		brute_force(wordlist,hash1,op2)
	else:
		print("\n Bye, bye!")
		
if __name__ == '__main__':
	main()
