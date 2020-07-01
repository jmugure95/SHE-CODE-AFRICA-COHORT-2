x = int(input("Enter a positive integer:"))

def fibbonacci_series(x):
    m = 0
    n = 1

    if x < 0:
        print("Invalid, Try a positive integer")
    
    elif x == 1:
        print("Fibbonacci sequence of %d:" %(x))
        print(m)

    else:
        print("Fibbonacci sequence of %d:" %(x))
        print(m)
        print(n)
        
        for i in range(2,x):
            p = m + n
            m, n=n,m+n
            print(p)
            
fibbonacci_series(x)



