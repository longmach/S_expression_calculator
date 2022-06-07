# S Expression Calculator

### Introduction
    
This project implement a simple calculator: it takes a single argument as an expression and prints out the integer result of evaluating it..
	  
A function call takes the following form:

(FUNCTION EXPR EXPR)

A function call is always delimited by parenthesis `(` and `)`.

The `FUNCTION` is one of `add` or `multiply`.

The `EXPR` can be any arbitrary expression, i.e. it can be further function
calls or integer expressions.

Exactly one space is used to separate each term.

For example:

    (add 123 456)

    (multiply (add 1 2) 3)


	

### Files

    This project includes 2 files:
    - calc.py        			(This implements the S Expression Calculator)
    - test.py             (this includes basic tests)

### Testing

	- Unzip the files in your testing environment.
	- Open the terminal
	- To test, run the following commands in the terminal:
		python ./calc.py (FUNCTION EXPR EXPR)
    Example: python ./calc.py "(add 12 12)"
