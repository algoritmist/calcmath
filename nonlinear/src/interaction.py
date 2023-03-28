from nonlinear.utils import *

def program_info():
    return "This program solves non-lenear equations and non-lenear eqaution systems"


def get_type_number():
    print("Enter 1 if you want to solve an equation or 2 if you want to solve a system")
    return int(input())


def get_equation_number():
    from nonlinear.single.default_equations import equations
    print("Choose one of the following equations:")
    for i, eq in enumerate(equations):
        # TODO: pretty print
        print(f"{i + 1}. {eq}")
    return int(input("Enter number of equation: "))


def get_system_number():
    from nonlinear.equation_system.default_systems import systems
    print("Choose one of the following systems:")
    for i, system in enumerate(systems):
        print(f"{i + 1}. {system}")
    return int(input("Enter number of system: "))


def get_error():
    return float(input("Enter error: "))


def get_range(variable_name):
    print(f"Enter range for {variable_name}: ")
    a = float(input("l = "))
    b = float(input("r = "))
    return a, b


def get_ranges(free_variables):
    lst = [get_range(variable) for variable in free_variables]
    return lst


def run():
    print(program_info())
    while True:
        try:
            err = get_error()
            choise = get_type_number()
            if choise == 1:
                equation_number = get_equation_number()
                from nonlinear.single.default_equations import solve_equation
                a, b = get_range('x')
                results = solve_equation(equation_number - 1, a, b, err)
                show_results(results)
                continue
            if choise == 2:
                system_number = get_system_number()
                from nonlinear.equation_system.default_systems import solve_system, free_variables
                # print(free_variables(system_number - 1))
                ranges = get_ranges(free_variables(system_number - 1))
                result = solve_system(system_number - 1, ranges, err)
                show_result(result)
                continue
            raise Exception("Choose 1 or 2")
        except Exception as ex:
            pass
            print("A problem occurred")
            print(ex)
