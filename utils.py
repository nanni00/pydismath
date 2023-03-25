import math


def sign(x):
   return -1 if x < 0 else 1


def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
      if (n%i) == 0:
        return False
    return True


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


def diofantine_equation(a: int, b: int, c: int):
    g, x, y = my_gcd(a, b)

    if c % g != 0: return None, None, None, None

    x, y = x * (c / g), y *(c / g)

    return map(int, [x, -b/g * sign(a), y * sign(b), a/g])


def linear_congruence(a, b, n):
   g, x, _ = my_gcd(a, n)

   if b % g != 0: return None, None

   x, xk, _, _ = diofantine_equation(a, n, b)

   z_sol = (x, xk)

   zn_sol = [x + int((n * k) / g) for k in range(g)]

   return z_sol, zn_sol