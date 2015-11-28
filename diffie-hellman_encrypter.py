import random
import math

"""
Written by Idan Hovav, 27 November 2015. All rights reserved.
This script will be able to send and receive encrypted messages.
Note: the shared number at the end is not the secret. It is a key that can be
used for future communication, that is its value.

To Do:

- make the range of publicMod and publicGen customizable by user.

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

def getGenerator(modulus, k, m):
	good = False
	while not good:
		remainders = []
		gen = getPrime(k, m)
		print(gen)
		good = True
		for x in range(1, modulus):
			remainders.append((gen ** x) % modulus)
		for y in range(1, modulus):
			if y not in remainders:
				good = False
				break
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

def encrypt_explanation(name, mod, gen, secret, message):
	print("\n" + name + " raises the public generator, " + str(gen)
		+ ", to the power of their private number, " + str(secret) + ".")
	print("Then, " + name
		+ " finds the modulus of that number with the public modulus, " 
		+ str(mod) + ", and gets " + str(message))
	print("Equation: " + str(gen) + "^" + str(secret) + " mod " + str(mod)
		+ " = " + str(message))

def decrypt_explanation(name, mod, other, secret, shared):
	print("\n" + name + " takes the number they were passed, " + str(other)
		+ ", and raises it" + " to the power of their original secret number, "
		+ str(secret) + ", and again uses the public modulus, " + str(mod) 
		+ ", to find the shared message, " + str(shared) + ".")
	print("Equation: " + str(other) + "^" + str(secret) + " mod " + str(mod)
		+ " = " + str(shared))

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
		publicMod = getPrime(20, 9999)
		print("The public modulus is " + str(publicMod) + ".")
		print("Calculating possible generators for " + str(publicMod) + ":")
		publicGen = getGenerator(publicMod, 3, 500)
		print("The public generator is " + str(publicGen) + ".")

		a = Encryptor(publicMod, publicGen, a)
		b = Encryptor(publicMod, publicGen, b)
		a.secret = int(input(a.name + ", what's your secret number? "))
		b.secret = int(input(b.name + ", what's your secret number? "))

		aMessage = a.encrypt()
		encrypt_explanation(a.name, publicMod, publicGen, a.secret, aMessage)
		print("\n" + b.name + " does the same.")
		bMessage = b.encrypt()
		encrypt_explanation(b.name, publicMod, publicGen, b.secret, bMessage)

		print("\nThen, they pass each other their calculated messages:")
		print(a.name + " passes the number " + str(aMessage) 
			+ " to " + b.name + ".")
		print(b.name + " passes the number " + str(bMessage) 
			+ " to " + a.name + ".")

		print("\nNow, they can both calculate the " 
			+ "shared message using their secret numbers.")
		aShared, bShared = a.decrypt(bMessage), b.decrypt(aMessage)
		decrypt_explanation(a.name, publicMod, bMessage, a.secret, aShared)
		decrypt_explanation(b.name, publicMod, aMessage, b.secret, bShared)

		if aShared == bShared:
			print("\nIt worked! The shared message is " + str(aShared) + ".")
			print("This number is a key for future, secure communication!\n")
		else:
			print("\nSomething went wrong. The two messages we got were " 
				+ str(aShared) + " and " + str(bShared) + ".\n")
		cont = ask()
	print("Thank you for playing!")


if __name__ == "__main__":
	communicate()







