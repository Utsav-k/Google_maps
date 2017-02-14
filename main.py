#this program gives you the basic information of any City or place names

import urllib
import json

#getting complete url

def get_url(loc):
	serviceurl  ='https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
	url = serviceurl+str(loc)  #encoding url 
	return url
	print url

#extrcting data from web page

def get_json_data(loc):
	m = get_url(loc)
	x = urllib.urlopen(m)
	data  = x.read()
	return data

#converting data intp json format.

def get_js(loc):

	d = get_json_data(loc)
	try:
		js = json.loads(str(d))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print "**** FAilure to Retrieve ****"

	return js
#getting Address

def get_brief_address(loc):
	js = get_js(loc)
	location = js["results"][0]['formatted_address']
	print "\nBrief Address:", location,'\n'

#getting Coordinates.
def get_coordinates(loc):
	js = get_js(loc)
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print "Location Coordinates: "
	print '    Latitide: ',lat
	print '    Longitude: ', lng,'\n'

#getting place ID

def get_place_id(loc):
	js = get_js(loc)
	place_id = js['results'][0]['place_id']
	print 'Place ID: ', place_id, '\n'

#getting region voundaries

def get_boundaries(loc):
	js = get_js(loc)
	northbound = js["results"][0]["geometry"]["bounds"]["northeast"]
	southbound = js["results"][0]["geometry"]["bounds"]["southwest"]

	print"Boundaries: "

	print "  North-East Bound: "
	print "    Latitude:",northbound["lat"]
	print "    Longitude",northbound["lng"]

	print "  South-West Bound: "
	print "    Latitude:",southbound["lat"]
	print "    Longitude",southbound["lng"],'\n'

#combining all the details.
def Get_full_location_details(loc):
	get_brief_address(loc)
	get_coordinates(loc)
	get_boundaries(loc)
	get_place_id(loc)
