def log (n):
    if n==1:
        return 0
    else:
        return 1+log(n/2)