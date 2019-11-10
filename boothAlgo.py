#q = int(input())
#m = int(input())

def binToInt(num):
    return int(str(num), 2)

def binLength(num):
    temp = num
    num = abs(num)
    count = 0
    while(num > 0):
        num //= 2
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

def divTwoBinary(a, b):
    # Answer is given by a / b
    L = max(binLength(a), binLength(b)) + 2 # This will reflect in the final value that we will need
    #print(L + 2)
    A = list('0' * L)
    Q = list(complementConverter2s(abs(a), L))
    M = list(complementConverter2s(abs(b), L))
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
    strQ = ''.join(Q)
    strA = ''.join(A)
    intA = int(''.join(A), 2)
    intQ = int(''.join(Q), 2)
    if (a < 0 and b < 0):
        A = binaryTo2sComp(strA)
        intA = -1*intA
    elif(a < 0 or b < 0):
        Q = binaryTo2sComp(strQ)
        A = binaryTo2sComp(strA)
        intQ = -1*intQ
        intA = -1*intA
    #print(A, Q, M)
    print("Quotient: " + ''.join(Q), "Remainder: " + ''.join(A))
    print("Quotient: " + str(intQ), "Remainder: " + str(intA))
    with open("output.txt", 'a',encoding = 'utf-8') as f:
        f.write("\nQuotient is:\n" + "binary: " + str(''.join(Q)) + "\nint: " + str(intQ))
        f.write("\nRemainder is:\n" + "binary: " + str(''.join(A)) + "\nint: " + str(intA))

def mulTwoBinary(a, b):
    L = max(binLength(a), binLength(b)) + 1
    #print(L)
    A = list('0'*(L))
    Q = list(complementConverter2s(a, L))
    M = list(complementConverter2s(b, L))
    Mc = list(binaryTo2sComp(''.join(M)))
    #print(A, Q,M, Mc)
    Q0 = '0'
    for i in range(L):
        #print(''.join(A), ''.join(Q), Q0)

        #print(Q[-1] + Q0)
        if (Q[-1] + Q0 == '01'):
            A = addToBinArrays(A, M)
            #print(''.join(A), ''.join(Q), Q0)
        elif (Q[-1] + Q0 == '10'):
            A = addToBinArrays(A, Mc)
            #print(''.join(A), ''.join(Q), Q0)
        tempA = A[0]
        Q0 = Q[-1]
        Q = Q[:-1]
        Q.insert(0, A[-1])
        A = A[:-1]
        A.insert(0, A[0])
        #print(''.join(A), ''.join(Q), Q0)
        #print()
        #print(''.join(A), ''.join(Q), Q0)
    ans = ''.join(A + Q)
    intAns = int(ans, 2)
    with open("output.txt", 'w',encoding = 'utf-8') as f:
        f.write("Product is:\n" + "binary: " + str(ans) + "\nint: " + str(intAns))

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
mulTwoBinary(a, b)
divTwoBinary(a, b)