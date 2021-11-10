import yaml
import json
with open("data2.txt", 'r') as yaml_in, open("JJJ.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out)
