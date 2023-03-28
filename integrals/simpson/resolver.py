from typing import List

from functional_progamming.fputils import Either, Right, Left
import integrals.classes.methods as methods


def resolve(results: List[Either], method: methods.MethodType) -> Right:
    unresolvable = list(filter(lambda r:
                               r.is_left() and r.get_error().is_unresolvable(),
                               results))
    if len(unresolvable) != 0:
        return Left.chain(unresolvable)

    resolvable = filter(lambda r: r.is_left(), results)
    resolved = list(map(lambda r: methods.resolve(r.get_error(), method), resolvable))
    correct = list(filter(lambda r: r.is_right(), results))

    return Right.chain(correct + resolved)
