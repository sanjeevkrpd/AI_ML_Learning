
# dictionary => key:pair values


dict = {
    "name" : "sanjeev kumar",
    "percentage" : "71%",
    "subject" : ["Maths","Science" ,"S.ST","G.K","Hindi","English"]
}


dict_keys = dict.keys()
print(dict_keys)


dict_values = dict.values()
print(dict_values)


val = dict.items()
print(dict.values)


get_val = dict.get("name")
print((get_val))


dict.update({
    "city" : "Mumbai"
})

print(dict)

