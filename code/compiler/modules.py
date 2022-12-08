import re


def keywords():
    return [
        "class",
        "constructor",
        "function",
        "method",
        "field",
        "static",
        "var",
        "int",
        "char",
        "boolean",
        "void",
        "true",
        "false",
        "null",
        "this",
        "let",
        "do",
        "if",
        "else",
        "while",
        "return",
    ]


def symbols():
    return [
        "{",
        "}",
        "(",
        ")",
        "[",
        "]",
        ".",
        ",",
        ";",
        "+",
        "-",
        "*",
        "/",
        "&",
        "|",
        "<",
        ">",
        "=",
        "~",
    ]


def constant_int():
    # 0 - 32767
    p = (
        r"^([0-2]?\d{0,4})$|"
        r"^(3[0-1]\d{3})$|"
        r"^(32[0-6]\d{2})$|"
        r"^(327[0-5]\d{1})$|"
        r"^(3276[0-7])$"
    )
    
    re.match(p, s)


def constant_str():
    # sequence of ASCII characters not including double quote or newline
    re.match(r"\"[^\"]+\"", s)

def statements():
    pass


