import random

"""
Written by Idan Hovav, 27 November 2015. All rights reserved.

This script will be able to send and receive encrypted messages.

To Do:

- make functions (decrypt, encrypt) print out what they're doing

"""

class Encryptor:

	def __init__(self, mod, gen, name):
		self.modulus = mod
		self.generator = gen
		self.name = name
		self.secret = 0
	
	def encrypt(self):
		self.remainder = (self.generator**self.secret) % self.modulus
		return self.remainder

	def decrypt(self, other):
		self.message = (other ** self.secret) % self.modulus
		return self.message



def getPrime(x, y):
	a = 4
	while not is_prime(a):
		a = random.randint(x, y)
	return a

def getGenerator(modulus):
	good = False
	while not good:
		remainders = []
		gen = getPrime(3, 50)
		#print(gen)
		good = True
		for x in range(1, modulus):
			remainders.append((gen ** x) % modulus)
		for y in range(1, modulus):
			if y not in remainders:
				good = False
	return gen

def ask():
	response = input("Would you like to send another message? T or F: ")
	if response == "T":
		return True
	elif response == "F":
		return False
	else:
		return ask()

def is_prime(a):
	"""
	>>> is_prime(4)
	False
	>>> is_prime(5)
	True
	>>> is_prime(6)
	False
	>>> is_prime(7)
	True
	>>> is_prime(8)
	False
	>>> is_prime(9)
	False
	>>> is_prime(10)
	False
	>>> is_prime(11)
	True
	>>> is_prime(12)
	False
	>>> is_prime(13)
	True
	>>> is_prime(14)
	False
	"""
	b = 2
	while b <= math.sqrt(a):
		if a % b == 0:
			return False
		b += 1
	return True

def communicate():
	"""	
	Ask for two names.
	Create public generator and modulus.
	print gen and mod.
	Assign encryptor instances to names.
	pass remainders to each other.
	Have both sides decrypt, print secret message.
	want to pass another message?

	"""
	cont = True
	while cont:
		a = input('Enter a name for person 1: ')
		b = input('Enter a name for person 2: ')
		publicMod = getPrime(20, 400)
		publicGen = getGenerator(publicMod)

		print("The public modulus is   " + str(publicMod) + ".")
		print("The public generator is " + str(publicGen) + ".")


		a = Encryptor(publicMod, publicGen, a)
		b = Encryptor(publicMod, publicGen, b)
		a.secret = int(input(a.name + ", what's your secret number? "))
		b.secret = int(input(b.name + ", what's your secret number? "))

		aMessage = a.encrypt()
		bMessage = b.encrypt()

		print(a.name + " passes the number " + str(aMessage) + " to " + b.name + ".")
		print(b.name + " passes the number " + str(bMessage) + " to " + a.name + ".")

		print("Then, they can both calculate the shared message using their secret numbers.")
		aMessage, bMessage = a.decrypt(bMessage), b.decrypt(aMessage)
		if aMessage == bMessage:
			print("It worked! The shared message is " + str(aMessage) + ".")
		else:
			print("Something went wrong. The two messages we got were " + str(aMessage) + " and " + str(bMessage) + ".")
		cont = ask()
	print("Thank you for playing!")


if __name__ == "__main__":
	communicate()







