import sys
from typing import Any, Callable


class Flag:
    def __init__(self, short: str, long: str, func: Callable[[], None], help_text: str) -> None:
        self.short = short
        self.long = long
        self.func = func
        self.help_text = help_text

    def __call__(self) -> None:
        self.func()

    def __repr__(self) -> str:
        return f"<Flag:{self.short},{self.long}>"


class Cli:
    flags: list[Flag] = []
    arguments: dict[int, Callable[[Any], None]] = {}

    def __init__(self, cmd_args: list) -> None:
        self.cmd_args = cmd_args

    def argument(self, position: int, help_text: str) -> Callable[[Any], None]:
        """
        Set a callback for the argument at the given position.
        :param position: The position of the argument in the command line arguments (starts at 1)
        """
        def inner(func: Callable[[Any], None]):
            self.arguments[position] = func

        return inner

    def flag(self, short_flag: str, long_flag: str, help_text: str) -> Callable[[], None]:
        def inner(func: Callable[[], None]):
            self.flags.append(
                Flag(short_flag, long_flag, func, help_text)
            )
        return inner

    def execute(self) -> None:
        arg_count = 1
        for arg in self.cmd_args:
            if arg.startswith("-"):
                for flag in self.flags:
                    if arg == flag.short or arg == flag.long:
                        flag()
            else:
                if arg_count in self.arguments:
                    self.arguments[arg_count](arg)
                arg_count += 1

    def __str__(self) -> str:
        flag_texts = '\n\t'.join(
            f'{flag.short}, {flag.long} {flag.help_text}\n' for flag in self.flags)
        return f"Usage: python3 __main__.py [algorithm] [flags]\n\nFlags:\n\t{flag_texts}"
