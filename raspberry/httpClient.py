import httpx

data = {
    "parking-lot-number" : "52",
    "license-plate" : "abc123"
}

choice = input("1. for checking\n2.for inserting\n")
if int(choice) == 1:
    r = httpx.post('http://localhost:8000/check-plate/', json=data)
elif int(choice) == 2:
    data['parking-lot-number'] = input("Insert parking lot number: ")
    data['license-plate'] = input("Insert license plate: ")
    r = httpx.post('http://localhost:8000/check-plate/add-plate/', json=data)

print(r.status_code)