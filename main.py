import sys
import os
import parser
from myclass import Stack

# verifikasi jumlah argumen pada pemanggilan main.py
if len(sys.argv) != 3:
    print("Usage: python main.py pda.txt \"inputAcc.html\"")
    sys.exit(1)

# path file pda dan html
pda_path = sys.argv[1]
html_path = sys.argv[2]

# verifikasi format file pda dan html
format_pda = pda_path[-4:]
format_html = html_path[-5:]

if (format_pda != ".txt" or format_html != ".html"):
    print("Usage: python main.py pda.txt \"inputAcc.html\"")
    sys.exit(1)


# program bisa menerima input berupa path file atau hanya nama filenya saja,
# jika hanya nama file maka akan dilakukan pengecekan di folder pda atau folder html
pdaFound = True
htmlFound = True

# ngecek file pda secara global path dan di dalam folder pda
if not(os.path.exists(pda_path)) and not(os.path.exists("pda\\" + pda_path)):
    print(f"File \"{pda_path}\" tidak ditemukan.")
    pdaFound = False
# ngecek apakah pathnya global atau hanya nama file
# jika hanya nama file, path folder pda ditambahkan di depan
elif not(os.path.exists(pda_path)):
    pda_path = "pda\\" + pda_path

# ngecek file html secara global path dan di dalam folder html
if not(os.path.exists(html_path)) and not(os.path.exists("html\\" + html_path)):
    print(f"File \"{html_path}\" tidak ditemukan.")
    htmlFound = False
# ngecek apakah pathnya global atau hanya nama file
# jika hanya nama file, path folder html ditambahkan di depan
elif not(os.path.exists(html_path)):
    html_path = "html\\" + html_path

# exit program jika salah satu atau kedua file tidak ditemukan
if (not(pdaFound and htmlFound)):
    sys.exit(1)
 
# jika semuanya sudah aman baru main program bisa dijalankan
else:

    ### parsing file pda dan html ###
    pda = parser.parseFilePDA(pda_path)
    html = parser.parseFileHTML(html_path)

    # stack direpresentasikan sebagai string biasa yang bottom of stacknya berada pada sebelah kiri
    stack = Stack(pda)

    ### output pda dan string html ###
    print("Push Down Automata: ")
    print(pda)

    print("\nTransitions: ")
    for transition in pda.transitions:
        print(transition)

    ### simulasi pengolahan string HTML ###
    # print("\nString HTML :")
    # print(html)

    # print("\nhtml.read()")
    # cc = html.read()
    # print(f"Current character: {cc}")

    # print("String HTML:")
    # print(html)

    # print("\nhtml.read(\"epsilon\")")
    # cc = html.read("epsilon")
    # print(f"Current character: {cc}")

    # print("String HTML:")
    # print(html)

    ### simulai operasi push dan pop pada stack ###
    # print(f"\nStack: {stack}")
    # print("stack.pop()")
    # stack.pop()

    # print(f"stack.push(YZ)")
    # stack.push(pda.transitions[0].push)

    # print(f"Stack: {stack}")

    # print("stack.pop()")
    # stack.pop()
    # print(f"Stack: {stack}")