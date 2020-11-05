def format_float(number):
    return f'{number:.2f}'

def format_point(x=None, y=None, z=None):
    out = 'G1'
    if x is not None:
        out += f' X{format_float(x)}'
    if y is not None:
        out += f' Y{format_float(y)}'
    if z is not None:
        out += f' Z{format_float(z)}'
    return out
