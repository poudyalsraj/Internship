
#!/usr/bin/python3


from bs4 import BeautifulSoup
import re

import urllib.request

try:
	m=0
	#functin define:
	def headlineNews():
		z=i.find('a').text
		print(m,'. ', z )
	


	url=input("Enter the url: ")
#checking url:
	s=re.findall(r'^(http://www.|http://|www.)setopati.com$|^setopati.com$|104.24.26.75', url, re.I)
	if s:
		page = urllib.request.urlopen("http://setopati.com") #url opened

	e=re.findall(r'^(http://|https://|www.)ekantipur.*|^ekantipur.*|103.48.88.4', url, re.I)	
	if e:
		page = urllib.request.urlopen("http://ekantipur.com") #url opened
	r=re.findall(r'^(http://|https://|www.)ratopati.*|^ratopati.*|202.51.74.195', url, re.I)
	if r:
			page = urllib.request.urlopen("http://ratopati.com") #url opened


	l=re.findall(r'^(http://|https://|www.)lightnews.*|^lightnepal.*|45.76.11.61', url, re.I)
	if l:
		page = urllib.request.urlopen("http://lightnepal.news") #url opened


	web = BeautifulSoup(page, 'lxml')#it takes all content of webpage to web variable
	
#this is for setopati.com
	for i in web.find_all('h2',class_="entry-title"):
		m=m+1
		if m>11:
			break
		headlineNews()

#this is for ekantipur.com
	for i in web.find_all('div', class_="display-news-title"):
		m=m+1
		if m>11:
			break
		headlineNews()

#this is for ratopati.com

	for i in web.find_all('div', class_ ="item-content"):
		m=m+1
		if m>11:
			break
		headlineNews()

#this is for light nepal.news
	for i in web.find_all('div',class_="main-list small-list clearfix"):
		m=m+1
		if m>11:
			break
		headlineNews()
except Exception as e: 
	print (e)	
	print('Not connected!!')
	print('check url pattern!')
	print ('check internet connection! ')
