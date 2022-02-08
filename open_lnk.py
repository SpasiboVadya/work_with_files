import webbrowser


b = open('1.txt').readlines()
for i in b:
    webbrowser.open(i)

