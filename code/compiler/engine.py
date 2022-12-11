from copy import copy
from collections import defaultdict, deque


cls_var_kws = [f"{w}" for w in ("static", "field")]
cls_sub_kws = [f"{w}" for w in ("constructor", "function", "method")]
operators = [f"{w}" for w in ("+", "-", "*", "/", "&", "|", "<", ">", "=")]
unary_symbols = [f"{w}" for w in ("-", "~")]


cnt_while = defaultdict(int)
cnt_if = defaultdict(int)


def print_vm(vm):
    if False:
        print(vm)


class SymbolTable:
    def __init__(self, *kinds, cls_name=None, sub_name=None):
        self.cls_name = cls_name
        self.sub_name = sub_name
        self.table = {}
        self.cnt_kind = {k: 0 for k in kinds}

    def __contains__(self, name):
        return name in self.table

    def add(self, name, type, kind):
        self.table[name] = (type, kind, self.cnt_kind[kind])
        self.cnt_kind[kind] += 1

    def type_of(self, name):
        return self.table[name][0]

    def kind_of(self, name):
        return self.table[name][1]

    def index_of(self, name):
        return self.table[name][2]

    def var_count(self, kind):
        if kind == "argument":
            return self.cnt_kind[kind] - 1
        return self.cnt_kind[kind]


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

    cls_symbols = SymbolTable("static", "field", cls_name=cls_name)

    pop_or_raise(tokens, "{")

    while tokens[0] in cls_var_kws:
        vm.extend(block__class_var_dec(tokens))

    while tokens[0] in cls_sub_kws:
        vm.extend(block__sub_dec(tokens, cls_symbols))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__class_var_dec(tokens):
    vm = []
    pop_or_raise(tokens, cls_var_kws)

    vm.append(__type(tokens))
    vm.append(__identifier(tokens))
    while tokens[0] == ",":
        vm.append(tokens.popleft())
        vm.append(__identifier(tokens))

    pop_or_raise(tokens, ";")
    print_vm(vm)
    return vm


def block__sub_dec(tokens, cls_symbols: SymbolTable):
    vm = []
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
        sub_symbols.add("this", "argument")

    pop_or_raise(tokens, "(")
    param_list = block__param_list(tokens, sub_symbols)
    pop_or_raise(tokens, ")")
    sub_body = block__sub_body(tokens, sub_symbols)

    n_locals = sub_symbols.var_count("local")
    vm.append(
        f"function {cls_symbols.cls_name}.{sub_name} {n_locals}"
    )

    if sub_kind == "constructor":
        n_args = sub_symbols.var_count("local")

        ## allocate memory:
        # push constant n_args  // number of words to allocate on heap
        # call Memory.alloc 1

        ## init field vars
        # pop pointer 0  // set THIS to object base address
        # for i in range(len(n_args)):
        #    push argument i
        #    push this i

        ## do stuff with static var
        # push/pop static 0

        ## return this
        # push pointer 0
        pass

    if sub_kind == "function":
        vm.extend(param_list)
        vm.extend(sub_body)

    if sub_kind == "method":
        vm.append("push argument 0")
        vm.append("pop pointer 0")
        pass

    if sub_type == "void":
        vm.insert(-1, "push constant 0")

    vm.append("")

    print_vm(vm)
    print(sub_symbols.table)
    return vm


def block__param_list(tokens, sub_symbols: SymbolTable):
    if tokens[0] == ")":
        return []

    vm = []
    var_type = tokens.popleft()  # keyword var_type
    var_name = tokens.popleft()  # identifier var_name
    sub_symbols.add(var_name, var_type, "argument")
    while tokens[0] == ",":
        tokens.popleft()  # symbol ,
        var_type = tokens.popleft()  # keyword var_type
        var_name = tokens.popleft()  # identifier var_name
        sub_symbols.add(var_name, var_type, "argument")

    print_vm(vm)
    return vm


def block__sub_body(tokens, sub_symbols: SymbolTable):
    vm = []
    pop_or_raise(tokens, "{")

    while tokens[0] == "var":
        vm.extend(block__var_dec(tokens, sub_symbols))
    vm.extend(block__statements(tokens, sub_symbols))

    pop_or_raise(tokens, "}")
    print_vm(vm)
    return vm


def block__var_dec(tokens, sub_symbols: SymbolTable):
    vm = []
    tokens.popleft()  # keyword var

    var_type = tokens.popleft()  # keyword var_type
    var_name = tokens.popleft()  # identifier var_name
    sub_symbols.add(var_name, var_type, "local")
    while tokens[0] == ",":
        tokens.popleft()  # symbol ,
        var_name = tokens.popleft()  # identifier var_name
        sub_symbols.add(var_name, var_type, "local")

    pop_or_raise(tokens, ";")
    print_vm(vm)
    return vm


def block__statements(tokens, sub_symbols: SymbolTable):
    vm = []
    while True:
        match tokens[0]:
            case "while":
                vm.extend(block__while(tokens, sub_symbols))
            case "if":
                vm.extend(block__if(tokens, sub_symbols))
            case "return":
                vm.extend(block__return(tokens, sub_symbols))
            case "let":
                vm.extend(block__let(tokens, sub_symbols))
            case "do":
                vm.extend(block__do(tokens, sub_symbols))
            case _:
                break
    print_vm(vm)
    return vm


def block__while(tokens, sub_symbols: SymbolTable):
    name = f"{sub_symbols.cls_name}.{sub_symbols.sub_name}"
    cnt_while[name] += 1
    cnt = copy(cnt_while[name])

    pop_or_raise(tokens, "while")
    vm = [f"label {name}.WHILE_START.{cnt}"]

    pop_or_raise(tokens, "(")
    vm.extend(block__expression(tokens, sub_symbols))
    pop_or_raise(tokens, ")")

    # stack -1 -> True, stack 0 -> False
    vm.append("not")
    vm.append(f"if-goto {name}.WHILE_EXIT.{cnt}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, sub_symbols))
    pop_or_raise(tokens, "}")
    
    vm.append(f"goto {name}.WHILE_START.{cnt}")
    vm.append(f"label {name}.WHILE_EXIT.{cnt}")

    print_vm(vm)
    return vm


def block__if(tokens, sub_symbols: SymbolTable):
    name = f"{sub_symbols.cls_name}.{sub_symbols.sub_name}"
    cnt_if[name] += 1
    cnt = copy(cnt_if[name])

    pop_or_raise(tokens, "if")

    pop_or_raise(tokens, "(")
    vm = block__expression(tokens, sub_symbols)
    pop_or_raise(tokens, ")")

    vm.append("not")
    vm.append(f"if-goto {name}.IF_FALSE.{cnt_if[name]}")

    pop_or_raise(tokens, "{")
    vm.extend(block__statements(tokens, sub_symbols))
    pop_or_raise(tokens, "}")

    vm.append(f"goto {name}.IF_END.{cnt}")

    if tokens[0] == "else":
        pop_or_raise(tokens, "else")

        vm.append(f"label {name}.IF_FALSE.{cnt}")

        pop_or_raise(tokens, "{")
        vm.extend(block__statements(tokens, sub_symbols))
        pop_or_raise(tokens, "}")

    vm.append(f"label {name}.IF_END.{cnt}")

    print_vm(vm)
    return vm


def block__return(tokens, sub_symbols: SymbolTable):
    vm = []
    pop_or_raise(tokens, "return")

    if tokens[0] != ";":
        vm.extend(block__expression(tokens, sub_symbols))
    vm.append("return")

    pop_or_raise(tokens, ";")
    print_vm(vm)
    return vm


def block__let(tokens, sub_symbols: SymbolTable):
    vm = []
    tokens.popleft()  # keyword
    var_name = tokens.popleft()

    if tokens[0] == "[":
        pop_or_raise(tokens, "[")
        vm.extend(block__expression(tokens, sub_symbols))
        pop_or_raise(tokens, "]")

    pop_or_raise(tokens, "=")
    vm.extend(block__expression(tokens, sub_symbols))

    kind = sub_symbols.kind_of(var_name)
    index = sub_symbols.index_of(var_name)
    vm.append(f"pop {kind} {index}")

    pop_or_raise(tokens, ";")
    return vm


def block__do(tokens, sub_symbols: SymbolTable):
    pop_or_raise(tokens, "do")
    vm = __sub_call(tokens, sub_symbols)
    pop_or_raise(tokens, ";")

    vm.append("pop temp 0")  # pop void return value

    print_vm(vm)
    return vm


def block__expression(tokens, sub_symbols: SymbolTable):


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


    vm = block__term(tokens, sub_symbols)
    while tokens[0] in operators:
        op = tokens.popleft()  # symbol operator
        vm.extend(block__term(tokens, sub_symbols))
        vm.append(OP_MAP[op])

    return vm


def block__term(tokens, sub_symbols: SymbolTable):
    vm = []

    # negative and negation sign
    if tokens[0] in unary_symbols:
        op = pop_or_raise(tokens, unary_symbols)
        vm.extend(block__term(tokens, sub_symbols))
        vm.append({"-": "neg", "~": "not"}[op])

    # nested expression
    elif tokens[0] == "(":
        tokens.popleft()  # symbol (
        vm.extend(block__expression(tokens, sub_symbols))
        pop_or_raise(tokens, ")")

    # subroutine call
    elif tokens[1] in [".", "("]:
        vm.extend(__sub_call(tokens, sub_symbols))

    # array access
    elif tokens[1] == ["["]:
        vm.append(__identifier(tokens))
        if tokens[0] == "[":
            vm.append(tokens.popleft())
            vm.extend(block__expression(tokens, sub_symbols))
            vm.append(pop_or_raise(tokens, "]"))

    # str-/int-/keyword-constant, var_name
    else:
        value = tokens.popleft()
        if value in sub_symbols.table:
            kind = sub_symbols.kind_of(value)
            index = sub_symbols.index_of(value)
            vm.append(f"push {kind} {index}")
        elif value == "true":
            vm.extend([f"push constant 1", "neg"])
        elif value == "false":
            vm.append(f"push constant 0")
        elif value.isdecimal():
            vm.append(f"push constant {value}")
        else:
            assert False, "Implement String Constants"
            # vm.append(f"push constant {value}")

    print_vm(vm)
    return vm


def block__expr_list(tokens, sub_symbols: SymbolTable):
    if tokens[0] == ")":
        return [], 0

    expression_count = 1
    vm = block__expression(tokens, sub_symbols)

    while tokens[0] == ",":
        tokens.popleft()  # symbol ,
        vm.extend(block__expression(tokens, sub_symbols))
        expression_count += 1

    print_vm(vm)
    return vm, expression_count


def __keyword(tokens):
    return tokens.popleft()


def __identifier(tokens):
    return tokens.popleft()


def __type(tokens):
    return tokens.popleft()


def __sub_call(tokens, sub_symbols: SymbolTable):
    vm = []
    if tokens[1] == ".":
        class_or_var_name = tokens.popleft()  # identifier class_name
        tokens.popleft()  # symbol .
    else:
        class_or_var_name = None

    sub_name = tokens.popleft()  # identifier sub_name

    pop_or_raise(tokens, "(")
    expr_list, n_args = block__expr_list(tokens, sub_symbols)
    vm.extend(expr_list)
    pop_or_raise(tokens, ")")

    if class_or_var_name:
        vm.append(f"call {class_or_var_name}.{sub_name} {n_args}")
    else:
        vm.append(f"call {sub_name} {n_args}")

    # TODO: handle object address return value
    if False:
        vm.append("pop local <obj-var-name-idx>")

    print_vm(vm)
    return vm
