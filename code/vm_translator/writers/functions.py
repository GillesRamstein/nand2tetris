import re
from typing import List
from collections import defaultdict


function_name_stack = ["Sys.init"]
return_counter = defaultdict(int)


def vm_functions(instr: str, debug: bool) -> List[str]:
    if instr.startswith("function"):
        return func_declaration(instr, debug)
    if instr.startswith("call"):
        return func_call(instr, debug)
    if instr == "return":
        return func_return(debug)
    return []


def func_declaration(instr: str, debug: bool) -> List[str]:
    """Set label and initialise n local variables to 0"""
    _, function_name, n_local_variables = instr.split(" ")
    validate_name(function_name, instr)
    n_local_variables = int(n_local_variables)

    if debug:
        function_name_stack.append(function_name)

    # set label
    asm = [f"({function_name})"]
    # init n local variables to 0
    for i in range(n_local_variables):
        if i == 0:
            asm.extend(
                [
                    f"@LCL  // init local variables" if debug else "@LCL",
                    "A=M",
                    f"M=0  // init {i+1}/{n_local_variables} local vars to 0"
                    if debug
                    else "M=0",
                ]
            )
        else:
            asm.extend(
                [
                    "A=A+1",
                    f"M=0  // init {i+1}/{n_local_variables} local vars to 0"
                    if debug
                    else "M=0",
                ]
            )
    # increment stack pointer
    if n_local_variables:
        asm.append(
            f"@SP  // inc SP by {n_local_variables} local vars" if debug else "@SP"
        )
        for _ in range(int(n_local_variables)):
            asm.append("M=M+1")
    return asm


def func_call(instr: str, debug: bool) -> List[str]:
    _, function_name, n_arguments = instr.split(" ")
    n_arguments = int(n_arguments)

    return_counter[function_name] += 1

    return_address = f"{function_name}.RETURN_ADDRESS"
    if return_counter[function_name] > 1:
        return_address += f".REC{return_counter[function_name]}"

    validate_name(function_name, instr)
    asm = []
    # push return-address onto stack (1 value)
    asm.extend(
        [
            f"@{return_address}",  # pointer
            "D=A",  # store return_address in D
            "@SP",
            "M=M+1",  # increment stack SP
            "A=M-1",
            "M=D  // push return_address onto stack" if debug else "M=D",
        ]
    )
    # push caller pointers onto stack (4 values)
    for addr in ["@LCL", "@ARG", "@THIS", "@THAT"]:
        asm.extend(
            [
                addr,  # pointer
                "D=M",  # store *pointer address in D
                "@SP",
                "M=M+1",  # increment stack SP
                "A=M-1",
                f"M=D  // push *{addr[1:]} onto stack" if debug else "M=D",
            ]
        )
    asm.extend(
        [
            f"@SP",
            "D=M",  # store SP value in D
            "@LCL",
            "M=D  // reposition LCL to *SP" if debug else "M=D",
            *["D=D-1" for _ in range(n_arguments + 5)],
            "@ARG",
            f"M=D  // reposition ARG to *SP-5-{n_arguments}" if debug else "M=D",
            f"@{function_name}",
            "0;JMP",  # goto function
            f"\n({return_address})" if debug else f"({return_address})",
        ]
    )
    return asm


def func_return(debug: bool) -> List[str]:
    asm = []
    if debug:
        asm.append(f"// (from {function_name_stack.pop()} to {function_name_stack[-1]})")
    asm.extend(
        [
            "@LCL",
            "A=M-1 // LCL-1" if debug else "A=M-1",
            "A=A-1 // LCL-2" if debug else "A=A-1",
            "A=A-1 // LCL-3" if debug else "A=A-1",
            "A=A-1 // LCL-4" if debug else "A=A-1",
            "A=A-1 // LCL-5" if debug else "A=A-1",
            "D=M // return_address from *LCL-5 to D" if debug else "D=M",
            "@13",
            "M=D // store return_address in R13" if debug else "M=D",
            "@SP",
            "A=M-1",
            "D=M  // return_value from *SP-1 to D" if debug else "D=M",
            "@ARG",
            "A=M",
            "M=D  // store return_value in *ARG" if debug else "M=D",
            "D=A",
            "@SP",
            "M=D+1 // *SP = *ARG+1" if debug else "M=D+1",
        ]
    )
    for i, pointer in enumerate(["@THAT", "@THIS", "@ARG", "@LCL"]):
        asm.extend(
            [
                "@LCL",
                f"M=M-1  // endFrame-{i+1}" if debug else "M=M-1",
                "A=M",
                "D=M",
                pointer,
                f"M=D  // restore {pointer[1:]} pointer" if debug else "M=D",
            ]
        )
    asm.extend(
        [
            "@13",
            "A=M // load return_address from R13" if debug else "A=M",
            "0;JMP  // jump to return_address" if debug else "0;JMP",
        ]
    )
    return asm


def validate_name(label: str, instr: str):
    """Function names can only contain letters, number and the
    special characters . and _
    """
    if not re.match(r"[a-zA-Z0-9_:.]", label):
        raise ValueError(f"Illegal label: {instr}")
