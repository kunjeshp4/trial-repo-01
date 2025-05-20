import argparse
from naked_math import add, subtract, multiply, div, exponential


def main(argv=None):
    """Command line interface for math operations."""
    parser = argparse.ArgumentParser(description="Perform basic math operations")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Sum numbers")
    parser_add.add_argument("numbers", nargs="+", type=float)

    parser_sub = subparsers.add_parser("subtract", help="Subtract numbers from the first")
    parser_sub.add_argument("numbers", nargs="+", type=float)

    parser_mul = subparsers.add_parser("multiply", help="Multiply numbers")
    parser_mul.add_argument("numbers", nargs="+", type=float)

    parser_div = subparsers.add_parser("div", help="Divide the first number by the rest")
    parser_div.add_argument("numbers", nargs="+", type=float)

    parser_exp = subparsers.add_parser("exponential", help="Exponentiate sequentially")
    parser_exp.add_argument("numbers", nargs="+", type=float)

    args = parser.parse_args(argv)

    if args.command == "add":
        result = add(*args.numbers)
    elif args.command == "subtract":
        result = subtract(*args.numbers)
    elif args.command == "multiply":
        result = multiply(*args.numbers)
    elif args.command == "div":
        result = div(*args.numbers)
    elif args.command == "exponential":
        result = exponential(*args.numbers)
    else:
        parser.error("Unknown command")
    print(result)


if __name__ == "__main__":
    main()
