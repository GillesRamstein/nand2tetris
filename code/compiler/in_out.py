from pathlib import Path
from typing import Union, List


def read_jack_file(path: Union[str, Path]) -> List[str]:
    """ Load assembly file line by line into a list of strings.
    """
    with open(path, "r") as f:
        return f.readlines()


def remove_comments(jack):
    multiline_comment = False
    _jack = []
    for l in jack:
        _l = l.split("//")[0].strip()
        if not _l:
            continue
        if _l.startswith("//"):
            continue
        if _l.startswith("/*") and _l.endswith("*/"):
            continue
        if _l.endswith("*/"):
            multiline_comment = False
            continue
        if _l.startswith("/*"):
            multiline_comment = True
            continue
        if multiline_comment:
            continue
        _jack.append(_l)
    return _jack


def write_output(xml: List[str], out_path: Path):
    with open(out_path, "w") as f:
        f.writelines([f"{l}\n" for l in xml])
