from typing import List

from .functions import func_call


def vm_bootstrap(debug: bool) -> List[str]:
    asm = []
    if debug:
        asm.append("// initalize pointers"),
    asm.extend(
        [
            "@256",
            "D=A",
            "@SP",
            "M=D  // SP=256" if debug else "M=D",
        ]
    )
    asm.extend([
            "@0",
            "D=A",
            "@LCL",
            "D=D-1",
            "M=D  // LCL=-1" if debug else "M=D",
            "@ARG",
            "D=D-1",
            "M=D  // ARG=-2" if debug else "M=D",
            "@THIS",
            "D=D-1",
            "M=D  // THIS=-3" if debug else "M=D",
            "@THAT",
            "D=D-1",
            "M=D  // THAT=-4" if debug else "M=D",
        ]
    )
    # asm.extend([
    #         "@256",
    #         "D=A",
    #         "@LCL",
    #         "M=D  // LCL=-1" if debug else "M=D",
    #         "@256",
    #         "D=A",
    #         "@ARG",
    #         "M=D  // ARG=-2" if debug else "M=D",
    #         "@14000",
    #         "D=A",
    #         "@THIS",
    #         "M=D  // THIS=-3" if debug else "M=D",
    #         "@15000",
    #         "D=A",
    #         "@THAT",
    #         "M=D  // THAT=-4" if debug else "M=D",
    #     ]
    # )
    if debug:
        asm.append("\n// call Sys.init")
    asm.extend(func_call("call Sys.init 0", debug))
    # asm.extend(
    #         [
    #             f"@Sys.init.RETURN_ADDRESS",  # addres to push onto stack
    #             "D=A",  # store return_address in D
    #             "@SP",
    #             "M=M+1",  # increment stack SP
    #             "A=M-1",
    #             "M=D  // push return_address onto stack" if debug else "M=D",
    #         ]
    #     )
    # for addr in ["@LCL", "@ARG", "@THIS", "@THAT"]:
    #     asm.extend(
    #         [
    #             addr,  # addres in pointer
    #             "D=M",  # store address in D
    #             "@SP",
    #             "M=M+1",  # increment stack SP
    #             "A=M-1",
    #             f"M=D  // push *{addr[1:]} onto stack" if debug else "M=D",
    #         ]
    #     )
    # asm.extend(
    #     [
    #         f"@SP",
    #         "D=M",  # store SP value in D
    #         "@LCL",
    #         "M=D  // reposition LCL to *SP" if debug else "M=D",
    #         *["D=D-1" for _ in range(5)],
    #         "@ARG",
    #         "M=D  // reposition ARG to *SP-5" if debug else "M=D",
    #         f"@Sys.init",
    #         "0;JMP",  # goto function
    #         f"(Sys.init.RETURN_ADDRESS)",
    #     ]
    # )
    return asm
