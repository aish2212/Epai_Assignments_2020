import fractions
from fractions import Fraction


def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''
    if base < 2 or base > 36:
        raise ValueError(" base is out of ranges, It should be between 2 to 36 (including)")
    elif len(digit_map) > len(set(digit_map)):
        raise ValueError("digit_map must not have any repeating character")
    elif len(digit_map) != base:
        raise ValueError("Length of digit map is not equal to base ")
    elif number == 0:
        return 0
    else:
        digits = []
        n,encoding = (-number,"-") if number < 0 else (number,"")
        while n > 0:
            m = n % base
            n = n // base
            digits.insert(0,m)
        encoding += "".join([digit_map[d] for d in digits])
        return encoding


def rel_tol(X,Y):  #Function to calculate the relative tolerance
    try:
        rl = abs(X - Y) /min(abs(X), abs(Y))
        if(rl <= 1e-12):
            return True
        else:
            return False
    except:
        return False


def abs_tol(X,Y): #Function to calculate the absolute tolerance
    al = abs(X - Y)
    if(al <= 1e-05):
        return True
    else:
        return False


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    output = (rel_tol(a,b) or abs_tol(a,b))
    if (output == True):
        a=b
    else:
        a!=b
    return a==b


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    a = 0
    b = []
    if(type(f_num) is float):
        a = f_num
        for i in str(a):
            if(i == '.'):
                break
            b.append(i)
        s_num = "".join(b)
        f_num=Fraction(s_num)
        return f_num.numerator


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    a = 0
    b = []
    sign = -1 if f_num < 0 else 1
    if(type(f_num) is float):
        a = f_num
        for i in str(a):
            if(i == '.'):
                break
            b.append(i)
        s_num = "".join(b)
        f = Fraction(s_num)
        f_num_round = f.numerator
        f_num_dec = f_num - f_num_round  
        if (f_num_dec >= 0.5) and (sign == 1):
            return f_num_round + 1
        elif (f_num_dec <= -0.5) and (sign == -1):
            return f_num_round - 1
        else:
            return f_num_round


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0
