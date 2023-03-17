def program_info():
    return "This program solves non-lenear equations and non-lenear eqaution systems"


def get_type_number():
    print("Enter 1 if you want to solve an equation or 2 if you want to solve a system")
    return int(input())


def get_equation_number():
    from single.default_equations import equations
    print("Choose one of the following equations:")
    for i, eq in enumerate(equations):
        print(f"{i + 1}. {eq}")
    return int(input("Enter number of equation: "))

def get_system_number():
    from equaction_system.default_systems import systems
    print("Choose one of the following systems")
    for i, system in enumerate(systems):
        print(f"{i+1}. {system}")

def solve_equation(number):
    pass

def show_result(result):
    pass

def solve_equation_system(number):
    pass

def show_error_message():
    pass
def run():
    print(program_info())
    choise = get_type_number()
    if choise == 1:
        equation_number = get_equation_number()
        result = solve_equation(equation_number)
        show_result(result)
        return
    if choise == 2:
        equation_system_number = get_system_number()
        result = solve_equation_system(equation_system_number)
        show_result(result)
        return
    show_error_message()