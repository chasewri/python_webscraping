#!/usr/bin/env python3

import requests, shutil, sys, os
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
  url = ' '.join(sys.argv[1:])
else:
  print('Please enter a URL')

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1')
main = soup.find_all('p')

with open(title.text.strip()[:10] + '.txt', 'w') as f:
  f.write(title.text.strip() + '\n'*2)
  for p in main:
    f.write(p.text.strip()+'\n'*2)
  
print('The article was created!')
print(title.text.strip())
print('Would you like to convert?')
answer = input()
if answer == 'y' or answer == 'Y':
  os.system("ebook-convert '" + title.text.strip()[:10] + ".txt' '" + title.text.strip()[:10] + ".epub'" )
  print('Would you like to send to Drive?')
  send = input()
  if send == 'Y' or send == 'y':
    os.system("rm '" + title.text.strip()[:10] + ".txt'")
    os.system("mv '" + title.text.strip()[:10] + ".epub' ~/myGoogleDrive/")