import argparse
import os

KEYWORD = "keyword"
SYMBOL = "symbol"
STRING_CONSTANT = "stringConstant"
INTEGER_CONSTANT = "integerConstant"
IDENTIFIER = "identifier"

KEYWORDS = [
    'class',
    'constructor', 
    'function',
    'method', 
    'field', 
    'static', 
    'var', 
    'int',
    'char',
    'boolean',
    'void',
    'true', 
    'false',
    'null', 
    'this', 
    'let', 
    'do', 
    'if', 
    'else',
    'while', 
    'return',
]

SYMBOLS = [
    '{', 
    '}', 
    '(', 
    ')', 
    '[', 
    ']', 
    '.', 
    ',', 
    ';', 
    '+', 
    '-', 
    '*',
    '/', 
    '&',
    '|', 
    ',', 
    '<', 
    '>', 
    '=', 
    '~',
]

ESCAPED_SYMBOLS = {
    '<': "&lt;",
    '>': "&gt;",
    '"': "&quot;",
    '&': "&amp;",
}

class Tokenizer():
    def __init__(self):
        pass
    
    @staticmethod
    def get_token_type(token):
        print(f"Token: {token}")
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
    
    @staticmethod
    def get_line(token, token_type):
        if token_type == STRING_CONSTANT:
            line =  f"<{token_type}> {token[1:-1]} </{token_type}>"
        elif token in ESCAPED_SYMBOLS:
            line =  f"<{token_type}> {ESCAPED_SYMBOLS[token]} </{token_type}>"
        else:
            line =  f"<{token_type}> {token} </{token_type}>"
        print(line)
        return line

    def tokenize(self, lines):
        otuput_lines = ["<tokens>"]
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
                        otuput_lines.append(self.get_line(current_token, STRING_CONSTANT))
                        current_token = ""
                elif char in SYMBOLS:
                    if current_token:
                        token_type = self.get_token_type(current_token)
                        otuput_lines.append(self.get_line(current_token, token_type))
                    otuput_lines.append(self.get_line(char, SYMBOL))
                    current_token = ""
                elif char == " ":
                    if current_token:
                        token_type = self.get_token_type(current_token)
                        otuput_lines.append(self.get_line(current_token, token_type))
                    current_token = ""
                else:
                    current_token += char

        otuput_lines.append("</tokens>")
        otuput_lines.append("")
        return otuput_lines


def main(path):
    if not os.path.isfile(path):
        raise ValueError("Unknown path type")
    
    with open(path, "r") as f:
        lines = f.readlines()
    print(f"Read {path}")

    head, tail = os.path.split(path)
    if not tail:
        raise ValueError

    assert tail.endswith(".jack")
    fn = tail.split(".jack")[0]
    save_dir = os.path.join(head, "output")
    out_path = os.path.join(save_dir, f"{fn}T.xml")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    tokenizer = Tokenizer()
    output_lines = tokenizer.tokenize(lines)

    with open(out_path, "w") as f:
        f.writelines("\n".join(output_lines))

    print(f"Output written to {out_path}")
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    main(args.path)
