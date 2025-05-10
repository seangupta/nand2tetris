from definitions import (
    KEYWORD, SYMBOL, STRING_CONSTANT, INTEGER_CONSTANT, 
    IDENTIFIER, KEYWORDS, SYMBOLS, TOKEN_TYPES, ESCAPED_SYMBOLS, KEYWORD_CONSTANTS
)


class Token:
    def __init__(self, token_name, token_type):
        assert token_type in TOKEN_TYPES
        assert isinstance(token_name, str)

        self.token_name = token_name
        self.token_type = token_type

        print(f"Token: {self.token_name} {self.token_type}")

    @property
    def is_identifier(self):
        return self.token_type == IDENTIFIER
    
    def is_symbol(self, name):
        return self.token_name == name and self.token_type == SYMBOL
    
    def is_keyword(self, name):
        return self.token_name == name and self.token_type == KEYWORD
    
    @property
    def is_keyword_constant(self):
        return self.token_name in KEYWORD_CONSTANTS
    
    @property
    def is_type(self):
        return (
            self.is_keyword("int") 
            or self.is_keyword("char")
            or self.is_keyword("boolean")
            or self.is_identifier
        )
    
    def get_line(self):
        token_name = self.token_name
        token_type = self.token_type

        if token_type == STRING_CONSTANT:
            line =  f"<{token_type}> {token_name[1:-1]} </{token_type}>"
        elif token_name in ESCAPED_SYMBOLS:
            line =  f"<{token_type}> {ESCAPED_SYMBOLS[token_name]} </{token_type}>"
        else:
            line =  f"<{token_type}> {token_name} </{token_type}>"
        print(line)
        return line


class Tokenizer():
    def __init__(self):
        pass
    
    @staticmethod
    def get_token_type(token):
        if token in KEYWORDS:
            return KEYWORD
        elif token in SYMBOLS:
            return SYMBOL
        elif token.isdigit():
            assert 0 <= int(token) <= 32_767
            return INTEGER_CONSTANT
        elif token.startswith('"') and token.endswith('"') and '"' not in token[1:-1] and '\n' not in token[1:-1]:
            return STRING_CONSTANT
        elif not token[0].isdigit() and all(char.isdigit() or char.isalpha() or char == "_" for char in token):
            return IDENTIFIER
        else:
            raise ValueError("Unknown token type")
    
    def tokenize(self, lines):
        output_tokens = []
        in_comment = False

        for line in lines:
            line = line.split("//")[0]
            line = line.strip()
            
            if in_comment:
                if line.endswith("*/"):
                    in_comment = False
                continue

            if line.startswith("/*"):
                if not line.endswith("*/"):
                    in_comment = True
                continue
            
            if not line:
                continue
            
            current_token = ""
            for char in line:
                if current_token.startswith('"'):
                    current_token += char
                    if char == '"':
                        # End of string constant
                        output_tokens.append(Token(current_token, STRING_CONSTANT))
                        current_token = ""
                elif char in SYMBOLS:
                    if current_token:
                        token_type = self.get_token_type(current_token)
                        output_tokens.append(Token(current_token, token_type))
                    output_tokens.append(Token(char, SYMBOL))
                    current_token = ""
                elif char == " ":
                    if current_token:
                        token_type = self.get_token_type(current_token)
                        output_tokens.append(Token(current_token, token_type))
                    current_token = ""
                else:
                    current_token += char

        return output_tokens
