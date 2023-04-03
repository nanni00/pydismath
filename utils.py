from math import sqrt, floor, gcd, lcm
from collections import defaultdict


def sign(x): return -1 if x < 0 else 1


def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
      if (n%i) == 0:
        return False
    return True


def my_lcm(a, b): return lcm(a, b)


def my_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = abs(b); old_r = abs(a)

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]


def fermat_factorization(n):
    factors = defaultdict(int)
    q = [n]
    
    while q:
        n = q.pop()
        if n % 2 == 0: 
            n /= 2
            q.append(n)
            factors[2] += 1
        elif sqrt(n) == floor(sqrt(n)):
            q.append(sqrt(n))
            q.append(sqrt(n))
        else:
            x = floor(sqrt(n)) + 1
            while (s := sqrt(pow(x, 2) - n)) != floor(s)  and x != (n + 1) / 2:
                x += 1
            
            v1, v2 = x + s, x - s
            if is_prime(v1): factors[v1] += 1  
            else: q.append(v1) 
            
            if is_prime(v2): factors[v2] += 1  
            else: q.append(v2)
    return factors


def diofantine_equation(a: int, b: int, c: int):
    g, x, y = my_gcd(a, b, True)

    if c % g != 0: return None, None, None, None

    x, y = x * (c / g), y *(c / g)

    return map(int, [x, -b/g * sign(a), y * sign(b), a/g])


def linear_congruence(a, b, n):
    ''' Solves the linear congruence ax congr b mod n. 
    If it hasn't solutions return an error string, otherwise a tuple with solutions in Z and in Zn. '''
    g, x, _ = my_gcd(a, n, True)
    if b % g != 0: return 'The linear congruence has no solution.'

    x, xk, _, _ = diofantine_equation(a, n, b)
    z_sol = (x, xk)
    zn_sol = [x + int((n * k) / g) for k in range(g)]
    return z_sol, zn_sol


def euler_function(n):
    if n <= 0:
        return 'Input value n must be a natural number.'
    else:
        factors = fermat_factorization(n)
        if 1 in factors.keys(): factors.pop(1)
        ef = 1

        for f, e in factors.items():
            ef *= int(pow(f, e) - pow(f, e - 1)) 
        return ef


def find_modulus(a, m, n): 
    #if gcd(a, n) != 1: return f'Values {a} and {n} are not coprime.'
    return pow(a, m) % n


def two_congruence_system(a1, n1, a2, n2):
    """ Returns the solution of the system as a tuple (x, mod) """
    g, x, y = my_gcd(n1, n2)
    diff = a1 - a2
    if diff % g != 0:
        return 'The system has no solution.'
    
    x, y = x * int(diff / g), y * int(diff / g)

    if a1 - n1 * x == a2 + n2 * y:
        return find_modulus(a1 - n1 * x, 1, lcm(n1, n2)), lcm(n1, n2)

