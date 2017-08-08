import http.client
import json
from urllib.parse import quote_plus
 
base = '/maps/api/geocode/json'
 
def geocode(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(reply['results'][0]['geometry']['location'])
 
if __name__ == '__main__':
	geocode('307 Diamond Hill Rd, Berkeley Heights, NJ')