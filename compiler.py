# compiler.py

import sys

def dec_to_bin(a, n = 8):
    b = bin(int(a))[2:]

    # ensure b in n bits long
    
    if len(b) < n:
        b = (n - len(b)) * '0' + b

    elif len(b) > n:
        b = b[len(b) - n:]

    return b

if len(sys.argv) < 3:
    print "Usage: compiller.py <source> <output>"
    sys.exit(1)

fname = sys.argv[1]
fnameOut = sys.argv[2]

f = list(open(fname, 'r'))

clean = []
for item in f:
    clean.append(item.rstrip())

out = ''
for line in clean:
    print line
    if 'push' in line:
        s = line.split(' ')
        out = out + '0' + dec_to_bin(s[1]) + '/ Push ' + s[1] + '\n'
        
    elif ('add' in line) or ('+' in line):
        out = out + '100000000/ Add\n'

    elif ('subtract' in line) or ('-' in line):
        out = out + '100000001/ Subtract\n'

    elif ('multiply' in line) or ('*' in line):
        out = out + '100000010/ Multiply\n'

    elif ('divide' in line) or ('/' in line):
        out = out + '100000011/ Divide\n'

    elif 'goto' in line:
        s = line.split(' ')
        out = out + '11' + dec_to_bin(s[1]) + '/ Goto ' + s[1] + '\n'

    elif 'if' in line:
        out = out + '100010000/ If\n'
    
    elif 'get' in line:
        s = line.split(' ')
        out = out + '1000001/ Get ' + dec_to_bin(s[1], 2) + '/ ' + s[1] + '\n'

    elif 'disp' in line:
        s = line.split(' ')
        out = out + '100001' + dec_to_bin(s[1], 3) + '/ Display ' + s[1] + '\n'

    elif 'copy' in line:
        out = out + '100010001/ Copy\n'

    elif 'del' in line:
        out = out + '100010010/ Delete\n'

    elif ('bitshift right' in line) or ('>>' in line):
        out = out + '100010011/ Bitshift right\n'

    elif ('bitshift left' in line) or ('<<' in line):
        out = out + '100010100/ Bitshift left\n'

    elif 'swap' in line:
        out = out + '100010101/ Swap\n'

    elif ('greater than' in line) or ('>' in line):
        out = out + '100010110/ Greater than\n'

    elif ('equal to' in line) or ('=' in line):
        out = out + '100010111/ Equal to\n'

    elif 'halt' in line:
        out = out + '100011000/ Halt\n'

fout = open(fnameOut, 'w')
fout.write(out)
fout.close()

print 'Success!'

