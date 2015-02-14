"""
Scrape movie info from omdb. Pretty simple.
"""

import numpy as np 
import pandas as pd
import urllib2
import urllib
import json
import time

# spreadsheet contains movie titles
movie_data = pd.io.excel.read_excel( open('movies2.xlsx','r') )

out=open('out.txt','w')
for i in range(4001,4145) :
	print i
	try :
		if pd.isnull( movie_data['studio'][i] ) :
			name=urllib.quote_plus( movie_data['title'][i] )
			year=urllib.quote_plus( str(movie_data['release year'][i]) )
			json_data= urllib2.urlopen("http://www.omdbapi.com/?t="+name+"&y="+str(year)+"&r=json").read()
			#print json_data
			data = json.loads(json_data)
			out.write( data['Rated']+';'+data['Runtime']+';'+data['Genre']+';'+data['Director']+';'+data['Writer']+';'+data['Actors']+';'+data['Plot']+'\n' )
			time.sleep(5)
		else :
			out.write('Not Found\n')
	except :
		out.write('Error\n')
out.close()