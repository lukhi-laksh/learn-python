def generetTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
        with open(f"Tables/table_{n}", "w") as f:
            f.write(table)


for i in range(1, 21):
    generetTable(i)
    
        