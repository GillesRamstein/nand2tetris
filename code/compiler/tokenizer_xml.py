import re


def tokenize_xml(jack_lines):
    return label_tokens(separate_tokens(jack_lines))


def separate_tokens(jack_lines):
    p = re.compile(
        r"(?<={)|(?={)|"
        r"(?<=})|(?=})|"
        r"(?<=\()|(?=\()|"
        r"(?<=\))|(?=\))|"
        r"(?<=\[)|(?=\[)|"
        r"(?<=])|(?=])|"
        r"(?<=\.)|(?=\.)|"
        r"(?<=,)|(?=,)|"
        r"(?<=;)|(?=;)|"
        r"(?<=\+)|(?=\+)|"
        r"(?<=-)|(?=-)|"
        r"(?<=\*)|(?=\*)|"
        r"(?<=\/)|(?=\/)|"
        r"(?<=&)|(?=&)|"
        r"(?<=\|)|(?=\|)|"
        r"(?<=<)|(?=<)|"
        r"(?<=>)|(?=>)|"
        r"(?<==)|(?==)|"
        r"(?<=~)|(?=~)"
    )
    tokens = []
    for line in jack_lines:
        if '"' in line:
            tokens.extend(split_str_constants(line, p))
        else:
            tokens.extend(split_string(line, p))
    return tokens


def split_string(string, p):
    tokens = []
    for almost_tokens in re.split(p, string):
        almost_tokens = almost_tokens.strip()
        if not almost_tokens:
            # remove empty strings
            continue
        if almost_tokens.startswith('"'):
            # handle string constants
            tokens.append(almost_tokens)
            continue
        if " " not in almost_tokens:
            # contains no spaces -> is a token
            tokens.append(almost_tokens)
            continue
        # split by spaces -> tokens
        tokens.extend(almost_tokens.split())
    return tokens


def split_str_constants(line, p):
    """Split string constant tokens"""
    tokens = []
    cnt = 1
    if line[0] == '"':
        while '"' in line:
            s, line = line.split('"', 1)
            if cnt % 1 == 0:
                tokens.append(s)
            else:
                tokens.extend(split_string(s, p))
            cnt += 1
        if cnt % 1 == 0:
            tokens.append(line)
        else:
            tokens.extend(split_string(line, p))
    else:
        while '"' in line:
            s, line = line.split('"', 1)
            if cnt % 2 == 0:
                tokens.append(s)
            else:
                tokens.extend(split_string(s, p))
            cnt += 1
        if cnt % 2 == 0:
            tokens.append(line)
        else:
            tokens.extend(split_string(line, p))
    return tokens


KEYWORDS = [
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


SYMBOLS = [
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


def label_tokens(tokens):
    xml_tokens = []
    for tk in tokens:

        if tk in KEYWORDS:
            xml_tokens.append(xml_token(tk, "keyword"))
            continue

        if tk in SYMBOLS:
            if tk == "<":
                tk = "&lt;"
            if tk == ">":
                tk = "&gt;"
            if tk == "&":
                tk = "&amp;"
            if tk == '"':
                tk = "&quot;"
            xml_tokens.append(xml_token(tk, "symbol"))
            continue

        if tk.isdecimal() and (0 <= int(tk) <= 32767):
            xml_tokens.append(xml_token(tk, "integerConstant"))
            continue

        if tk.startswith('"'):
            print(tk)
            xml_tokens.append(xml_token(tk.strip('"'), "stringConstant"))
            continue

        xml_tokens.append(xml_token(tk, "identifier"))

    return xml_tokens


def xml_token(tk, name):
    return f"<{name}> {tk} </{name}>"