from collections import deque


cls_var_kws = [f"<keyword> {w} </keyword>" for w in ("static", "field")]
cls_sub_kws = [f"<keyword> {w} </keyword>" for w in ("constructor", "function", "method")]
operators = [f"<symbol> {w} </symbol>" for w in ('+','-','*','/','&amp;','|','&lt;','&gt;','=')]
unary_symbols = [f"<symbol> {w} </symbol>" for w in ("-", "~")]


def parse_to_xml(tokens):
    tokens = deque(tokens)
    return block__class(tokens)


def block__class(tokens):
    """
    'class' className '{' classVarDec* subroutineDec* '}' 
    """
    xml = ["<class>"]
    xml.append(__keyword(tokens))
    xml.append(__identifier(tokens))

    if not tokens[0] == "<symbol> { </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    while tokens[0] in cls_var_kws:
        xml.extend(block__class_var_dec(tokens))

    while tokens[0] in cls_sub_kws:
        xml.extend(block__sub_dec(tokens))

    if not tokens[0] == "<symbol> } </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</class>")
    return xml


def block__class_var_dec(tokens):
    xml = ["<classVarDec>"]

    if not tokens[0] in cls_var_kws:
        raise ValueError
    xml.append(__keyword(tokens))

    xml.append(__type(tokens))
    xml.append(__identifier(tokens))
    while tokens[0] == "<symbol> , </symbol>":
        xml.append(tokens.popleft())
        xml.append(__identifier(tokens))

    if not tokens[0] == "<symbol> ; </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</classVarDec>")
    return xml


def block__sub_dec(tokens):
    xml = ["<subroutineDec>"]

    if not tokens[0] in cls_sub_kws:
        raise ValueError
    xml.append(__keyword(tokens))

    xml.append(__type(tokens))
    xml.append(__identifier(tokens))

    if not tokens[0] == "<symbol> ( </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__param_list(tokens))

    if not tokens[0] == "<symbol> ) </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__sub_body(tokens))

    xml.append("</subroutineDec>")
    return xml


def block__param_list(tokens):
    xml = ["<parameterList>"]

    if tokens[0] == "<symbol> ) </symbol>":
        xml.append("</parameterList>")
        return xml

    xml.append(__type(tokens))
    xml.append(__identifier(tokens))
    while tokens[0] == "<symbol> , </symbol>":
        xml.append(tokens.popleft())
        xml.append(__type(tokens))
        xml.append(__identifier(tokens))

    xml.append("</parameterList>")
    return xml


def block__sub_body(tokens):
    xml = ["<subroutineBody>"]

    if not tokens[0] == "<symbol> { </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    while tokens[0] == "<keyword> var </keyword>":
        xml.extend(block__var_dec(tokens))
    xml.extend(block__statements(tokens))

    if not tokens[0] == "<symbol> } </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</subroutineBody>")
    return xml


def block__var_dec(tokens):
    xml = ["<varDec>"]
    xml.append(__keyword(tokens))

    xml.append(__type(tokens))
    xml.append(__identifier(tokens))
    while tokens[0] == "<symbol> , </symbol>":
        xml.append(tokens.popleft())
        xml.append(__identifier(tokens))

    if not tokens[0] == "<symbol> ; </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</varDec>")
    return xml


def block__statements(tokens):
    xml = ["<statements>"]
    while True:
        match tokens[0]:
            case "<keyword> while </keyword>":
                xml.extend(block__while(tokens))
            case "<keyword> if </keyword>":
                xml.extend(block__if(tokens))
            case "<keyword> return </keyword>":
                xml.extend(block__return(tokens))
            case "<keyword> let </keyword>":
                xml.extend(block__let(tokens))
            case "<keyword> do </keyword>":
                xml.extend(block__do(tokens))
            case _:
                break
    xml.append("</statements>")
    return xml


def block__while(tokens):
    xml = ["<whileStatement>"]
    xml.append(__keyword(tokens))

    if not tokens[0] == "<symbol> ( </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__expression(tokens))

    if not tokens[0] == "<symbol> ) </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    if not tokens[0] == "<symbol> { </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__statements(tokens))

    if not tokens[0] == "<symbol> } </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</whileStatement>")
    return xml


def block__if(tokens):
    xml = ["<ifStatement>"]
    xml.append(__keyword(tokens))

    if not tokens[0] == "<symbol> ( </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__expression(tokens))

    if not tokens[0] == "<symbol> ) </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    if not tokens[0] == "<symbol> { </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__statements(tokens))

    if not tokens[0] == "<symbol> } </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    if tokens[0] == "<keyword> else </keyword>":
        xml.append(tokens.popleft())

        if not tokens[0] == "<symbol> { </symbol>":
            raise ValueError
        xml.append(tokens.popleft())

        xml.extend(block__statements(tokens))

        if not tokens[0] == "<symbol> } </symbol>":
            raise ValueError
        xml.append(tokens.popleft())

    xml.append("</ifStatement>")
    return xml


def block__return(tokens):
    xml = ["<returnStatement>"]
    xml.append(__keyword(tokens))

    if tokens[0] != "<symbol> ; </symbol>":
        xml.extend(block__expression(tokens))

    if not tokens[0] == "<symbol> ; </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</returnStatement>")
    return xml


def block__let(tokens):
    xml = ["<letStatement>"]
    xml.append(__keyword(tokens))
    xml.append(__identifier(tokens))

    if tokens[0] == "<symbol> [ </symbol>":
        xml.append(tokens.popleft())
        xml.extend(block__expression(tokens))
        if not tokens[0] == "<symbol> ] </symbol>":
            raise ValueError
        xml.append(tokens.popleft())

    if not tokens[0] == "<symbol> = </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__expression(tokens))

    if not tokens[0] == "<symbol> ; </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</letStatement>")
    return xml


def block__do(tokens):
    xml = ["<doStatement>"]
    xml.append(__keyword(tokens))

    xml.extend(__sub_call(tokens))

    if not tokens[0] == "<symbol> ; </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.append("</doStatement>")
    return xml


def block__expression(tokens):
    xml = ["<expression>"]

    xml.extend(block__term(tokens))

    while tokens[0] in operators:
        xml.append(tokens.popleft())
        xml.extend(block__term(tokens))

    xml.append("</expression>")
    return xml


def block__term(tokens):
    xml = ["<term>"]

    if tokens[0] in unary_symbols:
        xml.append(tokens.popleft())
        xml.extend(block__term(tokens))

    elif tokens[0] == "<symbol> ( </symbol>":
        xml.append(tokens.popleft())

        xml.extend(block__expression(tokens))

        if not tokens[0] == "<symbol> ) </symbol>":
            raise ValueError
        xml.append(tokens.popleft())

    elif tokens[1] in ["<symbol> . </symbol>", "<symbol> ( </symbol>"]:
        xml.extend(__sub_call(tokens))

    else:
        xml.append(__identifier(tokens))
        if tokens[0] == "<symbol> [ </symbol>":
            xml.append(tokens.popleft())

            xml.extend(block__expression(tokens))

            if not tokens[0] == "<symbol> ] </symbol>":
                raise ValueError
            xml.append(tokens.popleft())

    xml.append("</term>")
    return xml


def block__expr_list(tokens):
    xml = ["<expressionList>"]
    if tokens[0] == "<symbol> ) </symbol>":
        xml.append("</expressionList>")
        return xml

    xml.extend(block__expression(tokens))

    while tokens[0] == "<symbol> , </symbol>":
        xml.append(tokens.popleft())
        xml.extend(block__expression(tokens))

    xml.append("</expressionList>")
    return xml


def __keyword(tokens):
    return tokens.popleft()


def __identifier(tokens):
    return tokens.popleft()


def __type(tokens):
    return tokens.popleft()


def __sub_call(tokens):
    xml = []
    if tokens[1] == "<symbol> . </symbol>":
        xml.append(__identifier(tokens))
        xml.append(tokens.popleft())

    xml.append(__identifier(tokens))

    if not tokens[0] == "<symbol> ( </symbol>":
        raise ValueError
    xml.append(tokens.popleft())

    xml.extend(block__expr_list(tokens))

    if not tokens[0] == "<symbol> ) </symbol>":
        raise ValueError
    xml.append(tokens.popleft())
    return xml
