def show_result(method_result, precision=6):
    method = method_result[0]
    result = method_result[1]
    print(method)
    if result.is_right():
        xs, steps = result.get_value()
        print(f"Solved in {steps} steps...")
        xs = list(map(lambda x: round(x, precision), xs))
        if len(xs) == 1:
            xs = xs[0]
        print(f"x = {xs}")
    else:
        message = result.get_error()
        print(message)


def show_results(results):
    for result in results:
        show_result(result)