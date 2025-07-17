def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
        exit()

def is_float(a) :  # 실수 연산자 구분용
    try :
        float(a)
        return True
    except ValueError :
        return False

def check_parenthesis(list_input) :  # 괄호 짝 확인용
    if "(" not in list_input and ")" not in list_input :
        print("Invalid input.")
        exit()

def input_expr(expr) :
    try :
        tokens = expr.strip().split()
    except ValueError :
        print("Invalid input.")
        exit()
    return tokens


dic_calculate = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}
dic_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}


def calculate_expr(expr): # 중위표기식(input) -> 후위표기식
    tokens = input_expr(expr)
    list_output = []
    list_stack = []

    for comp in tokens:
        if is_float(comp):
            list_output.append(comp)

        elif comp == "(":
            list_stack.append(comp)
            check_parenthesis(tokens)
        elif comp == ")":
            check_parenthesis(tokens)
            while list_stack[-1] != "(":
                list_output.append(list_stack.pop())
            list_stack.pop()

        elif comp in dic_calculate:  # 연산자
            while (
                list_stack and
                list_stack[-1] != "(" and
                dic_precedence[list_stack[-1]] >= dic_precedence[comp]
            ):
                list_output.append(list_stack.pop())
            list_stack.append(comp)
        else :
            print("Invalid input.")
            exit()

    while list_stack:
        list_output.append(list_stack.pop())
    
    return calculate_nota(list_output)


def calculate_nota(list_input) :  # 후위표기식 계산
    list_stack = []
    for comp in list_input :
        if is_float(comp) :
            list_stack.append(float(comp))
        else :
            second_num = list_stack.pop()
            first_num = list_stack.pop()
            if comp in dic_calculate :
                result = dic_calculate[comp](first_num, second_num)
                list_stack.append(result)

    return result


def main():
    expr = input("")
    final_result = calculate_expr(expr)
    print(f"Result: {final_result}")
       
if __name__ == "__main__":
    main()