import json

my_details = {
  "name": "John",
  "age": 24,
  "city": "Kapilvastu"
}
# serialize list to json
dump_to_json = json.dumps(list(my_details))
print(dump_to_json)
print()
# deserialize json to list
load_dict = json.loads(dump_to_json)
print(load_dict)