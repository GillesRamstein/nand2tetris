from argparse import ArgumentParser
from pathlib import Path

from in_out import read_jack_file, remove_comments, write_output
from tokenizer import tokenize
from engine import engine
from parser_xml import parse_to_xml


def main(jack_files, write_xml):
    for jack_file in jack_files:
        print(f"Compiling {jack_file.name}")
        compile_file(jack_file, write_xml)


def compile_file(jack_file, write_xml):
    jack = read_jack_file(jack_file)
    jack_clean = remove_comments(jack)
    tokens = tokenize(jack_clean)

    if write_xml:
        xml = parse_to_xml(tokens)
        write_output(xml, jack_file.with_suffix(".new.xml"))

    vm = engine(tokens)
    write_output(vm, jack_file.with_suffix(".new.vm"))


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
