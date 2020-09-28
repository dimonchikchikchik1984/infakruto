from sys import argv
from sys import exit
def fib(n):
    f=[0]*n
    f[0]=f[1]=1
    for i in range (2,n):
        f[i]=f[i-1]+f[i-2]
    return f[n-1]
if __name__=="__main__":
        if len(argv)==3:
            if argv[1]=='-n':
                print(str(fib(int(argv[2]))))
            else:
                print('Invalid argument')
                exit(1)
        else:
            if len(argv)==2:
                print(str(fib(int(argv[1]))))
            else:
                print('Incorrect number of arguments')
                exit(1)
