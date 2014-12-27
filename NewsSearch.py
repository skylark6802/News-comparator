import urllib2
import simplejson

###Search
###url = ('https://ajax.googleapis.com/ajax/services/search/news?' + 'v=1.0&q=barack%20obama&userip=INSERT-USER-IP')


#
url = ('https://ajax.googleapis.com/ajax/services/search/news?' + 'v=1.0&userip=INSERT-USER-IP&topic=h&rsz=8&ned=tw')


request = urllib2.Request(url, None)
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
for a in results:
    print a
data = results['responseData']
details = results['responseDetails']
status = results['responseStatus']
print " - - - - - - - "
dataCursor = data['cursor']
dataResults = data['results']
for a in dataResults:
    print a['title']
    print "contest:", a['content']
    
    try:
        related = a['relatedStories']
        print "relatedUrl:"
        for ele in related:
            print ele['titleNoFormatting']
    except:
        pass

    print ""
 

                
# now have some fun with the results...
