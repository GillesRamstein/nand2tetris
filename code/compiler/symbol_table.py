class SymbolTable:
    def __init__(self, *kinds, cls_name=None, sub_name=None):
        self.cls_name = cls_name
        self.sub_name = sub_name
        self.table = {}
        self.cnt_kind = {k: 0 for k in kinds}

    def add(self, name, type, kind):
        self.table[name] = (type, kind, self.cnt_kind[kind])
        self.cnt_kind[kind] += 1

    def type_of(self, name):
        return self.table[name][0]

    def kind_of(self, name):
        return self.table[name][1]

    def index_of(self, name):
        return self.table[name][2]

    def var_count(self, kind):
        if kind == "argument":
            return self.cnt_kind[kind] - 1
        return self.cnt_kind[kind]

    def __contains__(self, name):
        return name in self.table

    def __str__(self):
        name = (
            f"Subroutine-SymbolTable: {self.cls_name}.{self.sub_name}"
            if self.sub_name
            else f"Class-SymbolTable: {self.cls_name}"
        )
        if not self.table:
            return f"[{name}]\n  <empty>"

        d = max(map(len, self.table.keys()))
        t = list(self.table.keys())
        table = (
            "".join([f"{k.rjust(d+2)}: {self.table[k]}\n" for k in t[:-1]])
            + f"{t[-1].rjust(d+2)}: {self.table[t[-1]]}"
        )
        return f"[{name}]\n{table}"
