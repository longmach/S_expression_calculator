import sys

# time complexity: O(n) where n is the length of the string
#       because I only loop through the string input once in reversed order
# space complexity: O(n) where n is the length of the string
#       because I use one stack with maximum size n to store the expression as I loop through the input.
#
# Code clarity: please follow the comments
# Abstraction: I ultilized stack to optimize the program's time complexity
# Extensibility: 
#       - this program supports more than 2 arguments. Eg: (add 1 2 3 4 (multiply 2 3 5))
#       - for more operators (function type), I can add more to the logic of evaluate_expr()
#       - for more complex cases, I can move evaluate_expr() to a new file and build a new class
# User experience:
#       - for more complex case, I can move print_error to a new file and build a new class 
#           that have a specific error handling function for each error type

class Expression:
 
    def evaluate_expr(self, stack):
        try:
            res = 0           
            
            #get the operator
            sign = stack.pop()
            
            if stack:
                #pop the first number
                res = stack.pop()
                #pop the second numer and do the operation
                if sign == '+':
                    # to pop more number if more arguments instead of 2
                    # eg: (add 1 2 3 4 (multiply 2 3 5))
                    while stack[-1] != ')':
                        res += stack.pop()
                elif sign == '*':
                    # to pop more number if more arguments instead of 2
                    # eg: (add 1 2 3 4 (multiply 2 3 5))
                    while stack[-1] != ')':
                        res *= stack.pop()

                # add more operators (function type) here if needed
                # eg: (exponent 2 5)

                if stack[-1] == ')':
                    stack.pop()

                
            return res

        except:
            print_error()  

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0
        i = len(s) - 1

        while i > -1:
            ch = s[i]

            if ch.isdigit():
                # Forming the operand - in reverse order. 
                # Eg: 12 will be read as 2, 1 so 1*10^0 + 2*10^1
                operand += (10**n * int(ch))
                n += 1
            
            elif ch == ' ':
                if n:
                    # Save the operand on the stack
                    # As I encounter ' '
                    stack.append(operand)
                    n, operand = 0, 0

            else:
                #closing bracket signals the need to evaluate 2 most recent operands
                if ch == '(':         
                    res = self.evaluate_expr(stack)
                    # Append the evaluated result to the stack.
                    stack.append(res)

                # For other non-digits.
                # if expression is 'add' then it ends with 'd' and move i back 2 unit
                elif ch == 'd':
                #elif ch == 'd':
                    stack.append('+')
                    i -= 2
                # if expression is 'multiply' then it ends with 'y' and move i back 7 unit
                elif ch == 'y':
                    stack.append('*')
                    i -= 7
                
                # if char == ')', append it to stack
                else:
                    stack.append(ch)
                # add more expression check here for operators if needed

            i -= 1

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        #only the final answer remains in the stack, return it
        return stack[0]

# basic error message
def print_error():
    print('Not valid input')
    print('valid input must be either: ')
    print('1- (FUNCTION EXPR EXPR)')
    print('    Example: (add 123 456)')
    print('2- integer')
    print('    Example: 123')

def main():
    # Basic eror handling when no expression present:
    try:
        print(Expression().calculate(sys.argv[1]))
    except:
        print_error()
    # I can also use the line below for name of error 
    # except Exception as e: print(e)


if __name__ == '__main__':
    main()
