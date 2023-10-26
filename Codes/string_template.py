from string import Template

template = Template("Hello, ${name}. Your age is ${age}.")

data = {"name": "Rita", "age": 26}
result = template.substitute(data)
print(result)

template = Template("Hello, ${name}. Your age is ${age}. Your city is ${city}.")
data = {"name": "Rita", "age": 26}
result = template.safe_substitute(data)
print(result)