def fc(f):
    return (f-32)/(9/5)
def cf(c):
    return c*(9/5)*32
def ck(c):
    return c+273.15
def kc(k):
    return k-273.15
def fk(f):
    return (f-32)*5/9 + 273.15
def kf(k):
    return k * 1.8 - 459.7

if __name__=="__main__":
    print("82F = " + str(ck(kc(fk(82)))) + "K")
