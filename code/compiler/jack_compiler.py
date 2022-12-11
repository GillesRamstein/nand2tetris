from argparse import ArgumentParser
from pathlib import Path
from time import time

from engine import engine
from in_out import read_jack_file, remove_comments, write_output
from parser_xml import parse_to_xml
from tokenizer import tokenize
from tokenizer_xml import tokenize_xml


def main(jack_files, write_xml):
    for jack_file in jack_files:
        start = time()
        print(f"Compiling {jack_file.name}")
        compile_file(jack_file, write_xml)
        print(f"Done! ({round(time()-start, 3)}s)\n")


def compile_file(jack_file, write_xml):
    jack = read_jack_file(jack_file)
    jack_clean = remove_comments(jack)

    if write_xml:
        xml = parse_to_xml(tokenize_xml(jack_clean))
        write_output(xml, jack_file.with_suffix(".new.xml"))

    vm = engine(tokenize(jack_clean))
    write_output(vm, jack_file.with_suffix(".vm"))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input", type=str, help="Path to dir with .jack file(s).")
    parser.add_argument(
        "--xml", action="store_true", help="Produce xml from parsed tokens - Project 10"
    )
    args = parser.parse_args()

    if args.input.endswith(".jack"):
        jack_files = [Path(args.input)]
    else:
        jack_files = Path(args.input).glob("*.jack")

    main(jack_files, args.xml)
