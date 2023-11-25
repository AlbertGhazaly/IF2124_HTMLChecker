def readHtml(filename):
    f = open(filename,"r")
    lines = ("".join(f.readlines()).replace("\n",'$')).replace(" ",'%')
    f.close
    return lines

def main():
    html = readHtml("html/input.html")
    print(html)

if __name__=="__main__":
    main()