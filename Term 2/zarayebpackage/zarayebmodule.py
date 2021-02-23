def zaraib(input_numper):
    n = input_numper
    file = open(f'multiples{n}.txt', 'w')
    file.write(f'multiples numbers of {n}\n')
    while n < 1000:
        file.write(f'{n}\n')
        n += input_numper
file.close()
