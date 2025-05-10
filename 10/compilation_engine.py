from tokenizer import Token

class CompilationEngine:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current_position = 0
        self.output_lines = []
        self.indentation_level = 0

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
        self.output_lines.append(line)

    def add_closing_tag(self, tag):
        line = f"</{tag}>"
        line = self.add_indentation(line)
        self.output_lines.append(line)

    def add_tags(tag):
        def decorator(func):
            def wrapper(self):
                self.add_opening_tag(tag)
                self.indentation_level += 1
                func(self)
                self.indentation_level -= 1
                self.add_closing_tag(tag)
            return wrapper
        return decorator

    def process_current_token(self):
        assert isinstance(self.current_token, Token)
        line = self.current_token.get_line()
        line = self.add_indentation(line)
        self.output_lines.append(line)
        self.current_position += 1

    def process_symbol(self, name):
        assert self.current_token.is_symbol(name)
        self.process_current_token()
    
    def process_varname(self):
        assert self.current_token.is_identifier
        self.process_current_token()

    def process_class_name(self):
        self.process_keyword("class")

    def process_keyword(self, name):
        assert self.current_token.is_keyword(name)
        self.process_current_token()

    def process_subroutine_name(self):
        assert self.current_token.is_identifier
        self.process_current_token()

    def process_type(self):
        assert self.current_token.is_type
        self.process_current_token()

    @add_tags("class")
    def compile_class(self):
        self.process_class_name()

        assert self.current_token.is_identifier
        self.process_current_token()

        self.process_symbol("{")

        while self.current_token.is_keyword("static") or self.current_token.is_keyword("field"):
            self.compile_class_var_dec()
        
        while self.starting_subroutine_dec():
            self.compile_subroutine_dec()

        self.process_symbol("}")

    @add_tags("classVarDec")
    def compile_class_var_dec(self):
        assert self.current_token.is_keyword("static") or self.current_token.is_keyword("field")
        self.process_current_token()

        self.process_type()
        self.process_varname()

        while self.current_token.is_symbol(",") and self.next_token.is_identifier:
            self.process_current_token()
            self.process_current_token()

        self.process_symbol(";")
    
    @add_tags("subroutineDec")
    def compile_subroutine_dec(self):
        assert self.starting_subroutine_dec()
        self.process_current_token()
        
        assert self.current_token.is_keyword("void") or self.current_token.is_type
        self.process_current_token()

        self.process_subroutine_name()
        self.process_symbol("(")
        self.compile_parameter_list()
        self.process_symbol(")")
        self.compile_subroutine_body()

    @add_tags("parameterList")
    def compile_parameter_list(self):
        if self.current_token.is_type and self.next_token.is_identifier:
            self.process_current_token()
            self.process_current_token()

            while (
                self.current_token.is_symbol(",") 
                and self.next_token.is_type 
                and self.next_next_token.is_identifier
                ):
                self.process_current_token()
                self.process_current_token()
                self.process_current_token()

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
        self.process_type()
        self.process_varname()

        while self.current_token.is_symbol(",") and self.next_token.is_identifier:
            self.process_current_token()
            self.process_current_token()

        self.process_symbol(";")
        
    @add_tags("expression")
    def compile_expression(self):
        self.compile_term()
        while self.current_token.is_binary_op:
            self.process_current_token()
            self.compile_term()

    @add_tags("term")
    def compile_term(self):
        if self.current_token.is_keyword_constant:
            self.process_current_token()
        elif self.current_token.is_string_constant:
            self.process_current_token()
        elif self.current_token.is_integer_constant:
            self.process_current_token()
        elif self.current_token.is_symbol("("):
            self.process_current_token()
            self.compile_expression()
            assert self.current_token.is_symbol(")")
            self.process_current_token()
        elif self.current_token.is_unary_op:
            self.process_current_token()
            self.compile_term()
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
            self.process_varname()
        else:
            raise ValueError(f"Couldn't compile term: {self.current_token.token_name}")
    
    @add_tags("expressionList")
    def compile_expression_list(self):        
        if self.current_token.is_symbol(")"):
            return
        
        self.compile_expression()
        while self.current_token.is_symbol(","):
            self.process_symbol(",")
            self.compile_expression()
    
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
        self.process_varname()

        if self.current_token.is_symbol("["):
            self.process_symbol("[")
            self.compile_expression()
            self.process_symbol("]")

        self.process_symbol("=")
        self.compile_expression()
        self.process_symbol(";")
    
    @add_tags("ifStatement")
    def compile_if_statement(self):
        self.process_keyword("if")
        self.process_symbol("(")
        self.compile_expression()
        self.process_symbol(")")
        self.process_symbol("{")
        self.compile_statements()
        self.process_symbol("}")

        if self.current_token.is_keyword("else"):
            self.process_keyword("else")
            self.process_symbol("{")
            self.compile_statements()
            self.process_symbol("}")

    @add_tags("whileStatement")
    def compile_while_statement(self):
        self.process_keyword("while")
        self.process_symbol("(")
        self.compile_expression()
        self.process_symbol(")")
        self.process_symbol("{")
        self.compile_statements()
        self.process_symbol("}")
    
    @add_tags("doStatement")
    def compile_do_statement(self):
        self.process_keyword("do")

        if self.next_token.is_symbol("."):
            self.process_subroutine_attr()
        else:
            self.process_subroutine_no_attr()

        self.process_symbol(";")

    def process_subroutine_no_attr(self):
        self.process_subroutine_name()
        self.process_symbol("(")
        self.compile_expression_list()
        self.process_symbol(")")

    def process_subroutine_attr(self):
        assert self.current_token.is_identifier
        self.process_current_token()

        self.process_symbol(".")
        self.process_subroutine_name()
        self.process_symbol("(")
        self.compile_expression_list()
        self.process_symbol(")")

    @add_tags("returnStatement")
    def compile_return_statement(self):
        self.process_keyword("return")

        if not self.current_token.is_symbol(";"):
            self.compile_expression()
        
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
