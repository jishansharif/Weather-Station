import requests
import json
def main(): 
    url = "https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22"
    # Requests will allow you to send HTTP requests using Python.
    read = requests.get(url)
    # Json converts the variable read which contains the URL into a format which
    # can be read and interpreted by python.
    api = json.loads(read.content)
    cordinates = api["coord"]
    quality = api["weather"]
    trial = quality[0]
    weather = trial["description"]
    # By extracting relevant information from the api, we can finally print 
    # out the result.
    print("Cordinates: " + str(cordinates) + " " + "Air Quality:" + " " + str(weather))
if __name__== "__main__":
  main()