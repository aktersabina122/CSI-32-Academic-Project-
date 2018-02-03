# Sabina Akter
# CSI 32 Project # 2
# BinInteger with signed integers

from copy import copy

class BinInteger(object):
                        
    def __init__(self, integer):                        # takes in an integer between -128 and 127.
                                                        # raises an error if  is out of range
        if integer > 127:   
            raise ValueError('Integer must me less than 127')
        elif integer < -128:
            raise ValueError('Integer must be greater than -128')
        else:
            self.binary = makeBinary(integer)


    def decimal(self):
        if self.binary[7] == 1:
            inverse = self.__neg__()
            num = makeDecimal(inverse)
            return -num
        else:        
            return makeDecimal(self.binary)
       
    def __neg__(self):                                  # returns opposite signed bitstring.
        onesComp = onesComplement(self.binary)
        twosComp = addBinary(onesComp, makeBinary(1))
        return twosComp

    def __str__(self):                                  # returns the bit string of the integer
        return str(self.binary)
    
    
    def __add__(self, other):
        return addBinary(self.binary, other.binary)


    def __sub__(self, other):                           # add first integer to the opposite of the other integer
        oppositeBin = other.__neg__()
        return addBinary(self.binary, oppositeBin)
    

def addBinary(bitList1, bitList2):
    newList = [0]*8
    carry = 0
    for i in range(8):
        newList[i], carry = (bitList1[i]+bitList2[i]+carry)%2, (bitList1[i]+bitList2[i]+carry)//2
    if (newList[7] == 0 and bitList1[7] == 1 and bitList2[7] == 1):
        raise ValueError("addition overflow")
    if (newList[7] == 1 and bitList1[7] == 0 and bitList2[7] == 0):
        raise ValueError("addition overflow")
    return newList

def onesComplement(bitList):
    newList = [0]*8
    for i in range(8):
        newList[i] = 1 - bitList[i]
    return newList    

def makeBinary(n):
    newList = [0]*8
    q = n
    for i in range(8):
        # assign quotient and remainder to be  new q and r
        q, r = q//2, q%2 
        newList[i] = r
    return newList   

def makeDecimal(b):
    retval = 0
    for i in range(8):
        d = b[i]
        retval = retval + d * 2**i
    return retval
    
if __name__ == "__main__":
    while True:
        try:
            n1 = eval(input("Enter first integer: "))
            b1 = BinInteger(n1)
            print("The opposite of ",str(b1), " is ", str(-b1));
            n2 = eval(input("Enter second integer: "))
            b2 = BinInteger(n2)
            print("The opposite of ",str(b2), " is ", str(-b2));
            bsum = b1+b2
            bdiff = b1-b2
            print("The sum of ", b1, " and ", b2, " is ", bsum)
            print("The sum of ", b1.decimal(), " and ", b2.decimal(), " is ", b1.decimal()+ b2.decimal())
            print("The difference of ", b1, " and ", b2, " is ", bdiff)
            print("The difference of ", b1.decimal(), " and ", b2.decimal(), " is ", b1.decimal() - b2.decimal())
        except ValueError as d:
            print(d)
           
    


    
        






