with open("text.txt" , "r", encoding="utf-8") as file:
    d = file.read()
    c = d.split()
    print(len(c))
