def readHtml(filename):
    f = open(filename,"r")
    lines = ("".join(f.readlines()).replace("\n",'$')).replace(" ",'%')
    f.close
    return lines

def readHtmlList(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:
        content = file.readlines()
        return content

def main():
    html = readHtml("html/input.html")
    print(html)

if __name__=="__main__":
    main()