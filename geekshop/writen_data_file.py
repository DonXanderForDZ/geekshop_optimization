import json

data = [
{'name':'Стул повышенного качества', 'description': 'Не оторваться. ', 'image': '/img/product-11.jpg'},
{'name':'Стул повышенного качества', 'description': 'Не оторваться. ', 'image': '/img/product-21.jpg'},
{'name':'Стул повышенного качества', 'description': 'Не оторваться. ', 'image': '/img/product-31.jpg'},
]


with open("data.txt", "w") as write_file:
    json.dump(data, write_file)
