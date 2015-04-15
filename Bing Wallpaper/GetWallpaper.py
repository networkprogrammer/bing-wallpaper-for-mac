import json

#Try with python3
try:
    from urllib.request import urlopen, urlretrieve
    from urllib.request import urlretrieve

#Else try python2
except:
    from urllib2 import urlopen
    from urllib import urlretrieve

from os import path


#User home folder
homeFolder = path.expanduser("~")

#Save pictures to a folder
pictureLocation = homeFolder + "/Downloads/"


def main():
    ########Defining variables#######

    #URL in json format for latest wallpaper
    url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
    
    getHighRes = 1 #Manually change the resolution in the url to 1920x1200. Change to 0 if url breaks.

    #Get json response from bing.com
    response = urlopen(url)

    #Trying python 3
    try:
        output = response.readall().decode('utf-8')

    #Else trying python2
    except:
           output = response.read()
           
    #Get json output
    data = json.loads(output)

    #Form image url from json
    output_url = "http://www.bing.com/" + data["images"][0]["url"]

    #Form 1920x1200 image from above url
    output_url_highres = output_url.replace("1080", "1200")


    #If higher resolution is preferred(default)
    if getHighRes == 1:
        
        #Use try block to catch any failure in getting the high res image
        try:
            process_url(output_url_highres)

        except:
            process_url(output_url)

    else:
        process_url(output_url)


def process_url(image_url):
    
    #Get the filename of the new file from the url
    filename = pictureLocation + image_url.split('/')[-1]

    #Retrieve the image from the web and save it to desired location
    req = urlretrieve(image_url, filename)

    #Save the file path + filename to the output variable
    bingImage = path.abspath(filename)
    print(bingImage)


main()
