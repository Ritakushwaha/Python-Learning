import yaml

def get_snowflake_creds(val):
    stream = open("snowflake_creds.yaml", 'r')
    
    dictionary = yaml.safe_load(stream)
    for key, value in dictionary.items():
        for key,value in value.items():
            if key == val:
                return value