my_string = '{\n    "data": {\n        "id": 2,\n        "email": "jaet.weaver@reqres.i",\n        "first_ame": "Jaet",\n        "last_ame": "Weaver",\n        "avatar": "https://reqres.i/img/faces/2-image.jpg"\n    },\n    "support": {\n        "url": "https://reqres.i/#support-headig",\n        "text": "To keep ReqRes free, cotributios towards server costs are appreciated!"\n    }\n}'
my_string = my_string.replace("\n", "").replace("    ", "")
print(f'{my_string}')

