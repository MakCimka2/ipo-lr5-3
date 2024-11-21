with open("text.txt" , "r", encoding="utf-8") as file: #Открываем файл
    d = file.read() #Читаем файл
    c = d.split()
    print(len(c))# Выводим кол-во слов
