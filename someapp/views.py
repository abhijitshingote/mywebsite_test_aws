from django.shortcuts import render
from django.http import HttpResponse
import os
import ast

# Create your views here.
def index(request):
	# return HttpResponse('Hello R A D H I K A !')
	# weatherurl='http://www.metaweather.com/api/location/44418/'
	# temperature=requests.get(weatherurl).json()['consolidated_weather'][0]['the_temp']
	# city=requests.get(weatherurl).json()['title']
	tempdict={}
	# for cityid in ['44418','12586539','2378426','2459115']:
	# 	weatherurl='http://www.metaweather.com/api/location/' + cityid + '/'
	# 	temperature=requests.get(weatherurl).json()['consolidated_weather'][0]['the_temp']
	# 	city=requests.get(weatherurl).json()['title']
	# 	tempdict[city]=temperature
	# context={'city':city,'temperature':temperature}
	path='/Users/abhijitshingote/mywebsite/scripts/weatheroutput.txt'

	with open(path) as handle:
		dictdump = ast.literal_eval(handle.read())

	return render(request,'index.html',context={'tempdict':dictdump})

