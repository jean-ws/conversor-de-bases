def read_base(value_and_base):
    base = ""
    
    if value_and_base.rfind("2") == len(value_and_base)-2:
        base = 2
    elif value_and_base.rfind("8") == len(value_and_base)-2:
        base = 8
    elif value_and_base.rfind("10") == len(value_and_base)-3:
        base = 10
    elif value_and_base.rfind("16") == len(value_and_base)-3:
        base = 16
    return base

def read_value(value_and_base):

    if value_and_base.rfind("2") == len(value_and_base)-2:
        value = value_and_base[:-2]
    elif value_and_base.rfind("8") == len(value_and_base)-2:
        value = value_and_base[:-2]
    elif value_and_base.rfind("10") == len(value_and_base)-3:
        value = value_and_base[:-3]
    elif value_and_base.rfind("16") == len(value_and_base)-3:
        value = value_and_base[:-3]
    return value

def read_lines(txt_name):
    with open(txt_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines
