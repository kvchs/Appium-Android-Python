import yaml

file = open('family.yaml', 'r')
data = yaml.load(file)
print(data)

print(data['name'])
print(data['age'])

print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'])

print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])

data['name'] = 'new name'
print(data['name'])

print(data['test'])