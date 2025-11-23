import numpy as np
pua=[]
pra=[]
pub=[]
prb=[]

def euclidean(a,b):
    if a>b:
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while r2!=0:
        q=r1//r2
        r=r1%r2
        #print(f"{q} | {r1} | {r2} | {r}")
        r1=r2
        r2=r
    return r1

def mi(a,b):
    if a<=b:
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    if euclidean(a,b)==1:
        t1=0
        t2=1
        while r2!=0:
            q=r1//r2
            r=r1%r2
            t=t1-t2*q
            r1=r2
            r2=r
            t1=t2
            t2=t
    else:
        print("Numbers are not coprime")
        exit()
    mi=t1
    if mi<=0:
        mi+=b
    return mi

def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0:
        return False
    
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True

def choose_e(phi):
        for i in range(3,phi,2): #start from 3, only odd nos for strong and nonproblematic enc
            if euclidean(i,phi)==1:
                return i

def rsa(pu,pr):
    p=int(input("Enter first prime number:"))
    if not is_prime(p):
        print("p is not a prime number.\n")
        return
    q=int(input("Enter second prime number:"))
    if not is_prime(q):
        print("q is not a prime number.\n")
        return
    n=p*q
    phi=(p-1)*(q-1)
            
    e=choose_e(phi)
    print("e:",e)
    d=mi(e,phi)
    pu.clear()
    pu.extend([e,n])
    print("Public key:",pu)
    pr.clear()
    pr.extend([d,n])
    print("Private key:",pr)
    # or:
    # ch=input("Enter a single character")
    # M=ord(ch)
    
def encrypt(M,pu):
    return pow(M,pu[0],pu[1])

def decrypt(C,pr):
    return pow(C,pr[0],pr[1])

def main():
    print("Sender's keys:\n")
    rsa(pua,pra)
    print("Receiver's keys:\n")
    rsa(pub,prb)
    M=int(input("Enter integer plaintext:"))
    ds=encrypt(M,pra)
    print("Digital signature of Alice for M:",ds)
    ct=encrypt(ds,pub)
    print("Ciphertext on encryption:",ct)
    signed_msg=decrypt(ct,prb)
    print("Decrypted text:",signed_msg)
    ds_recd=decrypt(signed_msg,pua)
    print("Digital signature received:",ds_recd)

    if ds_recd==M:
        print("Signatue valid")
    else:
        print("Signature invalid")


main()

