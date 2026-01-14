summa = int(input("Xarid summasini kiriting: "))

if summa < 0:
    print("Noto‘g‘ri summa")

elif summa < 100000:
    print("Chegirma yo‘q")

elif summa < 300000:
    print("5% chegirma")

elif summa < 500000:
    print("10% chegirma")

else:
    print("20% chegirma")
