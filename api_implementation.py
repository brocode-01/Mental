# import json
# import requests

# # URL of the FastAPI endpoint
# url = 'http://localhost:7860/diabetes_prediction'

# # Input data for the model
# input_data_for_model = {
#     'pregnancies': 5,
#     'Glucose': 166,
#     'BloodPressure': 72,
#     'SkinThickness': 19,
#     'Insulin': 175,
#     'BMI': 25.8,
#     'DiabetesPedigreeFunction': 0.587,
#     'Age': 51
# }

# # Convert input data to JSON
# input_json = json.dumps(input_data_for_model)

# # Send POST request
# response = requests.post(url, json=input_json)

# # Print the response
# print(response.json())
