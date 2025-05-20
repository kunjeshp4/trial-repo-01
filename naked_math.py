"""Basic algebra operations supporting any number of arguments."""

def add(*args):
    """Return the sum of all arguments."""
    return sum(args)


def subtract(*args):
    """Subtract all following arguments from the first one."""
    if not args:
        raise ValueError("At least one argument is required")
    first, *rest = args
    return first - sum(rest)


def multiply(*args):
    """Return the product of all arguments."""
    result = 1
    for arg in args:
        result *= arg
    return result


def div(*args):
    """Divide the first argument by each of the remaining arguments sequentially."""
    if not args:
        raise ValueError("At least one argument is required")
    result = args[0]
    for divisor in args[1:]:
        result /= divisor
    return result


def exponential(*args):
    """Sequentially exponentiate starting from the first argument."""
    if not args:
        raise ValueError("At least one argument is required")
    result = args[0]
    for exp in args[1:]:
        result **= exp
    return result


if __name__ == "__main__":
    from cli import main as cli_main
    cli_main()
