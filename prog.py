dados = []
dados = input().split(" ")
cod = int(dados[0])
q = float(dados[1])
if cod == 1:
    val = float(4.000)
    print("Total: R$","%.2f" % (q*val))
elif cod == 2:
    val = float(4.500)
    print("Total: R$","%.2f" % (q*val))
elif int(cod) == 3:
    val = float(5.000)
    print("Total: R$", "%.2f"% (q*val))
elif int(cod) == 4:
    val = float(2.000)
    print("Total: R$","%.2f" % (q*val))
elif int(cod) == 5:
    val = float(1.500)
    print("Total: R$","%.2f" % (q*val))
