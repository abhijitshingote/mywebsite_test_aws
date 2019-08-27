
import requests
import datetime
# import pandas as pd 
# pd.to_pick
 



tempdict={}
for cityid in ['44418','12586539','2378426','2459115']:
	weatherurl='http://www.metaweather.com/api/location/' + cityid + '/'
	temperature=requests.get(weatherurl).json()['consolidated_weather'][0]['the_temp']
	city=requests.get(weatherurl).json()['title']
	tempdict[city]=temperature
	# tempdict[city]=requests.get(weatherurl).json()



with open('weatheroutput.txt', 'w') as f:
	f.write(str(tempdict)+'\n')
	# f.write(str(datetime.datetime.now())+'\n')

 