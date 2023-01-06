import requests
from bs4 import BeautifulSoup
import webbrowser

filePath = 'frames\\frame8.jpg'
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
