
def dollarize(amount):
    val = str(amount)
    isNegtive = False
    if val.startswith("-"):
        isNegtive = True
        val = val[1:]
    Money = val.split(".")
    num = len(Money[0]) / 3
    mod = len(Money[0]) % 3
    if mod == 0:
        num -= 1
    strTemp = []
    for i in range(num):
        strTemp.append(Money[0][-3:])
        Money[0] = Money[0][:-3]
    strTemp.append(Money[0])
    strTemp.reverse()
    myDoller = ','.join(strTemp) + "." + Money[1]
    if isNegtive:
        myDoller = "-" + myDoller
    return myDoller

if __name__ == "__main__":
    doller = dollarize(-11123434.3244)
    print doller
