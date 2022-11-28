from typing import List, Dict


CNTS = {
    "eq": -1,
    "gt": -1,
    "lt": -1,
}


def vm_arithmetics(instr: str, cnts: Dict[str, int]=CNTS) -> List[str]:
    if instr == "add":
        return vm_add()
    if instr == "sub":
        return vm_sub()
    if instr == "neg":
        return vm_neg()
    if instr == "eq":
        return vm_eq(cnts)
    if instr == "gt":
        return vm_gt(cnts)
    if instr == "lt":
        return vm_lt(cnts)
    if instr == "and":
        return vm_and()
    if instr == "or":
        return vm_or()
    if instr == "not":
        return vm_not()
    return []


def vm_add():
    """
    pop y
    pop x
    push x+y
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "M=M+D",    # store x+y inplace of x
        "@SP",
        "M=M-1",    # update stack pointer
    ]

def vm_sub():
    """
    pop y
    pop x
    push x-y
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "M=M-D",    # store x-y inplace of x
        "@SP",
        "M=M-1",    # update stack pointer
    ]


def vm_neg():
    """
    pop x
    push -x
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to x
        "M=-M",     # store -x inplace of x
    ]


def vm_not():
    """
    pop x
    push NOTx
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to x
        "M=!M",      # store NOTx inplace of x
    ]


def vm_and():
    """
    pop y
    pop x
    push xANDy
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "M=M&D",    # store xANDy inplace of x
        "@SP",
        "M=M-1",    # update stack pointer
    ]


def vm_or():
    """
    pop y
    pop x
    push xORy
    """
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "M=M|D",    # store xORy inplace of x
        "D=A+1",
        "@SP",
        "M=M-1",    # update stack pointer
    ]


def vm_eq(cnts: Dict[str, int]):
    """
    pop y
    pop x
    push x==y
    """
    cnts["eq"] += 1
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "D=M-D",    # store x-y in D
        f"@TRUE.EQ.{cnts['eq']}",
        "D;JEQ",    # goto TRUE if y==x
        "D=0",      # store 0 in D (for false)
        f"@END.EQ.{cnts['eq']}",
        "0;JMP",    # goto END
        f"(TRUE.EQ.{cnts['eq']})",
        "D=-1",     # store -1 in D (for true)
        f"(END.EQ.{cnts['eq']})",
        "@SP",
        "M=M-1",    # update stack pointer
        "A=M-1",    # SP-2, points to x
        "M=D",      # store xEQy inplace of x
    ]


def vm_gt(cnts: Dict[str, int]):
    """
    pop y
    pop x
    push x>y
    """
    cnts["gt"] += 1
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "D=M-D",    # store x-y in D
        f"@TRUE.GT.{cnts['gt']}",
        "D;JGT",    # goto TRUE if x>y
        "D=0",      # store 0 in D (for false)
        f"@END.GT.{cnts['gt']}",
        "0;JMP",    # goto END
        f"(TRUE.GT.{cnts['gt']})",
        "D=-1",     # store -1 in D (for true)
        f"(END.GT.{cnts['gt']})",
        "@SP",
        "M=M-1",    # update stack pointer
        "A=M-1",    # SP-2, points to x
        "M=D",      # store xEQy inplace of x
    ]


def vm_lt(cnts: Dict[str, int]):
    """
    pop y
    pop x
    push x<y
    """
    cnts["lt"] += 1
    return [
        "@SP",
        "A=M-1",    # SP-1, points to y
        "D=M",      # store y in D
        "A=A-1",    # SP-2, points to x
        "D=M-D",    # store x-y in D
        f"@TRUE.LT.{cnts['lt']}",
        "D;JLT",    # goto TRUE if x<y
        "D=0",      # store 0 in D (for false)
        f"@END.LT.{cnts['lt']}",
        "0;JMP",    # goto END
        f"(TRUE.LT.{cnts['lt']})",
        "D=-1",     # store -1 in D (for true)
        f"(END.LT.{cnts['lt']})",
        "@SP",
        "M=M-1",    # update stack pointer
        "A=M-1",    # SP-2, points to x
        "M=D",      # store xEQy inplace of x
    ]