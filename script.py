"""
d4:dictd3:1234:test3:4565:thinge4:listl11:list-item-111:list-item-2e6:numberi123456e6:string5:valuee

===========================================

d
	4:dict d
				3:123 4:test 
				3:456 5:thing
			e
			
	4:list l 11:list-item-1 11:list-item-2 e
	6:number i123456e 
	6:string 5:value
e

===========================================

{
	{"dict": {
		{"123": "test"},
		{"456": "thing"}
	}},
	
	{"list": ["list-item-1", "list-item-2"]},
	
	{"number": 123456},
	
	{"string": "value"}
}
"""

class Shit:
    def __init__(self, text):
        self.text = text
        self.cursor = 0

# ЧИСЛО = i{number}e
def parseNumber(shit):
    shit.cursor += 1
    text = shit.text
    e_pos = text.find('e', shit.cursor)
    num = int(text[shit.cursor:e_pos])
    shit.cursor = e_pos + 1
    return num

# СТРОКА = {size}:{content}
def parseString(shit):
    text = shit.text
    colon_pos = text.find(':', shit.cursor)
    size = int(text[shit.cursor:colon_pos])
    shit.cursor = colon_pos + 1
    
    item = text[shit.cursor:(shit.cursor+size)]
    shit.cursor += size
    return item;

# СЛОВАРЬ = d{dictionary}e
def parseDictionary(shit):
    fakeList_ = parseList(shit)
    return {fakeList_[i-1]:fakeList_[i] for i in range(1, len(fakeList_), 2)}

# СПИСОК = l{list}e
def parseList(shit):
    shit.cursor += 1
    text = shit.text
    
    list_ = []
    while text[shit.cursor] != 'e':
        if text[shit.cursor] == 'i':
            value = parseNumber(shit)
            list_.append(value)
        if text[shit.cursor].isdigit():
            value = parseString(shit)
            list_.append(value)
        if text[shit.cursor] == 'l':
            value = parseList(shit)
            list_.append(value)
        if text[shit.cursor] == 'd':
            value = parseDictionary(shit)
            list_.append(value)
            
    shit.cursor += 1
    return list_

def parse(shit):
    text = shit.text
    list_ = []
    while (shit.cursor < len(text)):
        if text[shit.cursor] == 'i':
            value = parseNumber(shit)
            list_.append(value)
        if text[shit.cursor].isdigit():
            value = parseString(shit)
            list_.append(value)
        if text[shit.cursor] == 'l':
            value = parseList(shit)
            list_.append(value)
        if text[shit.cursor] == 'd':
            value = parseDictionary(shit)
            list_.append(value)
    
    return list_

s = 'd4:dictd3:1234:test3:4565:thinge4:listl11:list-item-111:list-item-2e6:numberi123456e6:string5:valuee'
shit = Shit(s)
res = parse(shit)
print(s)
print(res)