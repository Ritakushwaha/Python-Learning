python get-pip.py

pip --version

pip install PyYAML

python --version

import yaml
dic = {
  'a': {'region': 'b', 'name': 'c'},
  'd': {'region': 'e', 'name': 'f'},
  'g': {'region': 'h', 'name': 'i'},
  'j': {'region': 'k', 'name': 'l'},
  'm': {'region': 'n', 'name': 'o'},
}
result = yaml.dump(dic)
print(result)
