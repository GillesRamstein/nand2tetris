
from argparse import ArgumentParser
from pathlib import Path

from in_out import read_jack_file, remove_comments, write_output
from tokenizer import tokenize
from analyzer import analyze


def main(args):
    for jack_file in Path(args.input).glob("*.jack"):
        print(jack_file.stem)
        compile_file(jack_file)


def compile_file(jack_file):
    xml = []
    jack = read_jack_file(jack_file)
    jack_clean = remove_comments(jack)
    tokens = tokenize(jack_clean)
    xml = analyze(tokens)
    write_output(xml, jack_file.with_suffix(".new.xml"))



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input", type=str, help="Path to dir with .jack file(s).")
    args = parser.parse_args()

    main(args)
