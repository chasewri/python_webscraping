import requests, shutil, sys
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
  url = ' '.join(sys.argv[1:])
else:
  print('Please enter a URL')
# url = 'https://www.washingtonpost.com/politics/2020/08/26/retirement-community-postal-workers-has-message-deliver-trump-trust-mail/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1')
subtitle = soup.find('h2')
page_content = soup.find_all('p', class_='font--body')

# f = open(title.text.strip() + '.txt', 'w')
# f.write('New file?? \n\n')
# f.write(title.text.strip())
# f.close()

with open(title.text.strip()[:10] + '.txt', 'w') as f:
  f.write(title.text.strip() + '\n\n')
  if (subtitle is not None):
    f.write(subtitle.text.strip() + '\n\n')
  for content in page_content:
    f.write(content.text.strip() + '\n\n')
    
print('The article was created!')
print(title.text.strip())
# print(title.text.strip())
# print()
# print(subtitle.text.strip())
# print()
# for content in page_content:
#   print(content.text.strip())
#   print()