import json
#URL in json format for latest wallpaper
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

#Try with python3
try:
    from urllib.request import urlopen
    response = urlopen(url)
    output = response.readall().decode('utf-8')
    data = json.loads(output)
    output_url = "http://www.bing.com/" + data["images"][0]["url"]
    print(output_url) #Prints url to the image. Passes this on to the Automator workflow

#Else use python2
except:
    from urllib2 import urlopen
    response = urlopen(url)
    output = response.read()
    data = json.loads(output)
    output_url = "http://www.bing.com/" + data["images"][0]["url"]
    print(output_url) #Prints url to the image. Passes this on to the Automator workflow

