def answer(expr):
    terms = expr.split('+')
    factors = [ term.split('*') for term in terms ]
    multArray = []
    for item in factors:
    	cat = ''.join(item)
    	cat += '*'*(len(item) - 1)
    	multArray.append(cat)

    finalString = ''.join(multArray) + '+'*(len(multArray) - 1)


    rpn_expr = '{}{}'.format(''.join(multArray), '+'*(len(multArray)-1))
    return finalString