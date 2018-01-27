# This program request data get method:
'''import requests
res = requests.get(url = "http://httpbin.org/ip")
print("[*] Status Code: {}".format (res.status_code))
print("[*] Headers: {}".format (res.headers))'''

# This program build one tool about find ip address:
'''import requests
res = requests.get(url = "http://httpbin.org/ip")
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")
print("[+] Your IP Address: {}".format (res.json()["origin"]))'''

# This program about post data:

'''import requests
res = requests.post(url = "http://httpbin.org/post")
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")
print("[*] Content: {}".format (res.json()))'''

#Sent post data
'''import requests
res = requests.post(url = "http://httpbin.org/post",data = {"name": "payilagam", "Place": "Velacherry"})
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")
print("[*] Content: {}".format (res.json()))'''

#headers 
'''import requests
res = requests.get(url = "http://httpbin.org/headers", headers = {"User-Agent": "Payilagam"})
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")
print("[*] Content: {}".format (res.text))'''

#binary file download:
'''import requests
res = requests.get(url = "http://httpbin.org/image/jpeg")
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")
print("[*] Content: {}".format (res.content))'''

#how do download image: 
'''import requests
res = requests.get(url = "http://httpbin.org/image/jpeg")
print("[*] Status Code: {}".format (res.status_code))
print("\n\n")

f = open("test.jpeg", "wb+")
f.write(res.content)
f.close()
print("[*] Image downloaded")'''
