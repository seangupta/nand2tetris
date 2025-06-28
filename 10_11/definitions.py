KEYWORD = "keyword"
SYMBOL = "symbol"
STRING_CONSTANT = "stringConstant"
INTEGER_CONSTANT = "integerConstant"
IDENTIFIER = "identifier"

TOKEN_TYPES = [KEYWORD, SYMBOL, STRING_CONSTANT, INTEGER_CONSTANT, IDENTIFIER]

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

KEYWORD_CONSTANTS = [
    'true',
    'false',
    'null',
    'this',
]

KEYWORD_CONSTANTS_JACK_TO_VM = {
    "true": ["push constant 1", "neg"],
    "false": ["push constant 0"],
    "null": ["push constant 0"],
    "this": ["push pointer 0"],
}

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

UNARY_OPS = ['-', '~']

UNARY_OPS_JACK_TO_VM = {
    "-": "neg",
    "~": "not",
}

BINARY_OPS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']

BINARY_OPS_JACK_TO_VM = {
    "+": "add",
    "-": "sub",
    "*": "call Math.multiply 2",
    "/": "call Math.divide 2",
    "&": "and",
    "|": "or",
    "<": "lt",
    ">": "gt",
    "=": "eq",
}
