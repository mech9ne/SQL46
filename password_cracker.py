import hashlib

def crack_password(password_hash):
	dictionary=["123456","qwerty","letmein"]
	for word in dictionary:
		hash_object=hashlib.md5(word.encode())
		
		if(hash_object.hexdigest()==str(password_hash)):
			return word
			
	return None 

print(crack_password(hashlib.md5(b'mypassword').hexdigest()))
