def split(l, c=0):
    """Split the given list in two."""
    return (l[: int(len(l)/2)], l[int(len(l)/2) : None if c == 0 else c])

def main():
    print("This program excecutes (Non-)restoring division algorithm.\n")
    print("The formula it's going to calculate is:  X / Y = ?")
    print("Choose which algorithm (R)estoring or (N)on-restoring [r/n]: ", end="")
    while True:
        inp = str(input())[0]
        if   inp in ["n", "N"]:
            algorithm = "n"
            break
        elif inp in ["r", "R"]:
            algorithm = "r"
            break
        else:
            print("Input R or N. ", end="")
    algorithm = inp

    print("Input the bit length of SECOND variable Y: ", end="")
    ylen = int(input())
    xlen = ylen * 2
    print("(The bit length of X is: len(Y)*2 = %d)" % xlen)

    print("Input the number of first variable X: ", end="")
    x = int(input())
    if x < 0:
        x = TwoComp( ("{0:0%db}" % xlen).format(x) )    #Calculate the two's complement number of x
    else:
        x = ("{0:0%db}" % xlen).format(x)   #Convert to bits and assign directly

    print("Input the number of second variable Y: ", end="")
    y = int(input())
    if y < 0:
        y = TwoComp( ("{0:0%db}" % ylen).format(y) )
    else:
        y = ("{0:0%db}" % ylen).format(y)

    n = ylen
    c = ""

    #----- Prepare internal variables -----#

    print("Internal variables:")
    print("X = %s %s" % (x[:ylen], x[ylen:]))
    print("Y =", y)
    print("n =", n)
    print("")

    #----- Algorithm start -----#

    print("#Algorithm start: %s\n" % ("Restoring" if algorithm == "r" else "Non-restoring"))
    if not "1" in y:
        print("Y is zero. Aborting.")
        return

    print("X1 = X1 - Y\t\t", end="")
    x = BitAdd(x, TwoComp(y) + GenZeroStr(ylen), xlen)
    print("X = %s %s" % split(x))

    if x[0] == "0":
        print("X1 is positive or zero. Aborting.")
        return

    x = BitShift(x, -1)
    print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
    
    print("X1 = X1 + Y\t\t", end="")
    x = BitAdd(x, y + GenZeroStr(ylen), xlen)
    print("X = %s %sC" % split(x, -1))
    print("n = n - 1 = %d" % (n-1))
    n -= 1

def BitAdd(m, n, length):
    """Return m+n in string.
    
    Arguments:
    m -- Binary number in string
    n -- Same as above
    length -- The length of returned number (overflowed bit will be ignored)
    Returns: string
    """

    lmax = max(len(m), len(n))
    c = 0
    ml = [0] * (lmax - len(m)) + [int(x) for x in list(m)]
    nl = [0] * (lmax - len(n)) + [int(x) for x in list(n)]
    rl = []
    for i in range(1, lmax+1):
        if ml[-i] + nl[-i] + c == 0:
            rl.insert(0, 0)
            c = 0
        elif ml[-i] + nl[-i] + c == 1:
            rl.insert(0, 1)
            c = 0
        elif ml[-i] + nl[-i] + c == 2:
            rl.insert(0, 0)
            c = 1
        elif ml[-i] + nl[-i] + c == 3:
            rl.insert(0, 1)
            c = 1
    if c == 1:
        rl.insert(0, 1)
    if length > len(rl):
        rl = [0] * (length - len(rl)) + rl
    else:
        rl = rl[-length:]
    rl = "".join([str(x) for x in rl])
    return rl


def TwoComp(n):
    """Return the two's complement of given number.
    Arguments:
    n -- Binary number in string
    Returns: string
    """

    l = list(n)
    for i in range(len(l)):
        l[i] = "0" if l[i] == "1" else "1"
    return BitAdd("".join(l), "1", len(l))


def BitShift(n, shift):
    """Shift the bits rightward in arithmetical method.
    If shift is negative, it shifts the bits leftward.
    Arguments:
    n -- Binary number in string
    shift -- Number of times to shift
    Returns: string
    """

    if shift > 0:       #Right shift
        if n[0] == "0":
            n_ = "".join(["0"] * shift) + n
        else:
            n_ = "".join(["1"] * shift) + n
        return n_[:len(n)]
    else:
        n_ = n + "".join(["0"] * (-shift))
        return n_[-len(n):]


def CalcBoothRecoding(n):
    """Calculate the Booth recoding number of given n.
    Arguments:
    n -- Binary number to calculate in string
    Returns: string
    Attention:
    "2" in returned string represents "1-hat".
    """

    n_ = [int(x) for x in list(n + "0")]
    r = []
    for i in range(len(n)):
        x = n_[i+1] - n_[i]
        if x == -1: r.append(2)
        else:       r.append(x)
    return "".join([str(x) for x in r])


def GenZeroStr(n):
    """Generate a bunch of zeroes.
    Arguments:
    n -- Number of zeroes
    Returns: string
    """

    return "".join(["0"] * n)

def BoothRecToString(s, indent=0):
    """Convert a Booth recoding number to human-readable string.
    Arguments:
    s -- String of Booth recoding
    indent -- Number of spaces in the head of lines (optional)
    Returns: string
    """

    sp = " " * indent
    h = []
    n = []
    for i in list(s):
        if   i == "0":
            h.append(" ")
            n.append("0")
        elif i == "1":
            h.append(" ")
            n.append("1")
        elif i == "2":
            h.append("^")
            n.append("1")
    return sp + "".join(h) + "\n" + sp + "".join(n)

    #--- Go into the loop --- #

    print("\n#Into the loop...\n")

    if algorithm == "r":
        pass
    elif algorithm == "n":
        for i in range(n):  # X1 != 0
            print("Step %d:" % (i+1))
            if x[0] == "0": # X1 >= 0
                c = "1"
                print("X1 >= 0 -> c = 1", end="")
                x = x[:-1] + c #[X1][X2][C] << 1
                print("\tX = %s %s" % split(x))
                x = BitShift(x, -1) #Shift bits leftward
                print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
                x = BitAdd(x, TwoComp(y) + GenZeroStr(ylen), xlen)    #X1 = X1 - Y
                print("X1 = X1 - Y\t\tX = %s %sC" % split(x, -1))
            else:
                c = "0"
                print("X1 < 0 -> c = 0", end="")
                x = x[:-1] + c
                print("\t\tX = %s %s" % split(x))
                x = BitShift(x, -1)
                print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
                x = BitAdd(x, y + GenZeroStr(ylen), xlen)    #X1 = X1 + Y
                print("X1 = X1 + Y\t\tX = %s %sC" % split(x, -1))

            print("")

        if x[0] == "0": # X1 >= 0
            print("X1 >= 0 -> C = 1")
            c = "1"
            x = x[:-1] + c
        else:
            print("X1 < 0 -> C = 0")
            c = "0"
            x = x[:-1] + c
            x = BitAdd(x, y + GenZeroStr(ylen), xlen)
            print("X1 = X1 + Y")
        print("X = %s %s" % split(x))

    print("")
    print("The answer is: R = %s, Q = %s" % split(x))


if __name__ == "__main__":
    main()