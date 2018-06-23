#!/usr/bin/python

import urllib.request
from bs4 import BeautifulSoup 

website="http://php.net"

#data downloading

web_data=urllib.request.urlopen(website)

#printing data

#print(web_data.read())

#reading data with html tags

clean_data=web_data.read()

get_clean=BeautifulSoup(clean_data,'html5lib')

#getting data test format

final_data=get_clean.get_text()

#removing unwanted spaces
good_data=final_data.strip()

#print(good_data)

new_data=[]

for i in good_data:
	j=i.split()
	new_data.append(j)
	print(new_data)
