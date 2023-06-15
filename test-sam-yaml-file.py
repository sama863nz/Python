import yaml
with open('sam-yaml-file.yaml','r') as file:
    print(yaml.safe_load(file))
    