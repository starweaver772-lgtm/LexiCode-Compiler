# Keywords
KEYWORDS = {
    "int",
    "float",
    "double",
    "char",
    "string",
    "if",
    "else",
    "for",
    "while",
    "return",
    "void",
    "class",
    "public",
    "private",
    "using",
    "namespace",
    "include"
}


# Operators
OPERATORS = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "=",
    "==",
    "!=",
    ">",
    "<",
    ">=",
    "<=",
    "++",
    "--",
    "&&",
    "||"
}


# Separators
SEPARATORS = {
    ";",
    ",",
    "(",
    ")",
    "{",
    "}",
    "[",
    "]"
}


def analyze_code(code):

    tokens = []

    i = 0
    line = 1

    while i < len(code):

        current = code[i]

        # Ignore spaces
        if current.isspace():

            if current == "\n":
                line += 1

            i += 1
            continue


        # Identifier / Keyword
        if current.isalpha() or current == "_":

            word = ""

            while i < len(code) and (
                code[i].isalnum() or code[i] == "_"
            ):
                word += code[i]
                i += 1

            if word in KEYWORDS:
                token_type = "KEYWORD"
            else:
                token_type = "IDENTIFIER"

            tokens.append({
                "lexeme": word,
                "token": token_type,
                "line": line
            })

            continue


        # Number
        if current.isdigit():

            number = ""

            while i < len(code) and (
                code[i].isdigit() or code[i] == "."
            ):
                number += code[i]
                i += 1

            tokens.append({
                "lexeme": number,
                "token": "NUMBER",
                "line": line
            })

            continue


        # Check two-character operators
        if i + 1 < len(code):

            two_char = code[i:i + 2]

            if two_char in OPERATORS:

                tokens.append({
                    "lexeme": two_char,
                    "token": "OPERATOR",
                    "line": line
                })

                i += 2
                continue


        # One-character operators
        if current in OPERATORS:

            tokens.append({
                "lexeme": current,
                "token": "OPERATOR",
                "line": line
            })

            i += 1
            continue


        # Separators
        if current in SEPARATORS:

            tokens.append({
                "lexeme": current,
                "token": "SEPARATOR",
                "line": line
            })

            i += 1
            continue


        # Unknown character
        tokens.append({
            "lexeme": current,
            "token": "UNKNOWN",
            "line": line
        })

        i += 1


    return tokens