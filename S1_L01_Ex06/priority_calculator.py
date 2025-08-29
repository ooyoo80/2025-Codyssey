def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        exit()
    return a / b


def calculate_expression(expr):
    try:
        tokens = expr.strip().split()
        if len(tokens) < 3 or len(tokens) % 2 == 0:
            print("Error")
            exit()

        numbers = []
        operators = []
        for i, token in enumerate(tokens):
            if not i % 2:
                numbers.append(float(token))
            else:
                if token not in ('+', '-', '*', '/'):
                    print("Invalid input.")
                    exit()
                operators.append(token)


        i = 0
        while i < len(operators):
            if operators[i] == '*' or operators[i] == '/':
                a = numbers[i]
                b = numbers[i+1]
                if operators[i] == '*':
                    result = multiply(a, b)
                else:
                    result = divide(a, b)

                numbers[i] = result
                del numbers[i+1]
                del operators[i]
            else:
                i += 1
   
            
        j = 0
        while j < len(operators):
            if operators[j] == '+':
                result = add(numbers[j], numbers[j+1])
                numbers[j] = result
                del numbers[j+1]
                del operators[j]
            else:
                result = subtract(numbers[j], numbers[j+1])
                numbers[j] = result
                del numbers[j+1]
                del operators[j]

        return result
    

    except ValueError :
        print("Invalid input.")
        exit()



def main():
    expr = input("")
    final_result = calculate_expression(expr)
    print(f"Result: {final_result}")

if __name__ == "__main__":
    main()