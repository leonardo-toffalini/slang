from icecream import ic
from enum import Enum, auto


class TokenType(Enum):
    int_lit = auto()
    plus = auto()
    minus = auto()
    put = auto()
    num_tokens = auto()


class Token:
    def __init__(self, token_type, token_val=None):
        self.token_type = token_type
        self.token_val = token_val

    def __repr__(self):
        return f"Token({self.token_type}, {self.token_val})"


def check_int(s):
    if s[0] in ("-", "+"):
        return s[1:].isdigit()
    return s.isdigit()


def read_words(file_path):
    with open(file_path, "r") as f:
        return f.read().split()


def read_tokens(words):
    token_list = []
    for word in words:
        if check_int(word):
            token_list.append(Token(TokenType.int_lit, int(word)))

        elif word == "+":
            token_list.append(Token(TokenType.plus))

        elif word == "-":
            token_list.append(Token(TokenType.minus))

        elif word == "put":
            token_list.append(Token(TokenType.put))

    return token_list


def simulate_program(token_list):
    stack = []
    for token in token_list:
        if token.token_type == TokenType.int_lit:
            stack.append(token.token_val)
        elif token.token_type == TokenType.plus:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token.token_type == TokenType.minus:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token.token_type == TokenType.put:
            a = stack.pop()
            print(a)


def main():
    words = read_words("example.slang")
    token_list = read_tokens(words)

    ic(words)
    ic(token_list)

    print("-----\n\n")

    simulate_program(token_list)


if __name__ == "__main__":
    main()
