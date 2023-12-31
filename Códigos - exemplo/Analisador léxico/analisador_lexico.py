# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16yxN4WpJOxnC1YpXZOU1cXYnLv1qHx68
"""

import re

# Lista de padrões para tokens
patterns = [
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\bint\b', 'INT_TYPE'),
    (r'\bfloat\b', 'FLOAT_TYPE'),
    (r'\b[a-zA-Z_]\w*\b', 'IDENTIFIER'),
    (r'\b\d+\b', 'INTEGER'),
    (r'\b\d+\.\d+\b', 'FLOAT'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'=', 'ASSIGN'),
    (r';', 'SEMICOLON'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
]

# Função para analisar o código-fonte
def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                position = match.end()
                break

        if not match:
            print("Erro: Caractere inválido encontrado:", code[position])
            position += 1

    return tokens

# Código-fonte de exemplo
source_code = """
int x = 10;
float y = 3.14;
if x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")
"""

# Analisar e imprimir os tokens
tokens = tokenize(source_code)
for token in tokens:
    print(token)