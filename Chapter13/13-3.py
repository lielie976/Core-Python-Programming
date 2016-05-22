
class MoneyFmt(object):

    def __init__(self, amount, normal=True):
        if isinstance(amount, float):
            self.amount = amount
            self.value = ""
            self.normal = normal
        else:
            raise TypeError("Input a float")

    def update(self):
        self.dollarize()

    def dollarize(self):
        val = str(self.amount)
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
            if self.normal:
                myDoller = "-" + myDoller
            else:
                myDoller = "<->" + myDoller
        self.value = myDoller

    def __nonzero__(self):
        strTemp = self.value.split(".")
        if strTemp in ("0", "-0"):
            return False
        else:
            return True

    def __repr__(self):
        return str(self.amount)

    def __str__(self):
        return self.value

