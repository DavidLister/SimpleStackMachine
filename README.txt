Stack Machine

A stack machine that uses Reverse Polish Notation.

All numbers are positive integers.


Notation:
a - bottom value of the stack
b - seccond bottom value of the stack

Instructions:

	Push:
		Function:
			Pushes value to bottom of stack, replaces these values with the result.
	
		Syntax:
			push [value]

	Add:
		Function:
			Adds bottom two values from stack, replaces these values with the result. (a + b)

		Syntax:
			add or +

	Subtract:
		Function:
			Subtracts the bottom value of the stack from the seccond bottom value of the stack, replaces these values with the result. (b - a)

		Syntax:
			subtract or -
	
	Multiply:
		Function:
			Multiplies the bottom two values of the stack, replaces these values with the result. (a * b)

		Syntax:
			multiply or *

	Divide:
		Function:
			Divides the seccond bottom value of the stack by the bottom value of the stack, replaces these values with the result. The value is rounded down to the nearest integer. (b/a)

		Syntax:
			divide or /

	Goto:
		Function:
			Changes line address on disk to specified line (indexed from 0).  Note that the line address is always incremented by 1 so the actual line processed next will be the line after the one specefied.  Limited to 7 bit numbers. (0 - 255)

		Syntax:
			goto [line number]

	If:
		Function:
			If the value of the bottom value of the stack does not equal 0, move to the next line, else, skip the next line. The values compared are removed from stack.

		Syntax:
			if

	Get:
		Function:
			Not used currently, will be used to retrieve hardware inputs future

		Syntax:
			get [output # (0-3)]

	Display:
		Function:
			Prints value the bottom value of the stack, keeps the value in stack.

		Syntax:
			display 0 or disp 0

	Copy:
		Function:
			Copies the bottom value of the stack, the bottom two values of the stack now become the same value.

		Syntax:
			copy

	Delete:
		Function:
			Deletes the bottom value from the stack

		Syntax:
			delete or del

	Bitshift right:
		Function:
			Bitshifts to the right once, replaces the bottom value of the stack.

		Syntax:
			bitshift right or >>

	Bitshift left:
		Function:
			Bitshifts to the left once, replaces the bottom value of the stack.

		Syntax:
			bitshift left or <<

	Swap:
		Function:
			Swaps the bottom two values of the stack

		Syntax:
			swap

	Greater than:
		Function:
			Compares b > a, replaces the values with 1 if True and 0 if False

		Syntax:
			greater than or >

	Equal to:
		Function:
			compares a == b, replaces the values with 1 if True and 0 if False

		Syntax:
			equal to or = or ==

	Halt:
		Function:
			Halts the stack machine.  Must be used at the end of a program.

		Syntax:
			halt


Code Examples:

factorial.code

push 6 # This is the operand for the factorial
copy
push 1
subtract
copy
if
goto 0
delete
swap
copy
if
goto 14
delete
display 0
halt
multiply
goto 7

Compiled Code

000000110/ Push 6
100010001/ Copy
000000001/ Push 1
100000001/ Subtract
100010001/ Copy
100010000/ If
1100000000/ Goto 0
100010010/ Delete
100010101/ Swap
100010001/ Copy
100010000/ If
1100001110/ Goto 14
100010010/ Delete
100001000/ Display 0
100011000/ Halt
100000010/ Multiply
1100000111/ Goto 7


equivalent to:

6!

or

lst = range(6)
tally = 1
for item in lst:
	tally = tally * item

print tally




How to compile:

Write code in a normal text file, usign the program compile.py through the command line, it can be compiled using the following commands:

Unix:
python /path/to/compile.py /path/to/[texfile].[anything] /path/to/[output name].[anything]

Windows:

c://path/to/compile.py c://path/to/[texfile].[anything] c://path/to/[output name].[anything]


How to run the program in the stack machine.

- Start the stack machine by your prefered method.
- Input file name when asked
- Watch it run


There is a print command in the run function used to print the stack before after every cycle.





