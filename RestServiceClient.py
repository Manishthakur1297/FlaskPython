import requests;

url = "http://localhost:5000/"

result = requests.get(url).json();
print(result)

url1 = "http://localhost:5000/displayAll/"

result = requests.get(url1).json();
print(result)
