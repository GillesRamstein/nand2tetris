"""
nand2tetris assembler

run with:

python [../]assembler.py --asm <path-to-asm-file> [--out <path-for-output>]

"""

from argparse import ArgumentParser
from pathlib import Path
from typing import Union, List, Optional


from .constants import SYM, CMP, DST, JMP


variables = {}
labels = {}


def assembler(asm_file: str, out_file: Optional[str] = None):
    asm = read_asm_file(asm_file)
    breakpoint()
    clean_asm = first_parse(asm)
    hack = to_binary(clean_asm)
    write_output(hack, Path(out_file or asm_file).with_suffix(".hack"))


def read_asm_file(path: Union[str, Path]) -> List[str]:
    """ Load assembly file line by line into a list of strings.
    """
    with open(path, "r") as f:
        return f.readlines()


def first_parse(asm: List[str]) -> List[str]:
    """ Remove comments, empty lines and label declarations.
    Add labels to LAB table.
    """
    clean_asm = []
    for line in asm:
        instruction = line.split("//")[0].strip()
        if not instruction:
            continue

        if instruction.startswith("(") and instruction.endswith(")"):
            labels[instruction.strip("()")] = format(len(clean_asm), "b").zfill(16)
        else:
            clean_asm.append(instruction)
    return clean_asm


def to_binary(clean_asm):
    """ Decode the A and C instructions to 16 character binary string.
    """
    hack = []
    for instruction in clean_asm:
        if instruction.startswith("@"):
            hack.append(decode_a_instruction(instruction))
        else:
            hack.append(decode_c_instruction(instruction))
    return hack


def decode_a_instruction(instr: str) -> str:
    instr = instr.lstrip("@")

    # @<number>
    if instr.isnumeric():
        return f"{format(int(instr), 'b').zfill(16)}"

    # @<system-symbol>
    elif instr in SYM:
        return f"{SYM[instr]}"

    # @<label>
    elif instr in labels:
        return f"{labels[instr]}"

    # @<variable>
    elif instr not in variables:
        # VAR table if first occurence
        variables[instr] = format(16 + len(variables), "b").zfill(16)
    return variables[instr]


def decode_c_instruction(instr: str) -> str:

    dst = "0"
    if "=" in instr:
        dst, cmp = instr.split("=")

    jmp = "0"
    if ";" in instr:
        cmp, jmp = instr.split(";")

    return f"111{CMP[cmp]}{DST[dst]}{JMP[jmp]}"


def write_output(hack: List[str], out_path: Union[str, Path]):
    """ Write binary to out_path.hack
    """
    with open(out_path, "w") as f:
        f.writelines([f"{l}\n" for l in hack])


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("--asm", type=str, help="path to asm file")
    parser.add_argument("--out", type=str, help="path for output", required=False)
    args = parser.parse_args()

    assembler(args.asm, args.out)
