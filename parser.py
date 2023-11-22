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

token_dalam = ['rel', 'href', 'src', 'alt', 'type', 'action', 'method', 'class']

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
    awal = []
    dalam = []
    isi = []
    cek = True

    while (list[i] != ' '):
        awal.append(list[i])
        i += 1;
    awal = ''.join(awal)
    tokenize_3.append(awal)
    i += 1;
    
    while (list[i] != '='):
        dalam.append(list[i])
        i += 1;
    dalam = ''.join(dalam)
    
    if dalam in token_dalam:
        print('masuk')
        tokenize_3.append(dalam)
        tokenize_3.append(list[i])
        i += 1
        tokenize_3.append(list[i])
        i += 1
        while (list[i] != '"'):
            isi.append(list[i])
            i += 1
        isi = ''.join(isi)
        tokenize_3.append(isi)
        tokenize_3.append(list[i])
    
    return tokenize_3



         

# html_path = "cek.html"
# string = html_to_string(html_path)
# print(string)

# string = tokenize_1_html(string)
# print(string)

# string = tokenize_2_html(string)
# print(string)

string = 'body class="waudiuwadbwa"'
li = tokenize_3_html(string)
print(li)