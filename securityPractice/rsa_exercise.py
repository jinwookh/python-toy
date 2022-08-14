
def makePublicKeyAndPrivateKey():
	p = 11 # prime number. it has to be big enough in practice.
	q = 17 # prime number. it has to be big enough in practice.
	eulerPi = (p-1) * (q-1) # use euler phi function. (φ(phi)) result is 160

	e = 3

	d = 107
	# e * d ≡ 1 mod (p-1)(q-2)
        # has to solve d in 3 * d ≡ 1 mod 160
	# we might have to use euclidean algorithm at here.. but let's just give fix number 107 at here.
	# 107 can be d since 3 * 107  = 160 * k + 1 (k ∈ Z) 

	n = p * q
	firstPublicKey = n
	secondPublicKey = e
	
	privateKey = d

	return {'public': [firstPublicKey, secondPublicKey], 'private': privateKey}

def encode(message, firstPublicKey, secondPublicKey):
	n = firstPublicKey
	e = secondPublicKey
	
	k = 22
	
	c = k * n + message**e # c ≡ m^e mod n
	return c

def decode(encodedMessage, privateKey, firstPublicKey):
	n = firstPublicKey
	decoded = encodedMessage**privateKey % n
	return decoded



keys = makePublicKeyAndPrivateKey()

message = 77 
print("message: ", message)

encoded =  encode(77, keys['public'][0], keys['public'][1])
print("encoded message: ", encoded)

decoded = decode(encoded, keys['private'], keys['public'][0])
print("decoded message: ",  decoded)

