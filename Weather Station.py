def main():
    import requests
    import json

    url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A6C16568-8982-44E3-9509-4AEE4B4E16EF"

    try:
        r = requests.get(url)
        # json takes the URL and converts it to a form which can be 
        # interpreted by python.
        api = json.loads(r.content)
        # The api is a list and within the list is a dictionary.
        # We can noe extract desired values within the dictionary.
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
    except Exception as e:
        api = "Error"

    print(city + " " + "Air Quality: " + str(quality) + " " + "Category :" + " " + category)

if __name__== "__main__":
  main()




