import requests
import json
import threading
import time
email="dick@dickmail.com
pas="dick.py"
dev=""
api="https://proxypp124.herokuapp.com"
def log(email, password,device):
   data={
       "email":email,
       "password":password,
       "device":device}
   data=json.dumps(data)
   response=requests.post(f"{api}/login",data=data)
   if response.json()["api:statuscode"]==69:
   	print(response.json()["api:message"])
   	time.sleep(7)
   	res=requests.post(f"{api}/login",data=data).json()["sid"]
   	return res
   else:
   	return response.json()["sid"]
	
sid=log(email,pas,dev)
