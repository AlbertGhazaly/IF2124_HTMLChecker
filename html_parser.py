import sys, os

tokens = ["<",">","/","=",
        "html","/html",
        "head","/head",
        "body","/body",
        "title","/title",
        "link","/link",
        "rel",
        "href",
        "script","/script",
        "src",
        "h1","/h1",
        "h2","/h2",
        "h3","/h3",
        "h4","/h4",
        "h5","/h5",
        "h6","h6",
        "p","/p",
        "br",
        "em","/em",
        "b","/b",
        "abbr","/abbr",
        "strong","/strong",
        "small","/small",
        "hr",
        "div","/div",
        "a","/a",
        "img","/img",
        "button","/button",
        "alt",
        "button","/button",
        "type",
        "form","/form",
        "action",
        "method",
        "input", "/input",
        "table","/table",
        "tr","/tr",
        "td","/td",
        "th","/th"]

token_dalam = ['rel', 'href', 'src', 'alt', 'type', 'action', 'method', 'class', '"', '=']

def html_to_string(filedir):
    with open(f"{filedir}", "r", encoding="utf-8") as file:

        content = file.readlines()
        content = [(line.rstrip('\n').lstrip()) for line in content]
        content = [element for element in content if element != " "]

        string = ""
        for row in content:
            for char in row:
                string += char.lower()

        return string

def tokenize_1_html(string):
    tokenized_1 = []
    cs = ""

    i = 0
    len_str = len(string)

    isTag = False

    while i < len_str:

        cc = string[i]

        if not(isTag) and cc == "<":
            tokenized_1.append(cs)
            cs = cc
            isTag = True
    
        elif isTag and cc == "<":
            tokenized_1.append(cs)
            cs = cc

        elif isTag and cc == ">":
            cs += cc
            tokenized_1.append(cs)
            isTag = False
            cs = ""

        elif isTag and cc != ">":
            cs += cc

        elif isTag:
            cs += cc
            tokenized_1.append(cs)
            cs = ""

        else:
            cs += cc

        i += 1

    return tokenized_1

def tokenize_2_html(list):

    tokenized_2 = []

    for element in list:
        if len(element) > 0 and element[0] == "<" and element[-1] == ">":
            tokenized_2.append("<")
            string = element[1:-1]
            tokenized_2.append(string)
            tokenized_2.append(">")


        else:
            for char in element:
                tokenized_2.append(char)

    return tokenized_2

def tokenize_3_html(list):
    tokenize_3 = []
    i = 0
    dalam = []
    isi = []
    count = 1
    isIsi = False

    while (i < len(list)) and (list[i] != ' '):
        dalam.append(list[i])
        i += 1
    dalam = ''.join(dalam)
    tokenize_3.append(dalam)
    dalam = []
    
    if (i < len(list)):
        while (i < len(list)):
            if (list[i]) in (token_dalam):
                if (len(dalam) > 0):
                    dalam = ''.join(dalam)
                    dalam = dalam.replace(" ", "")
                    tokenize_3.append(dalam)
                    dalam = []
                if (len(isi) > 0):
                    isi = ''.join(isi)
                    tokenize_3.append(isi)
                    isi = []
                if (list[i] == '"') and (count == 1):
                    isIsi = True
                    count = 2
                elif (list[i] == '"') and (count == 2):
                    isIsi = False
                    count = 1
                tokenize_3.append(list[i])
                i += 1
            else:
                if (isIsi):
                    isi.append(list[i])
                else:
                    dalam.append(list[i])
                i += 1
        if (len(dalam) > 0):
            dalam = ''.join(dalam)
            dalam = dalam.replace(" ", "")
            tokenize_3.append(dalam)
        if (len(isi) > 0):
            isi = ''.join(isi)
            tokenize_3.append(isi)
    
    return tokenize_3
         
html_path = "cek.html"
string = html_to_string(html_path)
print('awal:')
print(string)

string = tokenize_1_html(string)
# print('pertama')
# print(string)

string = tokenize_2_html(string)
# print('kedua')
# print(string)

i = 0
lenStr = len(string)

while (i < lenStr):
    if (string[i-1] == '<'):
        contents = tokenize_3_html(string[i])
        if (len(contents) == 1):
            string[i] = contents[0]
        else:
            for j in range (len(contents)):
                string.insert(i, contents[j])
                i += 1
            string.pop(i)
    i += 1
print('tokenize:')
print(string)

# string = 'body style="    wiadiuwa" id="id_1"'
# li = tokenize_3_html(string)
# print(li)