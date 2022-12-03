"""
nand2tetris vm_translator

https://www.cs.huji.ac.il/course/2002/nand2tet/docs/ch_7_vm_I.pdf


python ../vm_translator/vmtranslator.py <dir-/file-path> [--debug]

"""
from argparse import ArgumentParser
from typing import Union, List
from pathlib import Path

from writers.arithmetics import vm_arithmetics
from writers.bootstrap import vm_bootstrap
from writers.branching import vm_branching
from writers.functions import vm_functions
from writers.pushpop import vm_pushpop


def vm_translator(input: str, debug: bool):
    """Read single or multiple files files, translate to asm,
    and write a single file back to disk.
    """

    # add bootstrap code
    asm = vm_bootstrap(debug)

    # translate single file
    if input.endswith(".vm"):
        out_path = Path(input).with_suffix(".asm")
        asm.extend(translate_vm_file(input, debug))
    # translate and append all files in a directory
    else:
        out_path = Path(input, Path(input).name).with_suffix(".asm")
        for vm_file in Path(input).glob("*.vm"):
            asm.extend(translate_vm_file(vm_file, debug))

    # add clean asm line numbers
    asm_with_line_numbers = []
    counter = 0
    for line in asm:
        if line and not (line.strip().startswith("//") or line.strip().startswith("(")): #)
            if "//" in line:
                instr, comment = line.split("//")
                line = instr.ljust(18) + f"  // ({counter}) {comment}"
            else:
                line = line.ljust(18) + f"  // ({counter})"
            counter += 1
        asm_with_line_numbers.append(line)

    write_output(asm_with_line_numbers, out_path)


def translate_vm_file(vm_file: str, debug: bool = False) -> List[str]:
    asm = []

    # translate line by line
    for line in read_vm_file(vm_file):

        # skip non-instruction lines
        instr = line.split("//")[0].strip()
        if not instr:
            continue

        if debug:
            asm.append(f"\n// {instr}")
        asm.extend(vm_arithmetics(instr))
        asm.extend(vm_branching(instr))
        asm.extend(vm_functions(instr, debug))
        asm.extend(vm_pushpop(instr, debug))

    return asm


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
    parser.add_argument("input", type=str, help="path to vm file or dir")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="adds vm instruction as comments into the hack code",
    )
    args = parser.parse_args()
    vm_translator(args.input, args.debug)
