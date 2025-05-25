import argparse
import os

from tokenizer import Tokenizer
from compilation_engine import CompilationEngine

class JackAnalyzer:
    def __init__(self):
        pass

    def analyze(self, path, compile, generate_symbol_table):
        if not compile and generate_symbol_table:
            raise ValueError("Invalid argument combination")

        if os.path.isfile(path):
            self.analyze_single_file(path, compile, generate_symbol_table)

        elif os.path.isdir(path):
            for fn in os.listdir(path):
                if not fn.endswith(".jack"):
                    continue
                full_path = os.path.join(path, fn)
                self.analyze_single_file(full_path, compile, generate_symbol_table)
        else:
            raise ValueError("Unknown path type")
        
        print("Done")
        
    def analyze_single_file(self, path, compile, generate_symbol_table):
        with open(path, "r") as f:
            lines = f.readlines()
        print(f"Read {path}")

        head, tail = os.path.split(path)
        if not tail:
            raise ValueError

        assert tail.endswith(".jack")
        fn = tail.split(".jack")[0]
        save_dir = os.path.join(head, "output")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if compile:
            if generate_symbol_table:
                out_path = os.path.join(save_dir, f"{fn}Symbols.xml")
            else:
                out_path = os.path.join(save_dir, f"{fn}.xml")
        else:
            out_path = os.path.join(save_dir, f"{fn}T.xml")

        print("Starting tokenization")
        tokenizer = Tokenizer()
        output_tokens = tokenizer.tokenize(lines)
        print("Finished tokenization")

        if compile:
            print("Starting compilation")
            engine = CompilationEngine(output_tokens, generate_symbol_table)
            engine.compile_class()
            output_lines = engine.output_lines + [""]
            print("Finished compilation")
        else:
            print("Creating token output lines")
            output_lines = self.get_output_tokenization(output_tokens)
            print("Finished creating token output lines")

        with open(out_path, "w") as f:
            f.writelines("\n".join(output_lines))

        print(f"Output written to {out_path}")

    def get_output_tokenization(self, output_tokens):
        output_lines = ["<tokens>"]          
        for token in output_tokens:
            line = token.get_line()
            output_lines.append(line)

        output_lines.append("</tokens>")
        output_lines.append("")

        return output_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--no_compile", dest="compile", action='store_false', default=True)
    parser.add_argument("--no_symbol_table", dest="generate_symbol_table", action='store_false', default=True)
    args = parser.parse_args()
    jack_analyzer = JackAnalyzer()
    jack_analyzer.analyze(args.path, args.compile, args.generate_symbol_table)
