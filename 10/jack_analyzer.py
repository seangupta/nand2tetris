import argparse
import os

from definitions import ESCAPED_SYMBOLS, STRING_CONSTANT
from tokenizer import Tokenizer, Token


class JackAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def get_line(token: Token):
        assert isinstance(token, Token)

        token_name = token.token_name
        token_type = token.token_type

        if token_type == STRING_CONSTANT:
            line =  f"<{token_type}> {token_name[1:-1]} </{token_type}>"
        elif token_name in ESCAPED_SYMBOLS:
            line =  f"<{token_type}> {ESCAPED_SYMBOLS[token_name]} </{token_type}>"
        else:
            line =  f"<{token_type}> {token_name} </{token_type}>"
        print(line)
        return line

    def analyze(self, path):
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
        output_tokens = tokenizer.tokenize(lines)

        output_lines = ["<tokens>"]
        for token in output_tokens:
            line = self.get_line(token)
            output_lines.append(line)

        output_lines.append("</tokens>")
        output_lines.append("")

        with open(out_path, "w") as f:
            f.writelines("\n".join(output_lines))

        print(f"Output written to {out_path}")
        print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    jack_analyzer = JackAnalyzer()
    jack_analyzer.analyze(args.path)
