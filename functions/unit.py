def unit_n(n,units):
    try:
        return units[n]
    except IndexError:
        return None

# lst=['fit1045', 'fit1047', 'fit1051', 'mat1830']
# print(unit_n(0,lst))
# print(unit_n(1,lst))
# print(unit_n(2,lst))
# print(unit_n(3,lst))
# print(unit_n(4,lst))