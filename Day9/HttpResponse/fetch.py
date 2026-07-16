#GET - fetch a user

import requests
BASE_URL="https://jsonplaceholder.typicode.com"
response=requests.get(f"{BASE_URL}/users/1")
print(response.status_code) 
print(response.json())

#Post - create a new user
new_post={"title":"Hello","body":"world","userId":50}
response=requests.post(f"{BASE_URL}/posts",json=new_post)
print(response.status_code)
print(response.json())

#PUT,PATCH - partial update
response=requests.patch(f"{BASE_URL}/posts/1",json={"title":"Updated!"})
print(response.status_code)
print(response.json())

#delete
response=requests.delete(f"{BASE_URL}/posts/1")
print(response.status_code)
print(response.json())
