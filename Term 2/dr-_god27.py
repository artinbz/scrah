def get_info():
    txt = input('enter your information:(name family age\n')
    return txt .split()


info = get_info()

template = f"""
name : {info[0].title()}
last : {info[1].upper()}
age :{info[2]}
**************************"""
file = open('names.txt', 'a')
file. write(template)
file. close()
