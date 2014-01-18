# StackMachine.py

import time

PUSH, ADD, SUBTRACT, MULTIPLY, DIVIDE, GOTO, IF, GET, DISP, COPY, DELETE, BITSHIFT_RIGHT, BITSHIFT_LEFT, SWAP, GREATER_THAN, EQUAL_TO, HALT = range(17)

class Stack:
    
    def __init__(self, height):
        self.stack = [0] * height
        self.height = height

    def push(self, number):
        self.stack = [number] + self.stack
        self.update()

    def update(self):
        if len(self.stack) > self.height:
            self.stack = self.stack[:self.height]

        while len(self.stack) < self.height:
            self.stack.append(0)

    def retrieve(self):
        out = self.stack.pop(0)
        self.update()
        return out

    def copy(self):
        bit = self.retrieve()
        self.push(bit)
        self.push(bit)

    def delete(self):
        self.retrieve()

    def __str__(self):
        out = ' -\n'
        for item in self.stack[::-1]:
            out += str(item) + '\n'

        out = out + '---\n'

        return out


class ALU:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        return b * a

    def divide(self, a, b):
        return int(b) / int(a)

    def bit_shift_left(self, a):
        return a << 1

    def bit_shift_right(self, a):
        return b >> 1

    def greater_than(self, a, b):
        return int(b > a)

    def equal(self, a, b):
        return int(a == b)


class DiskSpace:

    def __init__(self):
        self.disk = []
        self.address = 0

    def load(self, fileName):
        ## format is:
        ## 000010111/ Push 23
        f = list(open(fileName, 'r'))

        for item in f:
            self.disk.append(Code(item.split('/')[0]))

    def increment(self):
        self.address += 1

    def retrieve(self):
        return self.disk[self.address]

    def goto(self, new_address):
        self.address = new_address

    
class Code:

    def __init__(self, raw_code):
        self.raw = raw_code
        self.number = int(raw_code[1:], 2)

        if raw_code[:2] == '11':
            self.command = GOTO

        elif raw_code == '100000000':
            self.command = ADD

        elif raw_code == '100000001':
            self.command = SUBTRACT

        elif raw_code == '100000010':
            self.command = MULTIPLY

        elif raw_code == '100000011':
            self.command = DIVIDE

        elif raw_code[:7] == '1000001':
            self.command = GET

        elif raw_code[:6] == '100001':
            self.command = DISP

        elif raw_code == '100010000':
            self.command = IF

        elif raw_code == '100010001':
            self.command = COPY

        elif raw_code == '100010010':
            self.command = DELETE

        elif raw_code == '100010011':
            self.command = BITSHIFT_RIGHT

        elif raw_code == '100010100':
            self.command = BITSHIFT_LEFT

        elif raw_code == '100010101':
            self.command = SWAP

        elif raw_code == '100010110':
            self.command = GREATER_THAN

        elif raw_code == '100010111':
            self.command = EQUAL_TO

        elif raw_code == '100011000':
            self.command = HALT

        else:
            self.command = PUSH

    


class StackMachine:

    def __init__(self, fname = '', stackHeight = 16):
        self.stack = Stack(stackHeight)
        self.alu = ALU()
        self.disk = DiskSpace()

        if fname:
            self.disk.load(fname)


    def main(self):
        code = self.disk.retrieve()
        
        if code.command == PUSH:
            self.stack.push(code.number)

        elif code.command == GOTO:
            address = int(code.raw[2:], 2)
            self.disk.goto(address)

        elif code.command == ADD:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.add(a, b)
            self.stack.push(s)

        elif code.command == SUBTRACT:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.subtract(a, b)
            self.stack.push(s)

        elif code.command == MULTIPLY:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.multiply(a, b)
            self.stack.push(s)

        elif code.command == DIVIDE:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.divide(a, b)
            self.stack.push(s)

        elif code.command == ADD:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.add(a, b)
            self.stack.push(s)

        elif code.command == GET:
            ## Not implemented due to lack of hardware IO
            pass

        elif code.command == DISP:
            self.stack.copy()
            disp = self.stack.retrieve()
            print disp

        elif code.command == IF:
            a = self.stack.retrieve()
            if a != 0:
                pass
            
            else:
                self.disk.increment()

        elif code.command == COPY:
            self.stack.copy()

        elif code.command == DELETE:
            self.stack.retrieve()

        elif code.command == BITSHIFT_RIGHT:
            a = self.stack.retrieve()
            s = self.alu.bitshift_right(a)
            self.stack.push(s)

        elif code.command == BITSHIFT_LEFT:
            a = self.stack.retrieve()
            s = self.alu.bitshift_left(a)
            self.stack.push(s)

        elif code.command == SWAP:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            self.stack.push(a)
            self.stack.push(b)

        elif code.command == GREATER_THAN:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.greater_than(a, b)
            self.stack.push(s)

        elif code.command == EQUAL_TO:
            a = self.stack.retrieve()
            b = self.stack.retrieve()
            s = self.alu.equal_to(a, b)
            self.stack.push(s)

        elif code.command == HALT:
            return True
        
        self.disk.increment()

        return False

    def run(self, delay = 0):
        over = False
        while not over:
            time.sleep(delay)
            print self.stack
            over = self.main()

if __name__ == '__main__':
    print '    Stack Machine'
    print
    fname = raw_input('  Please input code file name: ')
    stack_machine = StackMachine(fname)
    stack_machine.run(0.1)
        
        
