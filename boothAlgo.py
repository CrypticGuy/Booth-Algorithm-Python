#q = int(input())
#m = int(input())

def binToInt(num):
    return int(str(num), 2)

def binLength(num):
    count = 0
    while(num > 0):
        num /= 2
        count += 1
    return count    

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

def addToBinArrays(a, b):
    #print(a, b)
    a = a[::-1]
    b = b[::-1]
    #print(a, b)
    c = '0'
    for i in range(len(a)):
        if (a[i] == '1' and b[i] == '1'):
            b[i] = c
            c = '1'
        elif (a[i] == '1' or b[i] == '1'):
            if (c == '1'):
                b[i] = '0'
                c = '1'
            else:
                b[i] = '1'
                c = '0'
        else:
            b[i] = c
            c = '0'
    return b[::-1]

def addTwoBinary(a, b):
    # Answer is given by a / b
    L = max(binLength(a), binLength(b)) + 2 # This will reflect in the final value that we will need
    print(L + 2)
    A = list('0' * L)
    Q = list(complementConverter2s(a, L))
    M = list(complementConverter2s(b, L))
    #print(A, Q, M)
    #print(binaryTo2sComp(''.join(M)))
    for i in range(L):
        leftA = A[0]
        A = A[1::]
        A.append(Q[0])
        Q = Q[1::]
        #print(A, Q, M)
        if (leftA == '1'): # A is positive
            A = addToBinArrays(A, M)
        else:
            A = addToBinArrays(A, list(binaryTo2sComp(''.join(M))))
        if (A[0] == '0'):
            Q.append('1')
        else:
            Q.append('0')
        #print(A, Q, M)
        #print("")
        #print("")
    if (A[0] == '1'):
        A = addToBinArrays(A, M)
    print(''.join(A), ''.join(Q))
    print(int(''.join(A), 2), int(''.join(Q), 2))
print(addTwoBinary(1000, 80))