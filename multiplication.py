def binaryTo2sComp(inp):
    binStr = inp
    if (binStr[0] == '1' or binStr[0] == '0'):
        origLength = len(binStr)
        ref = (10**len(binStr)-1)//9
        binary = ref - int(binStr)
        binary = '0'*(origLength - len(str(binary))) + str(binary)
        bianryString = list(str(binary))
        for i in range(len(bianryString)-1, -1, -1):
            if (bianryString[i] == '0'):
                bianryString[i] = '1'
                break
            else:
                bianryString[i] = '0'
        return ''.join(bianryString)
    return binStr


def complementConverter2s(num, dig):
    absNum = abs(num)
    binary = 0
    n = 1
    count = 0
    while(absNum > 0):
        binary = n*(absNum%2) + binary
        absNum = absNum // 2
        n *= 10
        count += 1
    if (num < 0):
        ref = (10**dig-1)//9
        binary = ref - binary
        binStr = '0'*(dig - len(str(binary))) + str(binary)
        bianryString = list(binStr)
        for i in range(len(bianryString)-1, -1, -1):
            if (bianryString[i] == '0'):
                bianryString[i] = '1'
                break
            else:
                bianryString[i] = '0'
        return ''.join(bianryString)
    return '0'*(dig-len(str(binary))) + str(binary)

def arthmeticRightShift(inp):
    arthStr=inp
    for i in range(len(inp)):
        if(i==0 or i==1):
            arthStr=arthStr[:i]+inp[0]+arthStr[i+1:]
        else:   
            arthStr=arthStr[:i]+inp[i-1]+arthStr[i+1:]
    return arthStr

def binToInt(num):
    return int(str(num), 2)

def binary(number):
    if number < 0:
        binstr= bin(number)[3:]
        binstr='1'+binstr
        return binstr
    return '0'+bin(number)[2:]

def add_binary_nums(x, y): 
        max_len = max(len(x), len(y))
        if(len(x)<len(y)):
            for i in range(len(y)-len(x)):
                x='0'+x
        if(len(x)>len(y)):
            for i in range(len(x)-len(y)):
                y='0'+y
        result = '' 
        carry = 0
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1 
        if carry !=0 : result = '1' + result 
        if(len(result)<max_len):
                for i in range(max_len-len(result)):
                    result='0'+result
        if(len(result)>max_len):
            for i in range(len(result)-max_len):
                result=result[1:]
        return result

def main():
    print("Enter Numbers to Multiply:")
    m1=int(input())
    q1=int(input())
    m=binary(m1)
    q=binary(q1)
    l=max(len(m), len(q))
    n=l
    a=bin(0)[2:]
    a=a.zfill(l)
    if(len(q)<len(m)):
        for i in range(len(m)-len(q)):
            q='0'+q
    if(len(q)>len(m)):
        for i in range(len(q)-len(m)):
            m='0'+m
    q0='0'
    while (l!=0):
        print(a+" "+q+" "+q0)
        if(q0=='0' and q[-1]=='0'):
            ansStr=a+q+q0
            print("Entering 00")
            ansu=arthmeticRightShift(ansStr)
        elif(q0=='1' and q[-1]=='1'):
            ansStr=a+q+q0
            print("Entering 11")
            ansu=arthmeticRightShift(ansStr)
        elif(q0=='0' and q[-1]=='1'):
            print("Entering 10")
            m2=complementConverter2s(m1, n)
            m2=binaryTo2sComp(m2)
            print("adding "+m2)
            a=add_binary_nums(a, m2)
            print("adding ans is "+a)
            ansStr=a+q+q0
            ansu=arthmeticRightShift(ansStr)
        else:
            print("Entering 01")
            m2=complementConverter2s(m1, n)
            print("adding "+m2)
            a=add_binary_nums(a, m2)
            ansStr=a+q+q0
            print("adding ans is "+a)
            ansu=arthmeticRightShift(ansStr)
        print("ansu "+ansu)
        l-=1
        q0=ansu[-1]
        q=ansu[n:n+n]
        a=ansu[0:0+n]
    minus=False
    answer=a+q
    print(answer)
    if(answer[0]=='1'):
        minus=True
    answer=binaryTo2sComp(answer)
    ans=binToInt(answer)
    if(minus==True):
        ans=-abs(ans)
    print(ans)

if __name__=="__main__":
    main()
    # x=7
    # x=complementConverter2s(x, 4)
    # print(binaryTo2sComp(x))
    # x=binaryTo2sComp(x)
    # print(x)
