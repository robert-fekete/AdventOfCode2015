
import json

def count(text):

    total = 0
    for m in re.finditer(pattern, text, re.DOTALL):
        total += int(m.group(0))

    return total

def calc_red(text):

    root = json.loads(text)
    return travers(root)
   
def travers(object):
    
    total = 0
    if type(object).__name__ == "list":
        for i in object:
            total += travers(i)
    elif type(object).__name__ == "dict":

        if "red" in object.values():
            return 0
        else:
            for k,v in object.iteritems():
                total += travers(v)
    elif type(object).__name__ == "int":
        total += object

    return total
    


pattern = "-?\d+"
red_pattern = "^{[^{]*?[:]\s*[\"]red[\"].*?}$"
print calc_red(open('input.txt', 'r').read())
