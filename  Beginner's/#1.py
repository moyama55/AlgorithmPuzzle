#11以上の奇数で回文数になるモノを探す
n = 11

print(str(oct(n)).strip("aa"))

while True:
    if str(n) == str(n)[::-1] and str(bin(n)).strip("0b") == str(bin(n)).strip("0b")[::-1] and str(oct(n)).strip("0o") == str(oct(n)).strip("0o")[::-1]:
        print(n)
        break
    n += 2