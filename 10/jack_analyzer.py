import argparse
import os

from tokenizer import Tokenizer
from compilation_engine import CompilationEngine

class JackAnalyzer:
    def __init__(self):
        pass

    def analyze(self, path, compile):
        if os.path.isfile(path):
            self.analyze_single_file(path, compile)

        elif os.path.isdir(path):
            for fn in os.listdir(path):
                if not fn.endswith(".jack"):
                    continue
                full_path = os.path.join(path, fn)
                self.analyze_single_file(full_path, compile)
        else:
            raise ValueError("Unknown path type")
        
        print("Done")
        
    def analyze_single_file(self, path, compile):
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
            out_path = os.path.join(save_dir, f"{fn}.xml")
        else:
            out_path = os.path.join(save_dir, f"{fn}T.xml")

        print("Starting tokenization")
        tokenizer = Tokenizer()
        output_tokens = tokenizer.tokenize(lines)
        print("Finished tokenization")

        if compile:
            print("Starting compilation")
            engine = CompilationEngine(output_tokens)
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
    parser.add_argument("--compile", action='store_true', default=False)
    args = parser.parse_args()
    jack_analyzer = JackAnalyzer()
    jack_analyzer.analyze(args.path, args.compile)
