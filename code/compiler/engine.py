from copy import copy
from collections import defaultdict, deque

from symbol_table import SymbolTable


cls_var_kws = [f"{w}" for w in ("static", "field")]
cls_sub_kws = [f"{w}" for w in ("constructor", "function", "method")]
unary_symbols = [f"{w}" for w in ("-", "~")]


cnt_while = defaultdict(int)
cnt_if = defaultdict(int)


def print_vm(vm):
    if False:
        print(vm)


def print_sym(tbl):
    if False:
        print(tbl)


def pop_or_raise(tokens, val):
    if isinstance(val, list):
        if tokens[0] not in val:
            raise ValueError
    else:
        if not tokens[0] == val:
            raise ValueError
    return tokens.popleft()


def engine(tokens):
    tokens = deque(tokens)
    return block__class(tokens)


def block__class(tokens):
    """
    'class' className '{' classVarDec* subroutineDec* '}'
    """
    vm = []
    tokens.popleft()  # keyword class
    cls_name = tokens.popleft()  # identifier class_name
    pop_or_raise(tokens, "{")

    cls_symbols = SymbolTable("static", "field", cls_name=cls_name)
    while tokens[0] in cls_var_kws:
        cls_symbols = block__class_var_dec(tokens, cls_symbols)
    print_sym(cls_symbols)

    while tokens[0] in cls_sub_kws:
        vm.extend(block__sub_dec(tokens, cls_symbols))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__class_var_dec(tokens, cls_symbols: SymbolTable):
    var_kind = pop_or_raise(tokens, cls_var_kws)
    var_type = tokens.popleft()

    var_name = tokens.popleft()
    cls_symbols.add(var_name, var_type, var_kind)
    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_name = tokens.popleft()
        cls_symbols.add(var_name, var_type, var_kind)

    pop_or_raise(tokens, ";")
    return cls_symbols


def block__sub_dec(tokens, cls_symbols: SymbolTable):
    sub_kind = pop_or_raise(tokens, cls_sub_kws)
    sub_type = tokens.popleft()
    sub_name = tokens.popleft()

    sub_symbols: SymbolTable = SymbolTable(
        "argument",
        "local",
        cls_name=cls_symbols.cls_name,
        sub_name=sub_name,
    )
    if sub_kind == "method":
        sub_symbols.add("this", "int", "argument")

    pop_or_raise(tokens, "(")
    block__param_list(tokens, sub_symbols)
    pop_or_raise(tokens, ")")
    sub_body = block__sub_body(tokens, cls_symbols, sub_symbols)

    n_locals = sub_symbols.var_count("local")
    vm = [f"function {cls_symbols.cls_name}.{sub_name} {n_locals}"]

    if sub_kind == "constructor":
        n_fields = cls_symbols.var_count("field")
        # allocate memory:
        vm.append(f"push constant {n_fields}")  # number of words to allocate on heap
        vm.append("call Memory.alloc 1")
        # set THIS to object base address
        if n_fields:
            vm.append("pop pointer 0")

    if sub_kind == "method":
        vm.append("push argument 0")
        vm.append("pop pointer 0")

    vm.extend(sub_body)

    if sub_type == "void":
        # push dummy 0 before return
        vm.insert(-1, "push constant 0")

    print_vm(vm)
    print_sym(sub_symbols)
    return vm


def block__param_list(tokens, sub_symbols: SymbolTable):
    if tokens[0] == ")":
        return

    var_type = tokens.popleft()
    var_name = tokens.popleft()
    sub_symbols.add(var_name, var_type, "argument")
    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_type = tokens.popleft()
        var_name = tokens.popleft()
        sub_symbols.add(var_name, var_type, "argument")
    return


def block__sub_body(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    vm = []
    pop_or_raise(tokens, "{")

    while tokens[0] == "var":
        vm.extend(block__var_dec(tokens, sub_symbols))
    vm.extend(block__statements(tokens, cls_symbols, sub_symbols))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__var_dec(tokens, sub_symbols: SymbolTable):
    tokens.popleft()

    var_type = tokens.popleft()
    var_name = tokens.popleft()
    sub_symbols.add(var_name, var_type, "local")
    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_name = tokens.popleft()
        sub_symbols.add(var_name, var_type, "local")

    pop_or_raise(tokens, ";")
    return []


def block__statements(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    vm = []
    while True:
        match tokens[0]:
            case "while":
                vm.extend(block__while(tokens, cls_symbols, sub_symbols))
            case "if":
                vm.extend(block__if(tokens, cls_symbols, sub_symbols))
            case "return":
                vm.extend(block__return(tokens, cls_symbols, sub_symbols))
            case "let":
                vm.extend(block__let(tokens, cls_symbols, sub_symbols))
            case "do":
                vm.extend(block__do(tokens, cls_symbols, sub_symbols))
            case _:
                break
    print_vm(vm)
    return vm


def block__while(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    name = f"{sub_symbols.cls_name}.{sub_symbols.sub_name}"
    cnt_while[name] += 1
    cnt = copy(cnt_while[name])

    pop_or_raise(tokens, "while")
    vm = [f"label {name}.WHILE_START.{cnt}"]

    pop_or_raise(tokens, "(")
    vm.extend(block__expression(tokens, cls_symbols, sub_symbols))
    pop_or_raise(tokens, ")")

    # stack -1 -> True, stack 0 -> False
    vm.append("not")
    vm.append(f"if-goto {name}.WHILE_EXIT.{cnt}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, cls_symbols, sub_symbols))
    pop_or_raise(tokens, "}")

    vm.append(f"goto {name}.WHILE_START.{cnt}")
    vm.append(f"label {name}.WHILE_EXIT.{cnt}")

    print_vm(vm)
    return vm


def block__if(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    name = f"{sub_symbols.cls_name}.{sub_symbols.sub_name}"
    cnt_if[name] += 1
    cnt = copy(cnt_if[name])

    pop_or_raise(tokens, "if")

    pop_or_raise(tokens, "(")
    vm = block__expression(tokens, cls_symbols, sub_symbols)
    pop_or_raise(tokens, ")")

    vm.append("not")
    vm.append(f"if-goto {name}.IF_FALSE.{cnt}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, cls_symbols, sub_symbols))
    pop_or_raise(tokens, "}")

    if tokens[0] == "else":
        vm.append(f"goto {name}.IF_END.{cnt}")
        vm.append(f"label {name}.IF_FALSE.{cnt}")
        pop_or_raise(tokens, "else")
        pop_or_raise(tokens, "{")
        vm.extend(block__statements(tokens, cls_symbols, sub_symbols))
        pop_or_raise(tokens, "}")
        vm.append(f"label {name}.IF_END.{cnt}")
    else:
        vm.append(f"label {name}.IF_FALSE.{cnt}")

    print_vm(vm)
    return vm


def block__return(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    vm = []
    pop_or_raise(tokens, "return")

    if tokens[0] != ";":
        vm.extend(block__expression(tokens, cls_symbols, sub_symbols))
    vm.append("return")

    pop_or_raise(tokens, ";")
    print_vm(vm)
    return vm


def block__let(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    tokens.popleft()  # keyword
    var_name = tokens.popleft()
    array = None

    # array assigment
    if tokens[0] == "[":
        if var_name in sub_symbols:
            kind = sub_symbols.kind_of(var_name)
            index = sub_symbols.index_of(var_name)
        if var_name in cls_symbols:
            kind = cls_symbols.kind_of(var_name)
            index = cls_symbols.index_of(var_name)
        array = [f"push {kind} {index}"]
        pop_or_raise(tokens, "[")
        array.extend(block__expression(tokens, cls_symbols, sub_symbols))
        pop_or_raise(tokens, "]")
        array.append("add")
        array.append("pop pointer 1")

    pop_or_raise(tokens, "=")
    # value to assign
    vm = block__expression(tokens, cls_symbols, sub_symbols)

    if var_name in cls_symbols:
        kind = cls_symbols.kind_of(var_name)
        index = cls_symbols.index_of(var_name)
        kind = "this" if kind == "field" else kind

    if var_name in sub_symbols:
        kind = sub_symbols.kind_of(var_name)
        index = sub_symbols.index_of(var_name)

    if array:
        kind = "that"
        index = 0
        vm.extend(array)

    # assign value
    vm.append(f"pop {kind} {index}")

    pop_or_raise(tokens, ";")
    return vm


def block__do(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    pop_or_raise(tokens, "do")
    vm = __sub_call(tokens, cls_symbols, sub_symbols)
    pop_or_raise(tokens, ";")

    vm.append("pop temp 0")  # pop void return value

    print_vm(vm)
    return vm


def block__expression(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    OP_MAP = {
        "+": "add",
        "-": "sub",
        "*": "call Math.multiply 2",
        "/": "call Math.divide 2",
        ">": "gt",
        "<": "lt",
        "=": "eq",
        "|": "or",
        "&": "and",
    }

    vm = block__term(tokens, cls_symbols, sub_symbols)
    while tokens[0] in OP_MAP:
        op = tokens.popleft()  # symbol operator
        vm.extend(block__term(tokens, cls_symbols, sub_symbols))
        vm.append(OP_MAP[op])

    return vm


def block__term(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    vm = []
    # negative and negation sign
    if tokens[0] in unary_symbols:
        op = pop_or_raise(tokens, unary_symbols)
        vm.extend(block__term(tokens, cls_symbols, sub_symbols))
        vm.append({"-": "neg", "~": "not"}[op])

    # nested expression
    elif tokens[0] == "(":
        tokens.popleft()  # symbol (
        vm.extend(block__expression(tokens, cls_symbols, sub_symbols))
        pop_or_raise(tokens, ")")

    # subroutine call
    elif tokens[1] in [".", "("]:
        vm.extend(__sub_call(tokens, cls_symbols, sub_symbols))

    # array access
    elif tokens[1] == "[":
        arr_name = tokens.popleft()
        if arr_name in sub_symbols:
            kind = sub_symbols.kind_of(arr_name)
            index = sub_symbols.index_of(arr_name)
        if arr_name in cls_symbols:
            kind = cls_symbols.kind_of(arr_name)
            index = cls_symbols.index_of(arr_name)
        vm.append(f"push {kind} {index}")
        pop_or_raise(tokens, "[")
        vm.extend(block__expression(tokens, cls_symbols, sub_symbols))
        pop_or_raise(tokens, "]")
        vm.append("add")
        vm.append("pop pointer 1")
        vm.append("push that 0")

    # str-/int-/keyword-constant, var_name
    else:
        value = tokens.popleft()
        if value in cls_symbols.table:
            kind = cls_symbols.kind_of(value)
            index = cls_symbols.index_of(value)
            kind = "this" if kind == "field" else kind
            vm.append(f"push {kind} {index}")
        elif value in sub_symbols.table:
            kind = sub_symbols.kind_of(value)
            index = sub_symbols.index_of(value)
            vm.append(f"push {kind} {index}")
        elif value == "true":
            vm.extend([f"push constant 1", "neg"])
        elif value in ["false", "null"]:
            vm.append(f"push constant 0")
        elif value.isdecimal():
            vm.append(f"push constant {value}")
        elif value == "this":
            vm.append(f"push pointer 0")
        else:
            # string constant
            n = len(value)
            vm.append(f"push constant {n}")
            vm.append(f"call String.new 1")
            for c in value:
                vm.extend([f"push constant {ord(c)}", "call String.appendChar 2"])

    print_vm(vm)
    return vm


def block__expr_list(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    if tokens[0] == ")":
        return [], 0

    expression_count = 1
    vm = block__expression(tokens, cls_symbols, sub_symbols)

    while tokens[0] == ",":
        tokens.popleft()  # symbol ,
        vm.extend(block__expression(tokens, cls_symbols, sub_symbols))
        expression_count += 1

    print_vm(vm)
    return vm, expression_count


def __sub_call(tokens, cls_symbols: SymbolTable, sub_symbols: SymbolTable):
    vm = []
    if tokens[1] == ".":
        cls_or_var_name = tokens.popleft()  # identifier class_name
        tokens.popleft()  # symbol .
    else:
        cls_or_var_name = None

    sub_name = tokens.popleft()  # identifier sub_name

    pop_or_raise(tokens, "(")
    expr_list, n_args = block__expr_list(tokens, cls_symbols, sub_symbols)
    pop_or_raise(tokens, ")")

    # Calling constructor or function of a class <cls_name> - no additional arguments needed
    if cls_or_var_name and cls_or_var_name[0].isupper():
        vm.extend(expr_list)
        vm.append(f"call {cls_or_var_name}.{sub_name} {n_args}")

    # Calling method on object <sub_var_name> - prepend object address to arguments
    elif cls_or_var_name and cls_or_var_name in sub_symbols:
        kind = sub_symbols.kind_of(cls_or_var_name)
        type = sub_symbols.type_of(cls_or_var_name)
        index = sub_symbols.index_of(cls_or_var_name)
        vm.append(f"push {kind} {index}")
        vm.extend(expr_list)
        vm.append(f"call {type}.{sub_name} {n_args+1}")

    # Calling method on object <cls_var_name> - prepend object address to arguments
    elif cls_or_var_name and cls_or_var_name in cls_symbols:
        kind = cls_symbols.kind_of(cls_or_var_name)
        type = cls_symbols.type_of(cls_or_var_name)
        index = cls_symbols.index_of(cls_or_var_name)
        kind = "this" if kind == "field" else kind
        vm.append(f"push {kind} {index}")  # pass object as argument 0
        vm.extend(expr_list)
        vm.append(f"call {type}.{sub_name} {n_args+1}")

    # Calling method on current object
    elif not cls_or_var_name:
        # Calling method of current class
        vm.append("push pointer 0")
        vm.extend(expr_list)
        vm.append(f"call {cls_symbols.cls_name}.{sub_name} {n_args+1}")

    else:
        assert False, "Unreachable"

    print_vm(vm)
    return vm
