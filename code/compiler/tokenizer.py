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
        if '"' in line:
            tokens.extend(split_str_constants(line, p))
        else:
            tokens.extend(split_string(line, p))
    return tokens


def split_string(string, p):
    """Split all non-string constant tokens"""
    tokens = []
    for almost_tokens in re.split(p, string):
        almost_tokens = almost_tokens.strip()
        if not almost_tokens:
            # remove empty strings
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
                tokens.append('"' + s + '"')
            else:
                tokens.extend(split_string(s, p))
            cnt += 1
        if cnt % 1 == 0:
            tokens.append('"' + line + '"')
        else:
            tokens.extend(split_string(line, p))
    else:
        while '"' in line:
            s, line = line.split('"', 1)
            if cnt % 2 == 0:
                tokens.append('"' + s + '"')
            else:
                tokens.extend(split_string(s, p))
            cnt += 1
        if cnt % 2 == 0:
            tokens.append('"' + line + '"')
        else:
            tokens.extend(split_string(line, p))
    return tokens
