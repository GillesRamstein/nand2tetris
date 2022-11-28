"""
nand2tetris vm_translator

https://www.cs.huji.ac.il/course/2002/nand2tet/docs/ch_7_vm_I.pdf


RAM Addresses:
       0-15: Virtual Registers
     16-255: Static Variables
   256-2047: Stack
 2048-16483: Heap
16384-24575: Memory mapped I/O 

Virtual Registers:
    0: SP - Stack Pointer
    1: LCL - Local Segment Base Pointer (Stack)
    2: ARG - Argument Segment Base Pointer (Stack)
    3: THIS - Object Fields Base Pointer (Heap)
    4: THAT - Object Array Base Pointer (Heap)
 5-12: TEMP - Hold the contents of the temp segment 
13-15: Can be used by the VM implementation as general-purpose registers


run with:

python code/vm_translator/vmtranslator.py --vm projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm

"""
from argparse import ArgumentParser
from typing import Union, List, Optional
from pathlib import Path

from arithmetics import vm_arithmetics
from pushpop import vm_pushpop


def vm_translator(vm_file: str, debug: bool = False, out_file: Optional[str] = None):
    asm = []

    # set stack pointer to 256
    if debug:
        asm.append(f"\n// init stack pointer:")
    asm.extend(["@256", "D=A", "@SP", "M=D"])

    # translate line by line
    for line in read_vm_file(vm_file):

        # skip non-instruction lines
        instr = line.split("//")[0].strip()
        if not instr:
            continue

        if debug:
            asm.append(f"\n// {instr}")
        asm.extend(vm_pushpop(instr))
        asm.extend(vm_arithmetics(instr))

    # add endless loop
    if debug:
        asm.append(f"\n// add endless loop on program end:")
    asm.extend(
        [f"@{len([l for l in asm if l and not (l.strip().startswith('//') or l.strip().startswith('('))])}", "0;JMP"]  # )
    )

    write_output(asm, Path(out_file or vm_file).with_suffix(".asm"))


def read_vm_file(path: Union[str, Path]) -> List[str]:
    """Load vm file line by line into a list of strings."""
    with open(path, "r") as f:
        return f.readlines()


def write_output(asm: List[str], out_path: Union[str, Path]):
    """Write asm file to out_path.asm"""
    with open(out_path, "w") as f:
        f.writelines([f"{l}\n" for l in asm])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--vm", nargs="+", type=str, help="path(s) to vm file(s")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="adds vm instruction as comments into the hack code",
    )
    args = parser.parse_args()
    for vm_file in args.vm:
        if vm_file.endswith(".vm"):
            vm_translator(vm_file, args.debug)
        else:
            vm_dir = vm_file
            for vm_file in Path(vm_dir).glob("*.vm"):
                vm_translator(vm_file, args.debug)
