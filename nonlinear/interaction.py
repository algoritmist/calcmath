def program_info():
    return "This program solves non-lenear equations and non-lenear eqaution systems"


def get_type_number():
    print("Enter 1 if you want to solve an equation or 2 if you want to solve a system")
    return int(input())


def get_equation_number():
    from single.default_equations import equations
    print("Choose one of the following equations:")
    for i, eq in enumerate(equations):
        # TODO: pretty print
        print(f"{i + 1}. {eq}")
    return int(input("Enter number of equation: "))


def get_system_number():
    from equaction_system.default_systems import systems
    print("Choose one of the following systems")
    for i, system in enumerate(systems):
        print(f"{i + 1}. {system}")


def show_result(result):
    print(result[0])
    print(result[1])


def show_error_message():
    pass


def run():
    print(program_info())
    choise = get_type_number()
    if choise == 1:
        equation_number = get_equation_number()
        from single.default_equations import solve_equation
        result = solve_equation(equation_number - 1)
        show_result(result)
        return
    if choise == 2:
        system_number = get_system_number()
        from equaction_system.default_systems import solve_system
        result = solve_system(system_number - 1)
        show_result(result)
        return
    show_error_message()
