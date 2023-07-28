for i in range(21,31):
    table2 = ''
    for j in range(1,11):
        table2 += f"{i} X {j} = {i*j}\n"
    with open(f'table2 {i}.txt','w') as f:
        f.write(table2)