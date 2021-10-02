from urllib.request import urlopen   ##importing necessary library this library contains all the modules for url status checking

name=input("enter your name:")    ## entering the user name

def status():          ## defining the function to check the status
    try:
        urlopen("https://www.youtube.com/",timeout=1)    ## if the url is openable then user is connected 
        print(name,"you are connected to internet")
    except:
        print(name,"you are not connected to internet")   ## otherwise not connected
status()   ## calling the status function