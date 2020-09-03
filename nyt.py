#!/usr/bin/env python3


import requests, shutil, sys
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
  url = ' '.join(sys.argv[1:])
else:
  print('Please enter a URL')


# url = 'https://www.ft.com/content/9cc779aa-d4b3-48d9-8878-f6690b4e34f3'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1')
main = soup.find_all('p')

# for text in soup:
#   p_tag = text.find_all('p')
with open(title.text.strip()[:10] + '.txt', 'w') as f:
  f.write(title.text.strip() + '\n'*2)
  for p in main:
    f.write(p.text.strip()+'\n'*2)
  
print('The article was created!')
print(title.text.strip())