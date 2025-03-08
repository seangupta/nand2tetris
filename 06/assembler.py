import argparse
import os
import math
import itertools

WIDTH = 16

def expand_table(table):
    for k in list(table):
        v = table[k]
        for permutation in itertools.permutations(k, len(k)):
            permutation_str = "".join(permutation)
            if permutation_str not in table:
                table[permutation_str] = v

COMP_TABLE = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101"
}

DESTINATION_TABLE = {
    "": "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "ADM": "111"
}
expand_table(DESTINATION_TABLE)

JUMP_TABLE = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

SYMBOL_TABLE = {
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
}
for i in range(WIDTH):
    SYMBOL_TABLE[f"R{i}"] = i

def is_a_instruction(line):
    return line.startswith("@")

def convert_decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        raise ValueError
    
    if not decimal >= 0:
        raise ValueError
    
    if decimal == 0:
        width = 0
    else:
        width = math.floor(math.log2(decimal)) + 1

    remainder = decimal
    binary = ""
    for i in range(WIDTH - 1, -1, -1):
        if i > width - 1:
            value = 0
        else:
            power_of_2 = 2 ** i
            if remainder >= power_of_2:
                value = 1
                remainder -= power_of_2
            else:
                value = 0
        binary += str(value)

    assert remainder == 0
    assert len(binary) == WIDTH

    return binary

def translate_a_instruction(line):
    decimal_location = int(line[1:])
    assembled_line = convert_decimal_to_binary(decimal_location)
    assert len(assembled_line) == WIDTH
    return assembled_line

def translate_c_instruction(line):
    if "=" in line:
        dest, comp_jump = line.split("=")
    else:
        dest = ""
        comp_jump = line
    
    if ";" in comp_jump:
        comp, jump = comp_jump.split(";")
    else:
        comp = comp_jump
        jump = ""
    
    assembled_line = "111"

    if "M" in comp:
        a_bit = 1
        comp = comp.replace("M", "A")
    else:
        a_bit = 0
    comp_bits = COMP_TABLE[comp]

    dest_bits = DESTINATION_TABLE[dest]
    jump_bits = JUMP_TABLE[jump]

    assembled_line = f"111{a_bit}{comp_bits}{dest_bits}{jump_bits}"
    assert len(assembled_line) == WIDTH

    return assembled_line


def main(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    print(f"Read {file_path}")

    print("Stripping whitespace and comments")
    lines_stripped = []
    for line in lines:
        line = line.split("//")[0]
        line = line.strip()
        if line:
            print(line)
            lines_stripped.append(line)

    # identify labels and their line number, add to symbol table
    # and remove from lines
    print("Identifying labels")
    lines_stripped_without_labels = []
    next_line_number = 0
    for line in lines_stripped:
        if line[0] == "(":
            assert line.endswith(")")
            label = line[1:-1]
            SYMBOL_TABLE[label] = next_line_number
            print(f"Label {label}: value {next_line_number}")
        else:
            next_line_number += 1
            lines_stripped_without_labels.append(line)

    # identify variables and add to symbol table
    # replace labels and variables using symbol table
    print("Identifying variables and replacing labels and variables")
    next_empty_symbol_value = WIDTH
    lines_stripped_without_labels_with_replacements = []
    for line in lines_stripped_without_labels:
        if is_a_instruction(line):
            location = line[1:]
            if not location.isdigit():
                if location in SYMBOL_TABLE:
                    replacement = SYMBOL_TABLE[location]
                else:
                    # new symbol found
                    SYMBOL_TABLE[location] = next_empty_symbol_value
                    replacement = next_empty_symbol_value
                    next_empty_symbol_value += 1
                    print(f"symbol {location}: value {next_empty_symbol_value}")
                print(f"Replacing {location} with {replacement}")
                new_line = f"@{replacement}"
            else:
                new_line = line
        else:
            new_line = line
        lines_stripped_without_labels_with_replacements.append(new_line)

    print("Translating instructions")
    assembled_lines = []
    for line in lines_stripped_without_labels_with_replacements:
        if is_a_instruction(line):
            assembled_line = translate_a_instruction(line)
        else:
            assembled_line = translate_c_instruction(line)
        assembled_lines.append(assembled_line)

    head, tail = os.path.split(file_path)
    if not tail:
        raise ValueError

    name = tail.split(".asm")[0]
    out_name = f"{name}.hack"
    out_path = os.path.join(head, out_name)

    with open(out_path, "w") as f:
        f.writelines("\n".join(assembled_lines))

    print(f"Output written to {out_path}")
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")

    args = parser.parse_args()
    file_path = args.file_path
    main(file_path)
