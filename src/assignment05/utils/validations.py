from cerberus import Validator

def is_full_name(input):
    schema = {'input': {'type' : 'string', 'empty': False, 'regex' : r'[a-zA-Z \.]+'}}
    v = Validator(schema)
    document = {'input' : input}
    try:
        assert v.validate(document)
    except AssertionError:
        return False
    else: 
        return True    
    
def is_money(input):
    schema = {'input': {'type' : 'float', 'empty': False, 'min' : 0.01}}
    v = Validator(schema)
    document = {'input' : input}
    try:
        assert v.validate(document)
    except AssertionError:
        return False
    else: 
        if round(input, 2) == input:
            return True
        else:
            return False
