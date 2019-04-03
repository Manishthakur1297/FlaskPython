import requests;

url = "http://localhost:5000/"

result = requests.get(url).json()
print(result)

url1 = "http://localhost:5000/displayAll/"

result1 = requests.get(url1).json()
print(result1)


# url2 = "http://localhost:5000/create/"

# result2 = requests.get(url2).json()
# print(result2)
