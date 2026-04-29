import requests

user_id = {
    'username':'admin',
    'password':'password123'
}

header = {
    'Content-Type: application/json'
}

# token_generation = requests.post('https://restful-booker.herokuapp.com/auth',data=user_id)
# print(token_generation.status_code)
# print(token_generation.text)

get_booking_id = requests.get(url='https://restful-booker.herokuapp.com/booking/1079')
print(get_booking_id.status_code)
print(get_booking_id.text)

url = "https://restful-booker.herokuapp.com/booking/"
data = {
    "firstname" : "Jimmy",
    "lastname" : "Bl",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
     # "Cookie": "b5e632352cf0ef1"
}

{"token":"2a52dfb63bc6138"}
response = requests.post(url, json=data,headers=headers)
print(response.status_code)
print(response.text)


