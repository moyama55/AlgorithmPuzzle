op = ["*", ""]
val = []

for num in range(1000, 9999):
    check = str(num)
    for i in range(len(op)):
        for j in range(len(op)):
            for k in range(len(op)):
                val = check[3] + op[i] + check[2] + op[j] + check[1] + op[k] + check[0]
            if len(val) > 4:
                if i == eval(val):
                    print(val)

##動かないけど理論的にはあってるはず
