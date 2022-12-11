import re


def tokenize(jack_lines):
    return separate_tokens(jack_lines)


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
        for almost_tokens in re.split(p, line):
            almost_tokens = almost_tokens.strip()
            if not almost_tokens:
                # remove empty strings
                continue
            if almost_tokens.startswith('"'):
                # handle string constants
                tokens.append(almost_tokens.strip('"'))
                continue
            if " " not in almost_tokens:
                # contains no spaces -> is a token
                tokens.append(almost_tokens)
                continue
            # split by spaces -> tokens
            tokens.extend(almost_tokens.split())
    return tokens
