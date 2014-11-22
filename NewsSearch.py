import urllib2
import simplejson

url = ('https://ajax.googleapis.com/ajax/services/search/news?' + 'v=1.0&userip=INSERT-USER-IP&topic=h')
#url = ('https://ajax.googleapis.com/ajax/services/search/news?' + 'v=1.0&q=barack%20obama&userip=INSERT-USER-IP')


request = urllib2.Request(url, None)
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
print results
# now have some fun with the results...
