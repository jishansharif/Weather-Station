import requests
import json
def main(): 
    url = "https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22"
    read = requests.get(url)
    api = json.loads(read.content)
    cordinates = api["coord"]
    quality = api["weather"]
    trial = quality[0]
    weather = trial["description"]
    print(weather)
    print("Cordinates: " + str(cordinates) + " " + "Air Quality:" + " " + str(weather))
if __name__== "__main__":
  main()




