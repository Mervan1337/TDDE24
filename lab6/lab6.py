from calc import *
import copy


def expression_value(value, variables):
    """ Checks if the expression is a integer or a string else it should raise an error"""
    if not isinstance(value, str):
        return value
    elif value in variables:
        return variables[value]
    else:
        raise ValueError(f"\
        {value} has not yet been defined")


def calculate(expression, variables):
    """ Calculates the expression depending on what operator it is (uses eval_binaryexpr)"""
    if is_constant(expression):
        return expression
    elif is_variable(expression):
        return expression_value(expression, variables)
    if is_binaryexpr(expression):
        if is_binaryoper(expression[1]):
            return eval_binaryexpr(expression, variables)
        else:
            raise SyntaxError('Incorrect operator')  # Raises SyntaxError if user has put in a faulty operator

def interp(expression, variables):
    """ Interprets an expression, returning a boolean fitting. """
    try:
        if not isinstance(expression, list):
            return expression_value(expression, variables)
        else:
            cond_left = condition_left(expression)
            #print(calculate(cond_left, variables), expression, variables)
            if len(expression) == 2 and cond_left == "not":
                return not interp(expression[1], variables)
            elif len(expression) == 3:
                cond_right = condition_right(expression)
                if is_condoper(condition_operator(expression)):
                    if condition_operator(expression) == ">":
                        return calculate(cond_left, variables) >    calculate(cond_right, variables)
                    if condition_operator(expression) == "<":
                        return calculate(cond_left, variables) <    calculate(cond_right, variables)
                    if condition_operator(expression) == "=":
                        return calculate(cond_left, variables) ==   calculate(cond_right, variables)

                elif condition_operator(expression) == "and":
                    return interp(cond_left, variables)        and  interp(cond_right, variables)
                elif condition_operator(expression) == "or":
                    return interp(cond_left, variables)        or   interp(cond_right, variables)
                else:
                    raise SyntaxError("Error unsupported operators")
    except ValueError as e:
        raise e


def exec_assignment(line, variables):
    """ Takes in two variables and setting variables returning dict after assignment """
    variable = assignment_variable(line)
    expression = assignment_expression(line)

    variables[variable] = calculate(expression, variables)
    return variables


def exec_repetition(line, variables):
    """ Executes a while-loop returning dict"""
    condition = repetition_condition(line)
    while interp(condition, variables):
        variables = exec_program(line[2:], variables) 
    return variables

def exec_selection(line, variables):
    """ Executes a if statement """
    if interp(line[1], variables):
        variables = exec_program(line[2], variables)
    else:
        if len(line) > 3:
            variables = exec_program((line[3]), variables)
    return variables

def exec_input(line, variables):
    """ Executes an input statement """
    variable = input_variable(line)
    variables[variable] = int(input(f"Enter value for {variable}: "))
    return variables

def exec_output(line, variables):
    """ Executes an output statement """
    expression = output_expression(line)
    if isinstance(expression, list):
        print(calculate(line[1], variables))
    else:
        if isinstance(expression, str):
            print(f"{expression} = {expression_value(output_expression(line), variables)}")

def eval_binaryexpr(expression, variables):
    """ Uses calculate functions doing the correct mathmatical operation """
    left_expression = calculate(expression[0], variables)
    right_expression = calculate(expression[2], variables)
    # Addition
    if expression[1] == "+":
        return left_expression + right_expression
    # Subtraction
    if expression[1] == "-":
        return left_expression - right_expression
    # Division
    if expression[1] == "/":
        return left_expression / right_expression
    # Multiplication
    if expression[1] == "*":
        return left_expression * right_expression

def exec_program(calc, variable_list=None):
    """ Executes the program with help of recurssion it translates from calc to python code"""
    # By setting a variable list to none in the def, the first variable list wont be affected if run recurrently
    if variable_list is None:
        variable_list = {}
    variables = variable_list
    # Base case that removes our first list and gets us into the first nestled list
    if is_program(calc): #-------- Ändra till program_statment så vi slipper komplettering
        variables = exec_program(program_statements(calc), variables)
    # When first list is removed we can access the first real lines of code 
    else:
        # Execute all lines in program
        # Sets line to current line to be executed.
        if isinstance(calc[0], list):
            """If the first argument is a list, set line to it. The execute it."""
            line = calc[0]
        else:
            line = calc
        # Assignment
        if is_assignment(line):
            variables = copy.deepcopy(variable_list)
            variables = exec_assignment(line, variables)
        # Input
        if is_input(line):
            variables = copy.deepcopy(variable_list)
            variables = exec_input(line, variables)
        # Print
        if is_output(line):
            exec_output(line, variables)
        # If
        if is_selection(line):
            variables = exec_selection(line, variables)
        # While
        if is_repetition(line):
            variables = exec_repetition(line, variables)
        if len(calc) > 1:   # If it has more than 1 list it goes down one more time again into the nestled lists
            variables = exec_program(calc[1:], variables)
    if variables is variable_list:
        return variable_list
    return variables

"""_loop_prog = [
        "calc",
        ["read", "n"],
        ["set", "sum", 0],
        [
            "while",
            ["n", ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"],
    ]
_loop_with_binexpr_prog = [
    "calc",
    ["read", "n"],
    ["set", "sum", 0],
    [
        "while",
        [["n", "-", 1], ">", 0],
        ["set", "sum", ["sum", "+", "n"]],
        ["set", "n", ["n", "-", 1]],
    ],
    ["print", "sum"],
]

_if_prog = [
        "calc",
        ["read", "x"],
        ["set", "zero", 0],
        ["set", "pos", 1],
        ["set", "nonpos", -1],
        ["if", ["x", "=", 0], ["print", "zero"]],
        ["if", ["x", ">", 0], ["print", "pos"]],
        ["if", ["x", "<", 0], ["print", "nonpos"]],
    ]

exec_program(_loop_prog)"""