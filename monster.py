#! /usr/bin/env python3

import requests, sys
from bs4 import BeautifulSoup


# join with '-'
if len(sys.argv) < 2:
  print('This needs at least one arguement')
elif len(sys.argv) == 2:
  search_term = sys.argv[1]
  location = 'Denver'
else:
  search_term = sys.argv[1]
  location = sys.argv[2]


url = 'https://www.monster.com/jobs/search/?q=' + search_term + '&where=' + location + '&tm=7'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for job in job_elems:
  # print(job, end='\n'*3)
  title = job.find('h2', class_='title')
  time = job.find('time')
  company = job.find('div', class_='company')
  location = job.find('div', class_='location')
  anchor = job.find('a', href=True)
  if None in (title, anchor):
    continue
  print(title.text.strip())
  print(company.text.strip())
  print(time.text.strip())
  print(location.text.strip())
  print(anchor['href'])
  print()
