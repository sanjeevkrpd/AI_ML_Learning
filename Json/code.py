# import json

# with open("Json/data.json", "r") as f:
#     data = json.load(f)  

# print(data)




# import json

# data = {
#     "name": "sanjeev kumar",
#     "email": "sanjeevkrpd11@gmail.com",
#     "age": "22",
#     "paymentStatus": True
# }

# with open("Json/data.json", "w") as f:
#    json.dump(data, f, indent=4)

import json
data = {
"name": "John",
"age": 25,
"marks": [85, 90, 92]
}



son_string = json.dumps(data)

with open("Json/data.json", "w") as f:
    f.write(son_string)
