import requests

url = "http://127.0.0.1:8000/api/doctors/11/" # Replace with the actual URL
response = requests.delete(url)

print(response.status_code)