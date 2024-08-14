import json
import requests

url = "https://water-prediction-api-1.onrender.com/prediction"

x_new = dict(
    ph = 10.0,
    hardness = 20.0,
    Solids = 30.0,
    Chloramines = 40.0,
    Sulfate = 50.0,
    Conductivity = 60.0,
    Organic_carbon = 70.0,
    Trihalomethanes = 80.0,
    Turbidity = 90.0
)

x_new_json = json.dumps(x_new)
response = requests.post(url, data=x_new_json)

print("Response Text:", response.text)
print("Status Code:", response.status_code)