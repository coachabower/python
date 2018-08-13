import json

def second_print():
    print("In Second")

def fib():
    a = 1
    b = 1

    yield 1
    yield 1
    while True:
        a,b = b,a+b
        yield b

def comprehension(list):
    new_list = []
    new_list = [li for li in list if li >= 0]
    return new_list

def countArgs (a,b,c,*d):
    return len(list(d))

def isMagic (a,b,c,**d):
    if d.get('magicnumber') == 7:
        return True
    else:
        return False

def add_employee(salaries_json,name,salary):
    salaries = json.loads(salaries_json)
    try:
        salaries[name] = salary
    except IndexError:
        salaries.append(name)
        salaries[name] = salary
    return json.dumps(salaries)
