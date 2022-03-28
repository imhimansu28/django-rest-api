import requests
import json
URL = "https://devhimanshu28.pythonanywhere.com/stucreate/"

data ={ 
 'id':8,
 'stu_name' : 'Rudra',
 'stu_class': 9,
 'stu_phone': '15678',
 'stu_roll':'126',
 'city':'Lucknow'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)