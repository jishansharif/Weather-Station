import requests
import json

url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A6C16568-8982-44E3-9509-4AEE4B4E16EF"

try:
    r = requests.get(url)
    api = json.loads(r.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error"

print(city + " " + "Air Quality: " + str(quality) + " " + "Category :" + " " + category)


# statuscode = r.status code

# Import json and print API response in a variable.
# response_dict = r.json()
# print(response_dict.keys())

# Different keys will show different information, we should print out the
# information relevant to us 

