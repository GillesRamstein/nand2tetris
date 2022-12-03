import re
from typing import List


def vm_branching(instr: str) -> List[str]:
    if instr.startswith("label"):
        return label(instr)
    if instr.startswith("goto"):
        return goto(instr)
    if instr.startswith("if-goto"):
        return ifgoto(instr)
    return []


def label(instr: str) -> List[str]:
    _, label = instr.split(" ")
    validate_label(label, instr)
    return [
        f"({label})",
    ]


def goto(instr: str) -> List[str]:
    _, label = instr.split(" ")
    validate_label(label, instr)
    return [
        f"@{label}",
        "0;JMP",
    ]


def ifgoto(instr: str) -> List[str]:
    _, label = instr.split(" ")
    validate_label(label, instr)
    return [
        "@SP",
        "M=M-1",  # decrement stack pointer
        "A=M",  # dereference pointer
        "D=M",  # store stacks topmost value in D
        f"@{label}",
        "D;JNE",  # jump to label of value in D unequal zero
    ]


def validate_label(label: str, instr: str):
    """Labels can only contain letters, number and the special
    characters : . and _
    """
    if not re.match(r"[a-zA-Z0-9_:.]", label):
        raise ValueError(f"Illegal label: {instr}")
