import yaml

# dump   把Python数据对象转换为yaml类型 与load相反
String = ['welcome', 'to', 'yaml']
website = {'url': 'www.google.com'}

print(String)
print(website)

print(yaml.dump(String))
print(yaml.dump(website))
