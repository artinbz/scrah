def register(name, last, birth, code):
    file = open('name.txt', 'a')
    file.write(f"{name}.{last}.{birth}.{code}\n")
    file.close()
    