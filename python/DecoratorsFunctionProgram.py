''' Decorators '''
def div(a,b) :
    return a/b

def smart_Div(func) :
    def inner(a,b) :
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner

div = smart_Div(div)

print("Using variable call ",div(5,10))


print("Direct call ",smart_Div(div)(50,10))
