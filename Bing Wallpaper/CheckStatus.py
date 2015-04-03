import os, datetime

#For python3
try:
    from urllib.request import urlopen
#For python2
except:
    from urllib2 import urlopen

#Get home folder
homeFolder = os.path.expanduser("~")
pictureLocation = homeFolder + "/Pictures/bing-wallpaper/"
appLocation = homeFolder + "/Applications/Bing\ Wallpaper/BingWallpaper.app"
internetConnected = False

#Check to see if there is an active internet connection
try:
    urlopen("http://www.bing.com",timeout=10)
    internetConnected = True
except:
    internetConnected = False


#Flag to see if any jpg file was found in the bing-wallpaper folder
fileExists=0

#Check to see if the bing-wallpaper folder exists in the Pictures directory
if not os.path.exists(pictureLocation):
    #If it does not exist, create the directory
    os.makedirs(pictureLocation)
#Find the jpg file in the bing-wallpaper folder
for f in os.listdir(pictureLocation):
    #if there is a file...
    if os.path.isfile(pictureLocation + f):
        #Check to see if the file ends with jpg. This removes the .DS files
        if f.endswith(".jpg"):
            #Flag that a jpg file was found
            fileExists=1
            file = pictureLocation + f
            #Get change date of the file
            #Returns number of seconds since the epoch
            fileChange = os.path.getctime(file)

            #Convert change time into string
            changeTimeStr = (datetime.datetime.fromtimestamp(fileChange).strftime('%Y-%m-%d %H:%M:%S.%f'))

            #Convert the
            changeTime = datetime.datetime.strptime(changeTimeStr, "%Y-%m-%d %H:%M:%S.%f")

            #Get the time now
            today = datetime.datetime.today()

            #Get the difference between now and the date the file was changed
            c = today.date() - changeTime.date()

            #If the difference is 1 day, then run the app to download a new image, else pass.
            if c.days > 0 and internetConnected==True:
                os.system("open " + appLocation)

#If there was no jpg file in the folder, run the app to get a new wallpaper
if internetConnected==True and fileExists==0:
    os.system("open " + appLocation)


