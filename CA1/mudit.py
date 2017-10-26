import sys

def done(value):
    return value == 'q'

inp = ''
while not done(inp):
    inp = raw_input('Please press 1 to conver to Celsius and 2 to conver to Fahrenheit: ')
    try:
        c = float(inp)
        if c == 1:
            ftemp= float(raw_input('Please enter temp in F'))
            cel = (ftemp - 32)*5/9
            print cel
        elif c == 2:
            ctemp = float(raw_input('Please enter temp in C'))
            fah = ctemp*9/5 + 32
            print fah
        inp = raw_input('Press any key for menu, q to quit: ')
    except:
        print 'enter 1 or 2 only'

