from copy import copy
from collections import defaultdict, deque

from symbol_table import SymbolTable


cls_var_kws = [f"{w}" for w in ("static", "field")]
cls_sub_kws = [f"{w}" for w in ("constructor", "function", "method")]
unary_sym_table = [f"{w}" for w in ("-", "~")]


cnt_while = defaultdict(int)
cnt_if = defaultdict(int)


def print_vm(vm):
    if False:
        print(vm)

print_cls_sym_table = False
print_sub_sym_table = False


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
    vm = []
    pop_or_raise(tokens, "class")
    cls_name = tokens.popleft()  # identifier class_name
    pop_or_raise(tokens, "{")

    sym_table = SymbolTable(cls_name=cls_name)
    while tokens[0] in cls_var_kws:
        sym_table = block__class_var_dec(tokens, sym_table)

    if print_cls_sym_table:
        sym_table.print_cls()

    while tokens[0] in cls_sub_kws:
        vm.extend(block__sub_dec(tokens, sym_table))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__class_var_dec(tokens, sym_table: SymbolTable):
    var_kind = pop_or_raise(tokens, cls_var_kws)
    var_type = tokens.popleft()

    var_name = tokens.popleft()
    sym_table.add(var_name, var_type, var_kind)
    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_name = tokens.popleft()
        sym_table.add(var_name, var_type, var_kind)

    pop_or_raise(tokens, ";")
    return sym_table


def block__sub_dec(tokens, sym_table: SymbolTable):
    sub_kind = pop_or_raise(tokens, cls_sub_kws)
    sub_type = tokens.popleft()
    sub_name = tokens.popleft()

    sym_table.reset_sub_table(sub_name)
    if sub_kind == "method":
        sym_table.add("this", "int", "argument")

    pop_or_raise(tokens, "(")
    block__param_list(tokens, sym_table)
    pop_or_raise(tokens, ")")
    sub_body = block__sub_body(tokens, sym_table)

    n_locals = sym_table.var_count("var")
    vm = [f"function {sym_table.cls_name}.{sub_name} {n_locals}"]

    if sub_kind == "constructor":
        n_fields = sym_table.var_count("field")
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
    if print_sub_sym_table:
        sym_table.print_sub()
    return vm


def block__param_list(tokens, sym_table: SymbolTable):
    if tokens[0] == ")":
        return

    var_type = tokens.popleft()
    var_name = tokens.popleft()
    sym_table.add(var_name, var_type, "argument")
    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_type = tokens.popleft()
        var_name = tokens.popleft()
        sym_table.add(var_name, var_type, "argument")
    return


def block__sub_body(tokens, sym_table: SymbolTable):
    vm = []
    pop_or_raise(tokens, "{")

    while tokens[0] == "var":
        vm.extend(block__var_dec(tokens, sym_table))
    vm.extend(block__statements(tokens, sym_table))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__var_dec(tokens, sym_table: SymbolTable):
    kind = pop_or_raise(tokens, "var")
    var_type = tokens.popleft()
    var_name = tokens.popleft()
    sym_table.add(var_name, var_type, kind)

    while tokens[0] == ",":
        pop_or_raise(tokens, ",")
        var_name = tokens.popleft()
        sym_table.add(var_name, var_type, kind)

    pop_or_raise(tokens, ";")
    return []


def block__statements(tokens, sym_table: SymbolTable):
    vm = []
    while True:
        match tokens[0]:
            case "while":
                vm.extend(block__while(tokens, sym_table))
            case "if":
                vm.extend(block__if(tokens, sym_table))
            case "return":
                vm.extend(block__return(tokens, sym_table))
            case "let":
                vm.extend(block__let(tokens, sym_table))
            case "do":
                vm.extend(block__do(tokens, sym_table))
            case _:
                break
    print_vm(vm)
    return vm


def block__while(tokens, sym_table: SymbolTable):
    name = f"{sym_table.cls_name}.{sym_table.sub_name}"
    cnt_while[name] += 1
    cnt = copy(cnt_while[name])

    pop_or_raise(tokens, "while")
    vm = [f"label {name}.WHILE_START.{cnt}"]

    pop_or_raise(tokens, "(")
    vm.extend(block__expression(tokens, sym_table))
    pop_or_raise(tokens, ")")

    # stack -1 -> True, stack 0 -> False
    vm.append("not")
    vm.append(f"if-goto {name}.WHILE_EXIT.{cnt}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, sym_table))
    pop_or_raise(tokens, "}")

    vm.append(f"goto {name}.WHILE_START.{cnt}")
    vm.append(f"label {name}.WHILE_EXIT.{cnt}")

    print_vm(vm)
    return vm


def block__if(tokens, sym_table: SymbolTable):
    name = f"{sym_table.cls_name}.{sym_table.sub_name}"
    cnt_if[name] += 1
    cnt = copy(cnt_if[name])

    pop_or_raise(tokens, "if")

    pop_or_raise(tokens, "(")
    vm = block__expression(tokens, sym_table)
    pop_or_raise(tokens, ")")

    vm.append("not")
    vm.append(f"if-goto {name}.IF_FALSE.{cnt}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, sym_table))
    pop_or_raise(tokens, "}")

    if tokens[0] == "else":
        vm.append(f"goto {name}.IF_END.{cnt}")
        vm.append(f"label {name}.IF_FALSE.{cnt}")
        pop_or_raise(tokens, "else")
        pop_or_raise(tokens, "{")
        vm.extend(block__statements(tokens, sym_table))
        pop_or_raise(tokens, "}")
        vm.append(f"label {name}.IF_END.{cnt}")
    else:
        vm.append(f"label {name}.IF_FALSE.{cnt}")

    print_vm(vm)
    return vm


def block__return(tokens, sym_table: SymbolTable):
    vm = []
    pop_or_raise(tokens, "return")

    if tokens[0] != ";":
        vm.extend(block__expression(tokens, sym_table))
    vm.append("return")

    pop_or_raise(tokens, ";")
    print_vm(vm)
    return vm


def block__let(tokens, sym_table: SymbolTable):
    pop_or_raise(tokens, "let")

    var_name = tokens.popleft()
    kind = sym_table.kind_of(var_name)
    index = sym_table.index_of(var_name)

    # variable assignment
    if tokens[0] != "[":
        pop_or_raise(tokens, "=")
        vm = block__expression(tokens, sym_table)  # value to assign
        vm.append(f"pop {kind} {index}")  # assign value

    # array assigment
    else:
        resolve_array = [f"push {kind} {index}"]
        pop_or_raise(tokens, "[")
        resolve_array.extend(block__expression(tokens, sym_table))
        pop_or_raise(tokens, "]")
        resolve_array.append("add")
        resolve_array.append("pop pointer 1")
        pop_or_raise(tokens, "=")
        vm = block__expression(tokens, sym_table)  # value to assign
        vm.extend(resolve_array)
        vm.append(f"pop that 0")  # assign value

    pop_or_raise(tokens, ";")
    return vm


def block__do(tokens, sym_table: SymbolTable):
    pop_or_raise(tokens, "do")
    vm = __sub_call(tokens, sym_table)
    pop_or_raise(tokens, ";")

    vm.append("pop temp 0")  # pop void return value

    print_vm(vm)
    return vm


def block__expression(tokens, sym_table: SymbolTable):
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

    vm = block__term(tokens, sym_table)
    while tokens[0] in OP_MAP:
        op = tokens.popleft()  # symbol operator
        vm.extend(block__term(tokens, sym_table))
        vm.append(OP_MAP[op])

    return vm


def block__term(tokens, sym_table: SymbolTable):
    vm = []

    # negative or negation sign
    if tokens[0] in unary_sym_table:
        op = pop_or_raise(tokens, unary_sym_table)
        vm.extend(block__term(tokens, sym_table))
        vm.append({"-": "neg", "~": "not"}[op])

    # nested expression
    elif tokens[0] == "(":
        tokens.popleft()  # symbol (
        vm.extend(block__expression(tokens, sym_table))
        pop_or_raise(tokens, ")")

    # subroutine call
    elif tokens[1] in [".", "("]:
        vm.extend(__sub_call(tokens, sym_table))

    # array access
    elif tokens[1] == "[":
        arr_name = tokens.popleft()
        kind = sym_table.kind_of(arr_name)
        index = sym_table.index_of(arr_name)
        vm.append(f"push {kind} {index}")
        pop_or_raise(tokens, "[")
        vm.extend(block__expression(tokens, sym_table))
        pop_or_raise(tokens, "]")
        vm.append("add")
        vm.append("pop pointer 1")
        vm.append("push that 0")

    # keywords, constants and variables
    else:
        value = tokens.popleft()

        # variable name
        if kind := sym_table.kind_of(value):
            index = sym_table.index_of(value)
            vm.append(f"push {kind} {index}")

        # boolean true
        elif value == "true":
            vm.extend([f"push constant 1", "neg"])

        # boolean false or null
        elif value in ["false", "null"]:
            vm.append(f"push constant 0")

        # integer constant
        elif value.isdecimal():
            vm.append(f"push constant {value}")

        # keyword 'this'
        elif value == "this":
            vm.append(f"push pointer 0")

        # string constant
        elif value[0] == value[-1] == '"':
            value = value.strip('"')
            n = len(value)
            vm.append(f"push constant {n}")
            vm.append(f"call String.new 1")
            for c in value:
                vm.extend([f"push constant {ord(c)}", "call String.appendChar 2"])

        else:
            assert False, "unreachable"

    print_vm(vm)
    return vm


def block__expr_list(tokens, sym_table: SymbolTable):
    if tokens[0] == ")":
        return [], 0

    expression_count = 1
    vm = block__expression(tokens, sym_table)

    while tokens[0] == ",":
        tokens.popleft()  # symbol ,
        vm.extend(block__expression(tokens, sym_table))
        expression_count += 1

    print_vm(vm)
    return vm, expression_count


def __sub_call(tokens, sym_table: SymbolTable):
    vm = []

    if tokens[1] == ".":
        cls_or_var_name = tokens.popleft()  # identifier class_name
        pop_or_raise(tokens, ".")
    else:
        cls_or_var_name = None

    sub_name = tokens.popleft()  # identifier sub_name

    pop_or_raise(tokens, "(")
    expr_list, n_args = block__expr_list(tokens, sym_table)
    pop_or_raise(tokens, ")")

    kind = sym_table.kind_of(cls_or_var_name)

    # Method call from local Class (Functions must always be prefixed witht the Class)
    #   let a = function(args);
    if cls_or_var_name is None:
        # Calling method of current class
        vm.append("push pointer 0")
        vm.extend(expr_list)
        vm.append(f"call {sym_table.cls_name}.{sub_name} {n_args+1}")

    # Constructor or Function call from another Class - no additional arguments needed
    #   let a = Class.new(args)
    #   let a = Class.function(args)
    elif kind is None:
        vm.extend(expr_list)
        vm.append(f"call {cls_or_var_name}.{sub_name} {n_args}")

    # Method call on Object
    #   do object.method(args)
    else:
        type = sym_table.type_of(cls_or_var_name)
        index = sym_table.index_of(cls_or_var_name)
        vm.append(f"push {kind} {index}")
        vm.extend(expr_list)
        vm.append(f"call {type}.{sub_name} {n_args+1}")

    print_vm(vm)
    return vm
