import requests
import re

url = input('Input url (with http://), please:').strip()
res = requests.get(url)
if res.status_code == 200:
    st = re.findall(r'<a[\w\s\'\"\;\=-]*href=[\'"]?[h,H,t,T,p,P,s,S,f,F]{0,5}[:\/]{0,3}([\w\.-]*)', res.text)
    
st = sorted(set(st))
for i in st:
    print(i)