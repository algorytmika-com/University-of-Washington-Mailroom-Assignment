import json, sys

def read_from_json(path):
    content = ""
    try:
        with open(path) as file:
            content = json.load(file)
    except FileNotFoundError:
        print(f"Couldn't find {path}")
    finally:
        return content  
    
def write_to_json(content, path):
    try:    
        with open(path, 'w') as file:
            return json.dump(content, file)
    except FileNotFoundError:
        print(f"Couldn't find {path}")
  