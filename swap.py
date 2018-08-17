def swapfun():
    a = input('Enter your input:')
    b = input('Enter your input:')
    lista = list(a)
    listb = list(b)

    # Check if lenghth of lists match
    if len(lista)==len(listb):
        if(set(lista) == set(listb)):
            print('Ho Gaya')
        else:
            print('Nahi Huwa')
    else:
        print('Hoga hi nahi')

swapfun()
