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

BINARY_OPS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
