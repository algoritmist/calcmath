from functional_progamming.fputils import Either


def show_result(result: Either):
    if result.is_right():
        return result.get_value()
    return f'Function has unresolvable breaks at: {[err.x for err in result.get_error()]}'
