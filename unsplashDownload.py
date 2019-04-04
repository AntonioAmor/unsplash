import requests
from PIL import Image
from io import BytesIO

payload = {'client_id': 'XXXXXX','count':2}

r = requests.get('https://api.unsplash.com/photos/random/', params=payload)

for i in range(len(r.json())):
    id=r.json()[i]['id']
    url=r.json()[i]['urls']['raw']
    img=requests.get(url)

    img=Image.open(BytesIO(img.content))
    img.show()
    #img.save(id+'.raw')
