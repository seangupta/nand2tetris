from tokenizer import Token
from definitions import UNARY_OPS_JACK_TO_VM, BINARY_OPS_JACK_TO_VM, KEYWORD_CONSTANTS_JACK_TO_VM

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, kind, data_type, name, declaration):
        assert name not in self.symbols
        assert isinstance(declaration, bool)
        index = self.get_index(kind)
        self.symbols[name] = {"kind": kind, "type": data_type, "index": index, "declaration": declaration}

    def get_index(self, kind):
        return len([v for v in self.symbols.values() if v["kind"] == kind])
    
    def get_num_local_vars(self):
        return len([v for v in self.symbols.values() if v["kind"] == "local"])
    
    def get_num_field_vars(self):
        return len([v for v in self.symbols.values() if v["kind"] == "field"])

class CompilationEngine:
    def __init__(self, tokens: list[Token], generate_vm_code):
        self.tokens = tokens
        self.current_position = 0
        self.xml_output_lines = []
        self.indentation_level = 0
        self.generate_vm_code = generate_vm_code
        self.class_symbol_table = SymbolTable()
        self.method_symbol_table = SymbolTable()
        self.compiled_vm_lines = []
        self.num_labels = 0

    @property
    def current_token(self):
        return self.tokens[self.current_position]
    
    @property
    def next_token(self):
        return self.tokens[self.current_position + 1]
    
    @property
    def next_next_token(self):
        return self.tokens[self.current_position + 2]
    
    def add_indentation(self, line):
        return "  " * self.indentation_level + line
    
    def add_opening_tag(self, tag):
        line = f"<{tag}>"
        line = self.add_indentation(line)
        self.xml_output_lines.append(line)

    def add_closing_tag(self, tag):
        line = f"</{tag}>"
        line = self.add_indentation(line)
        self.xml_output_lines.append(line)

    def add_tags(tag):
        def decorator(func):
            def wrapper(self):
                self.add_opening_tag(tag)
                self.indentation_level += 1
                res = func(self)
                self.indentation_level -= 1
                self.add_closing_tag(tag)
                return res
            return wrapper
        return decorator

    def process_current_token(self, declaration=False, is_classname=False, maybe_classname=False, is_subroutine_name=False, ignore=False):
        assert isinstance(self.current_token, Token)
        symbol = None

        if self.generate_vm_code and self.current_token.is_identifier and not ignore:
            name = self.current_token.token_name

            if is_classname:
                symbol = {"kind": "class"}
            elif is_subroutine_name:
                symbol = {"kind": "subroutine"}
            elif name in self.method_symbol_table.symbols:
                symbol = self.method_symbol_table.symbols[name]
            elif name in self.class_symbol_table.symbols:
                symbol = self.class_symbol_table.symbols[name]
            elif maybe_classname:
                is_classname = True
                symbol = {"kind": "class"}
            else:
                raise ValueError(f"WARNING: Not found in symbol table: {self.current_token}")

            tag = "identifier"
            self.add_opening_tag(tag)
            self.indentation_level += 1
            
            if is_classname or is_subroutine_name:
                info_tags = ["name", "kind", "declaration"]
            else:
                info_tags = ["name", "kind", "type", "index", "declaration"]

            for info_tag in info_tags:
                if info_tag == "name":
                    value = name
                elif info_tag == "declaration":
                    value = declaration
                else:
                    value = symbol[info_tag]

                line = f"<{info_tag}> {value} </{info_tag}>"
                print(line)
                line = self.add_indentation(line)
                self.xml_output_lines.append(line)

            self.indentation_level -= 1
            self.add_closing_tag(tag)
        else:
            line = self.current_token.get_line()
            line = self.add_indentation(line)
            self.xml_output_lines.append(line)

        self.current_position += 1
        return symbol

    def process_symbol(self, name):
        assert self.current_token.is_symbol(name)
        self.process_current_token()
    
    def process_varname(self, declaration=False):
        assert self.current_token.is_identifier
        symbol = self.process_current_token(declaration=declaration)
        return symbol

    def process_class_name(self):
        self.process_keyword("class")

    def process_keyword(self, name):
        assert self.current_token.is_keyword(name)
        self.process_current_token()

    def process_subroutine_name(self, declaration):
        assert self.current_token.is_identifier
        self.process_current_token(is_subroutine_name=True, declaration=declaration)

    def process_type(self):
        assert self.current_token.is_type
        self.process_current_token(ignore=True)

    @add_tags("class")
    def compile_class(self):
        if self.generate_vm_code:
            # Previous symbols are irrelevant
            self.class_symbol_table = SymbolTable()

        self.process_class_name()

        assert self.current_token.is_identifier
        self.current_class_name = self.current_token.token_name
        self.process_current_token(is_classname=True, declaration=True)

        self.process_symbol("{")

        while self.current_token.is_keyword("static") or self.current_token.is_keyword("field"):
            self.compile_class_var_dec()
        
        while self.starting_subroutine_dec():
            self.method_symbol_table = SymbolTable()
            self.compile_subroutine_dec()

        self.process_symbol("}")

    @add_tags("classVarDec")
    def compile_class_var_dec(self):
        assert self.current_token.is_keyword("static") or self.current_token.is_keyword("field")
        kind = self.current_token.token_name
        self.process_current_token()
        
        data_type = self.current_token.token_name
        self.process_type()

        name = self.current_token.token_name
    
        if self.generate_vm_code:
            self.class_symbol_table.add_symbol(kind, data_type, name, True)

        self.process_varname(declaration=True)

        while self.current_token.is_symbol(",") and self.next_token.is_identifier:
            self.process_current_token()

            name = self.current_token.token_name

            if self.generate_vm_code:
                self.class_symbol_table.add_symbol(kind, data_type, name, True)

            self.process_current_token(declaration=True)

        self.process_symbol(";")
    
    @add_tags("subroutineDec")
    def compile_subroutine_dec(self):
        assert self.starting_subroutine_dec()
        subroutine_type = self.current_token.token_name
        self.process_current_token()
        
        assert self.current_token.is_keyword("void") or self.current_token.is_type
        self.process_current_token(ignore=True)

        subroutine_name = self.current_token.token_name
        self.process_subroutine_name(declaration=True)

        if self.generate_vm_code:
            vm_line = "PLACEHOLDER"
            self.compiled_vm_lines.append(vm_line)

            if subroutine_type == "method":
                vm_lines = [
                    "push argument 0",
                    "pop pointer 0"
                ]
                self.compiled_vm_lines.extend(vm_lines)
            elif subroutine_type == "constructor":
                num_field_vars = self.class_symbol_table.get_num_field_vars()
                vm_lines = [
                    f"push constant {num_field_vars}",
                    "call Memory.alloc 1",
                    "pop pointer 0",
                ]
                self.compiled_vm_lines.extend(vm_lines)
            elif subroutine_type == "function":
                pass
            else:
                raise ValueError(f"Unknown subroutine type {subroutine_type}")

        self.process_symbol("(")

        if self.generate_vm_code:
            if subroutine_type == "method":
                self.method_symbol_table.add_symbol("argument", self.current_class_name, "this", False)

        self.compile_parameter_list()
        self.process_symbol(")")
        self.compile_subroutine_body()

        # Only now know number of local vars
        if self.generate_vm_code:
            num_local_vars = self.method_symbol_table.get_num_local_vars()
            vm_line = f"function {self.current_class_name}.{subroutine_name} {num_local_vars}"

            for i, line in enumerate(self.compiled_vm_lines[::-1]):
                if line == "PLACEHOLDER":
                    self.compiled_vm_lines[len(self.compiled_vm_lines) - 1 - i] = vm_line
                    break


    @add_tags("parameterList")
    def compile_parameter_list(self):
        if self.current_token.is_type and self.next_token.is_identifier:
            data_type = self.current_token.token_name
            self.process_current_token()

            name = self.current_token.token_name

            if self.generate_vm_code:
                self.method_symbol_table.add_symbol("argument", data_type, name, True)

            self.process_current_token(declaration=True)

            while (
                self.current_token.is_symbol(",") 
                and self.next_token.is_type 
                and self.next_next_token.is_identifier
                ):
                self.process_current_token()

                data_type = self.current_token.token_name
                self.process_current_token()

                name = self.current_token.token_name
                
                if self.generate_vm_code:
                    self.method_symbol_table.add_symbol("argument", data_type, name, True)

                self.process_current_token(declaration=True)

    @add_tags("subroutineBody")
    def compile_subroutine_body(self):
        self.process_symbol("{")

        while self.current_token.is_keyword("var"):
            self.compile_var_dec()

        self.compile_statements()
        self.process_symbol("}")
    
    @add_tags("varDec")
    def compile_var_dec(self):
        self.process_keyword("var")

        data_type = self.current_token.token_name
        self.process_type()

        name = self.current_token.token_name

        if self.generate_vm_code:
            self.method_symbol_table.add_symbol("local", data_type, name, True)

        self.process_varname(declaration=True)

        while self.current_token.is_symbol(",") and self.next_token.is_identifier:
            self.process_current_token()

            name = self.current_token.token_name
            
            if self.generate_vm_code:
                self.method_symbol_table.add_symbol("local", data_type, name, True)

            self.process_current_token()

        self.process_symbol(";")
        
    @add_tags("expression")
    def compile_expression(self):
        self.compile_term()
        while self.current_token.is_binary_op:
            binary_op = self.current_token.token_name

            self.process_current_token()
            self.compile_term()

            if self.generate_vm_code:
                vm_line = BINARY_OPS_JACK_TO_VM[binary_op]
                self.compiled_vm_lines.append(vm_line)

    @add_tags("term")
    def compile_term(self):
        if self.current_token.is_keyword_constant:
            keyword_constant = self.current_token.token_name
            self.process_current_token()
            if self.generate_vm_code:
                vm_lines = KEYWORD_CONSTANTS_JACK_TO_VM[keyword_constant]
                self.compiled_vm_lines.extend(vm_lines)
        elif self.current_token.is_string_constant:
            if self.generate_vm_code:
                # Exclude leading and ending quotes
                string_constant = self.current_token.token_name[1:-1]
                string_length = len(string_constant)
                vm_lines = [
                    f"push constant {string_length}",
                    "call String.new 1",
                ]
                self.compiled_vm_lines.extend(vm_lines)
                for char in string_constant:
                    vm_lines = [
                        f"push constant {ord(char)}",
                        f"call String.appendChar 2"
                    ]
                    self.compiled_vm_lines.extend(vm_lines)
            self.process_current_token()
        elif self.current_token.is_integer_constant:
            if self.generate_vm_code:
                vm_line = f"push constant {self.current_token.token_name}"
                self.compiled_vm_lines.append(vm_line)
            self.process_current_token()
        elif self.current_token.is_symbol("("):
            self.process_current_token()
            self.compile_expression()
            assert self.current_token.is_symbol(")")
            self.process_current_token()
        elif self.current_token.is_unary_op:
            unary_op = self.current_token.token_name
            self.process_current_token()
            self.compile_term()
            if self.generate_vm_code:
                vm_line = UNARY_OPS_JACK_TO_VM[unary_op]
                self.compiled_vm_lines.append(vm_line)
        elif self.next_token.is_symbol('['):
            self.process_varname()
            self.process_symbol("[")
            self.compile_expression()
            self.process_symbol("]")
        elif self.next_token.is_symbol("("):
            self.process_subroutine_no_attr()
        elif self.next_token.is_symbol("."):
            self.process_subroutine_attr()
        elif self.current_token.is_identifier:
            symbol = self.process_varname()
            if symbol["kind"] == "field":
                vm_line = f"push this {symbol['index']}"
            else:
                vm_line = f"push {symbol['kind']} {symbol['index']}"
            self.compiled_vm_lines.append(vm_line)
        else:
            raise ValueError(f"Couldn't compile term: {self.current_token.token_name}")
    
    @add_tags("expressionList")
    def compile_expression_list(self):
        num_expressions = 0        
        if self.current_token.is_symbol(")"):
            return num_expressions
        
        self.compile_expression()
        num_expressions += 1
        while self.current_token.is_symbol(","):
            self.process_symbol(",")
            self.compile_expression()
            num_expressions += 1

        return num_expressions
    
    def compile_statement(self):
        assert self.starting_statement()
        match self.current_token.token_name:
            case "let":
                self.compile_let_statement()
            case "if":
                self.compile_if_statement()
            case "while":
                self.compile_while_statement()
            case "do":
                self.compile_do_statement()
            case "return":
                self.compile_return_statement()
            case _:
                raise ValueError(f"Invalid statement type: {self.current_token}")
    
    @add_tags("letStatement")
    def compile_let_statement(self):
        self.process_keyword("let")
        symbol = self.process_varname()
        if self.generate_vm_code:
            kind = symbol["kind"]
            if kind == "field":
                kind = "this"

        if self.current_token.is_symbol("["):            
            if self.generate_vm_code:
                vm_line = f"push {kind} {symbol['index']}"
                self.compiled_vm_lines.append(vm_line)
            self.process_symbol("[")
            self.compile_expression()
            self.process_symbol("]")
            if self.generate_vm_code:
                vm_line = "add"
                self.compiled_vm_lines.append(vm_line)
            self.process_symbol("=")
            self.compile_expression()
            self.process_symbol(";")
            if self.generate_vm_code:
                vm_lines = [
                    "pop pointer 1",
                    "push that 0",
                    "pop temp 0",
                    "pop pointer 1",
                    "push temp 0",
                    "pop that 0",
                ]
                self.compiled_vm_lines.extend(vm_lines)
        else:
            self.process_symbol("=")
            self.compile_expression()
            self.process_symbol(";")
            if self.generate_vm_code:
                vm_line = f"pop {kind} {symbol['index']}"
                self.compiled_vm_lines.append(vm_line)
    
    @add_tags("ifStatement")
    def compile_if_statement(self):
        self.process_keyword("if")
        self.process_symbol("(")
        self.compile_expression()
        self.process_symbol(")")

        if self.generate_vm_code:
            label1 = self.get_label()
            vm_lines = [
                "not",
                f"if-goto {label1}"
            ]
            self.compiled_vm_lines.extend(vm_lines)

        self.process_symbol("{")
        self.compile_statements()
        self.process_symbol("}")

        if self.generate_vm_code:
            label2 = self.get_label()
            vm_lines = [
                f"goto {label2}",
                f"label {label1}"
            ]
            self.compiled_vm_lines.extend(vm_lines)

        if self.current_token.is_keyword("else"):
            self.process_keyword("else")
            self.process_symbol("{")
            self.compile_statements()
            self.process_symbol("}")

        if self.generate_vm_code:
            vm_line = f"label {label2}"
            self.compiled_vm_lines.append(vm_line)

    @add_tags("whileStatement")
    def compile_while_statement(self):
        if self.generate_vm_code:
            label1 = self.get_label()
            vm_line = f"label {label1}"
            self.compiled_vm_lines.append(vm_line)

        self.process_keyword("while")
        self.process_symbol("(")
        self.compile_expression()
        self.process_symbol(")")

        if self.generate_vm_code:
            label2 = self.get_label()
            vm_lines = [
                "not",
                f"if-goto {label2}"
            ]
            self.compiled_vm_lines.extend(vm_lines)

        self.process_symbol("{")
        self.compile_statements()
        self.process_symbol("}")

        if self.generate_vm_code:
            vm_lines = [
                f"goto {label1}",
                f"label {label2}"
            ]
            self.compiled_vm_lines.extend(vm_lines)
    
    @add_tags("doStatement")
    def compile_do_statement(self):
        self.process_keyword("do")

        if self.next_token.is_symbol("."):
            self.process_subroutine_attr()
        else:
            self.process_subroutine_no_attr()

        self.process_symbol(";")

        if self.generate_vm_code:
            # Dummy value
            vm_line = "pop temp 0"
            self.compiled_vm_lines.append(vm_line)

    def process_subroutine_no_attr(self):
        subroutine_name = self.current_token.token_name
        self.process_subroutine_name(declaration=False)
        self.process_symbol("(")

        if self.generate_vm_code:
            # calling a method (not function) from own class
            vm_line = KEYWORD_CONSTANTS_JACK_TO_VM["this"]
            self.compiled_vm_lines.append(vm_line)

        num_args = self.compile_expression_list()
        self.process_symbol(")")

        if self.generate_vm_code:
            vm_line = f"call {self.current_class_name}.{subroutine_name} {num_args + 1}"
            self.compiled_vm_lines.append(vm_line)

    def process_subroutine_attr(self):
        assert self.current_token.is_identifier

        prefix = self.current_token.token_name
        self.process_current_token(maybe_classname=True, declaration=False)

        self.process_symbol(".")

        subroutine_name = self.current_token.token_name
        self.process_subroutine_name(declaration=False)
        self.process_symbol("(")
        if self.generate_vm_code:
            symbol = self.method_symbol_table.symbols.get(prefix)
            if symbol is None:
                symbol = self.class_symbol_table.symbols.get(prefix)

            if symbol is None:
                # function or constructor call from another class
                call_line = f"call {prefix}.{subroutine_name} NUM_ARGS"
            else:
                # method call from another class
                kind = symbol["kind"]
                if kind == "field":
                    kind = "this"
                vm_line = f"push {kind} {symbol['index']}"
                self.compiled_vm_lines.append(vm_line)
                call_line = f"call {symbol['type']}.{subroutine_name} NUM_ARGS"

        num_args = self.compile_expression_list()
        self.process_symbol(")")

        if self.generate_vm_code:
            if symbol is not None:
                num_args += 1
            call_line = call_line.replace("NUM_ARGS", str(num_args))
            self.compiled_vm_lines.append(call_line)

    @add_tags("returnStatement")
    def compile_return_statement(self):
        self.process_keyword("return")

        if self.current_token.is_symbol(";"):
            if self.generate_vm_code:
                # Dummy value
                vm_line = "push constant 0"
                self.compiled_vm_lines.append(vm_line)
        else:
            self.compile_expression()

        if self.generate_vm_code:
            vm_line = "return"
            self.compiled_vm_lines.append(vm_line)
        
        self.process_symbol(";")

    @add_tags("statements")
    def compile_statements(self):
        while self.starting_statement():
            self.compile_statement()
    
    def starting_statement(self):
        return (
            self.current_token.is_keyword("let")
            or self.current_token.is_keyword("if")
            or self.current_token.is_keyword("while")
            or self.current_token.is_keyword("do")
            or self.current_token.is_keyword("return")
        )

    def starting_subroutine_dec(self):
        return (
            self.current_token.is_keyword("constructor") 
            or self.current_token.is_keyword("function") 
            or self.current_token.is_keyword("method")
            )
    
    def get_label(self):
        label = f"L{self.num_labels + 1}"
        self.num_labels += 1
        return label
