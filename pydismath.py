import utils


def _get_input(requireds: dict[str: int], info=None):
    inputs = []
    print(info) if info is not None else None
    for k, v in requireds.items():
        try:
            userin = input(f"Insert number {k}: ")
            if v is int: inputs.append(int(userin))
        except ValueError:
            print('Input error, value not acceptable: ' + str(userin))
    return inputs if len(inputs) > 1 else inputs[0]


def _print_header_footer(title, header=True):
    tot_len = 50
    right = left = int((tot_len - len(title)) / 2)
    if header: print('='*left + ' ' + title + ' ' + '='*right)
    
    else: print('='* max(tot_len + 1, right + left + 2 + len(title)))


def dm_greatest_common_divisor():
    """ Greatest Common Divisor """
    _print_header_footer('Greatest Common Divisor')
    a, b = _get_input({'a': int, 'b': int})
    print(f'GCD({a},{b}) = {utils.my_gcd(a, b)[0]}')
    _print_header_footer('Greatest Common Divisor', header=False)


def dm_least_common_multiple():
    """ Least Common Multiple """
    _print_header_footer('Least Common Multiple')
    a, b = _get_input({'a': int, 'b': int})
    print(f'LCM({a}, {b}) = {utils.my_lcm(a, b)}')
    _print_header_footer('Least Common Multiple', header=False)


def dm_is_prime():
    """ Is a prime """
    _print_header_footer('Is Prime')
    n = _get_input({'n': int})
    if utils.is_prime(n): print(f'The number {n} is prime!')
    else: print(f"The number {n} isn't prime.")
    _print_header_footer('Is Prime', header=False)


def dm_fermat_factorization():
    """ Fermat Factorization """
    def _print_factors(factors):
        s = ""
        for f, e in factors.items():
            if f != 1 and e != 1: s += f'{int(f)}^{int(e)}; ' 
            elif e == 1: s += f'{int(f)}; '
        return s[:-2]        

    _print_header_footer('Fermat Factorization')
    n = _get_input({'n': int})
    factors = utils.fermat_factorization(n)
            
    print(f'Factors of {n} are {_print_factors(factors)}')
    _print_header_footer('Fermat Factorization', header=False)


def dm_bezout_identity():
    _print_header_footer("Bezout Identity")
    a, b = _get_input({'a': int, 'b': int})
    _gcd, x, y = utils.my_gcd(a, b, True)
    print(f"MCD({a}, {b}) = {a}*x + {b}*y = {a}*{x} + {b}*{y} = {_gcd}")
    _print_header_footer("Bezout Identity", header=False)


def dm_diophantine_equation():
    _print_header_footer("Diofantine Equation")
    a, b, c = _get_input({'a': int, 'b': int, 'c': int}, "ax + by = c")
    x, xk, y, yk = utils.diofantine_equation(a, b, c)
    if x == None:
        print(f"The equation {a}x + {b}y = {c} hasn't solutions.")
    else:
        print(f"The solution of {a}x + {b}y = {c} is: " + '{' + f"({x} + {xk}k, {y} + {yk}k), k integer" + '}')
    _print_header_footer("Diofantine Equation", header=False)


def dm_linear_congruence():
    _print_header_footer("Linear Congruence")
    print("ax -congr- b mod n")
    a, b, n = _get_input({'a': int, 'b': int, 'n': int})
    z_sol, zn_sol = utils.linear_congruence(a, b, n)

    if z_sol is None: 
        print(f"The linear congruence {a}x = {b} mod({n}) hasn't solutions.")
    else:
        print(f"The linear congruence {a}x = {b} mod({n}): ")
        print(f"\tHas solutions in Z: " + '{' + f"({z_sol[0]} + {z_sol[1]}k), k integer" + '}')
        print(f"\tHas solutions in Zn: " + ', '.join([str(x) for x in zn_sol]))

    _print_header_footer("Linear Congruence", header=False)


def dm_euler_function():
    _print_header_footer('Euler Function')
    n = _get_input({'n': int})
    ef = utils.euler_function(n)
    if type(ef) is not int:
        print(ef)
    else:
        print(f'Euler function of {n} is: {ef}')
    _print_header_footer('Euler Function', header=False)


def dm_find_modulus():
    _print_header_footer('Find Modulus')
    a, m, n =_get_input({'a': int, 'm': int, 'n': int}, 'a^m is ? in mod n')
    r = utils.find_modul(a, m, n)
    if type(r) is not int:
        print(str(r))
    else:
        print(f'{a}^{m} is equal to {r} in Z-{n}.')
    _print_header_footer('Find Modulus', header=False)


def dm_two_congruences_system():
    _print_header_footer('Two Congruence System')
    info = "x congr a1 mod n1\nx congr a2 mod n2"
    a1, n1, a2, n2 = _get_input({'a1': int, 'n1': int, 'a2': int, 'n2': int}, info)

    r = utils.two_congruence_system(a1, n1, a2, n2)

    if type(r) is str: print(r)
    else: print(f'The system has solution {r[0]} mod {r[1]}.')

    _print_header_footer('Two Congruence System', False)


def print_menu():
    tag = 'dm_'
    while True:
        print('What you want to do?')
        options = [opt for opt in sorted(globals()) if opt.startswith(tag)]
        options = {i+1: opt for i, opt in enumerate(options)}
        exit_key = 'Any key'
        options[exit_key] = 'Exit'

        for i, opt in options.items():
            o = opt.removeprefix(tag)
            o = ' '.join([w.capitalize() for w in o.split('_')]) if '_' in o else o
            print(f'{i}: {o}')

        userin = input()
        try:
            userin = int(userin)
            if userin <= 0 or userin >= len(options): raise ValueError
        except ValueError:
            print('Bye!')
            return
        
        globals()[options[userin]]()
        input()


def main():
    print_menu()


if __name__ == '__main__':
    main()
