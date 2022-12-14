class SymbolTable:
    def __init__(self, cls_name):
        self.cls_name = cls_name
        self.sub_name = None
        self.cls_table = {}
        self.sub_table = None
        self.cnt_cls_kinds = {k: 0 for k in ["field", "static"]}
        self.cnt_sub_kinds = None

    def add(self, name, type, kind):
        if kind in ["field", "static"]:
            self.cls_table[name] = (kind, self.cnt_cls_kinds[kind], type)
            self.cnt_cls_kinds[kind] += 1
        if kind in ["argument", "var"]:
            self.sub_table[name] = (kind, self.cnt_sub_kinds[kind], type)
            self.cnt_sub_kinds[kind] += 1

    def reset_sub_table(self, sub_name):
        self.sub_name = sub_name
        self.sub_table = {}
        self.cnt_sub_kinds = {k: 0 for k in ["argument", "var"]}

    def kind_of(self, name):
        if name in self.cls_table:
            kind = self.cls_table[name][0]
            return {"field": "this"}.get(kind, kind)
        if name in self.sub_table:
            kind = self.sub_table[name][0]
            return {"var": "local"}.get(kind, kind)
        return None

    def index_of(self, name):
        if name in self.cls_table:
            return self.cls_table[name][1]
        if name in self.sub_table:
            return self.sub_table[name][1]
        return None

    def type_of(self, name):
        if name in self.cls_table:
            return self.cls_table[name][2]
        if name in self.sub_table:
            return self.sub_table[name][2]
        return None

    def var_count(self, kind):
        if kind in ["field", "static"]:
            return self.cnt_cls_kinds[kind]
        if kind in ["argument", "var"]:
            return self.cnt_sub_kinds[kind]

    def print_cls(self):
        self._print(f"Class-SymbolTable: {self.cls_name}", self.cls_table)

    def print_sub(self):
        self._print(
            f"Subroutine-SymbolTable: {self.cls_name}.{self.sub_name}",
            self.sub_table,
        )

    def _print(self, name, _table):
        if not _table:
            return f"[{name}]\n  <empty>"

        d = max(map(len, _table.keys()))
        t = list(_table.keys())
        table = (
            "".join([f"{k.rjust(d+2)}: {_table[k]}\n" for k in t[:-1]])
            + f"{t[-1].rjust(d+2)}: {_table[t[-1]]}"
        )
        print(f"[{name}]\n{table}")
