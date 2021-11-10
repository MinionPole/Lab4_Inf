import yaml
import json
with open("data2.txt", 'r', encoding='utf-8') as yaml_in, open("JJJ.json", "w", encoding='utf-8') as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out)
