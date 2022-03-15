import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
 'id':1,
 'stu_name' : 'Sonam',
 'stu_class': 11,
 'stu_phone': '123456789',
 'stu_roll':'1234567',
 'city':'Kanpur'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)