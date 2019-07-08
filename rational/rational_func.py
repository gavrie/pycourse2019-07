def rational(n, d):
    return n, d

def numer(x): return x[0]

def denom(x): return x[1]

def rational_add(x, y):
    return rational(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))

def rational_str(x):
    return "{}/{}".format(numer(x), denom(x))

