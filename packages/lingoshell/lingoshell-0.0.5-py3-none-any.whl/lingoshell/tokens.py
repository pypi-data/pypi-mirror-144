import importlib.resources
import json

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_STRING = "STRING"
TT_IDENTIFIER = "IDENTIFIER"
TT_KEYWORD = "KEYWORD"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_POW = "POW"
TT_EQ = "EQ"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_LSQUARE = "LSQUARE"
TT_RSQUARE = "RSQUARE"
TT_EE = "EE"
TT_NE = "NE"
TT_LT = "LT"
TT_GT = "GT"
TT_LTE = "LTE"
TT_GTE = "GTE"
TT_COMMA = "COMMA"
TT_ARROW = "ARROW"
TT_NEWLINE = "NEWLINE"
TT_EOF = "EOF"

try:
    with importlib.resources.open_text("lingoshell", "keywords.json") as f:
        KEYWORDS = json.load(f)
except Exception:
    print("Runtime Error: Could not find saved languages. Will use EN.")
    KEYWORDS = [
        "VAR",
        "AND",
        "OR",
        "NOT",
        "IF",
        "ELIF",
        "ELSE",
        "FOR",
        "TO",
        "STEP",
        "WHILE",
        "METHOD",
        "THEN",
        "END",
        "RETURN",
        "CONTINUE",
        "BREAK",
    ]

try:
    with importlib.resources.open_text("lingoshell", "language_keywords.json") as f:
        LANGUAGE_KEYWORDS = json.load(f)
except Exception:
    print("Runtime Error: Could not find saved languages. Will use EN.")
    LANGUAGE_KEYWORDS = {
        "en": {
            "VAR": "VAR",
            "AND": "AND",
            "OR": "OR",
            "NOT": "NOT",
            "IF": "IF",
            "ELIF": "ELIF",
            "ELSE": "ELSE",
            "FOR": "FOR",
            "TO": "TO",
            "STEP": "STEP",
            "WHILE": "WHILE",
            "METHOD": "METHOD",
            "THEN": "THEN",
            "END": "END",
            "RETURN": "RETURN",
            "CONTINUE": "CONTINUE",
            "BREAK": "BREAK",
        }
    }


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None, lang=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

        self.lang = lang

    def matches(self, type_, value):
        if self.lang is not None and self.lang in LANGUAGE_KEYWORDS:
            return (
                self.type == type_ and self.value == LANGUAGE_KEYWORDS[self.lang][value]
            )
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"
