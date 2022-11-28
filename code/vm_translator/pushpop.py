from typing import List


PTRS = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
}


def vm_pushpop(instr: str) -> List[str]:
    if instr.startswith("push"):
        return push(instr)
    if instr.startswith("pop"):
        return pop(instr)
    return []


def push(instr):
    _, seg, index = instr.split(" ")

    # get value from segment memory
    if seg == "constant":
        asm = [
            f"@{index}",
            "D=A",      # store constant in D
        ]
    elif seg == "pointer":
        asm = [
            f"@{3+int(index)}",     # pointer ranges from RAM[3] to RAM[4]
            "D=M",              # store value in D
        ]
    elif seg == "temp":
        asm = [
            f"@{5+int(index)}",     # temp ranges from RAM[5] to RAM[12]
            "D=M",              # store value in D
        ]
    elif seg == "static":
        asm = [
            f"@{16+int(index)}",     # static ranges from RAM[16] to RAM[255]
            "D=M",              # store value in D
        ]
    else:
        seg = PTRS[seg]
        asm = [
            f"@{index}",
            "D=A",              # store index in D
            f"@{seg}",          # get segment pointer
            "A=M",              # segment base address to A
            f"A=A+D",           # offset segment address by index
            "D=M",              # store value in D
        ]

    # push value to stack
    asm.extend(
        [
            "@SP",
            "M=M+1",    # increment stack pointer
            "A=M-1",    # point to top of stack
            "M=D",      # push value onto stack
        ]
    )
    return asm


def pop(instr):
    _, seg, index = instr.split(" ")
    if seg == "pointer":
        asm = [
            "@SP",
            "M=M-1",    # decrement stack pointer
            "A=M",      # point to value on stack
            "D=M",      # store value in D
            f"@{3+int(index)}",
            "M=D",      # store value in RAM[3+index]
        ]
    elif seg == "temp":
        asm = [
            "@SP",
            "M=M-1",    # decrement stack pointer
            "A=M",      # point to value on stack
            "D=M",      # store value in D
            f"@{5+int(index)}",
            "M=D",      # store value in RAM[5+index]
        ]
    elif seg == "static":
        asm = [
            "@SP",
            "M=M-1",    # decrement stack pointer
            "A=M",      # point to value on stack
            "D=M",      # store value in D
            f"@{16+int(index)}",
            "M=D",      # store value in RAM[16+index]
        ]
    else:
        asm = [
            f"@{index}",
            "D=A",              # store index in D
            f"@{PTRS[seg]}",    # get segment pointer
            "A=M",        # segment base address to A
            f"D=D+A",     # offset segment address by index
            "@13",
            "M=D",      # store segment+index address in @13
            "@SP",
            "M=M-1",    # decrement stack pointer
            "A=M",      # point to value on stack
            "D=M",      # store value in D
            "@13",
            "A=M",      # get segment+index address in @13
            "M=D",      # store value in RAM[segment+index]
        ]
    return asm
