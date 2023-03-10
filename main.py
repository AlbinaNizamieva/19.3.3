import requests

status='available'
res_get = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
                   params={'status': 'available'}, headers={'accept': 'application/json'})


res_post = requests.post(f"https://petstore.swagger.io/v2/pet/findByStatus",
                         headers={'accept': 'application/json'}, data={'name': 'Azot'})

res_del = requests.delete(f"https://petstore.swagger.io/v2/pet/findByStatus",
                         headers={'accept': 'application/json'}, data={'name': 'Azot'})

res_put = requests.put(f"https://petstore.swagger.io/v2/pet/findByStatus", data={'name': 'Azot'})

print(res_get.status_code)
print('GET: ', res_get.text)
print('POST: ', res_post.text)
print('PUT: ', res_put.text)
print('dELETE: ', res_del.text)



