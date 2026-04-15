"""
rpn.py

Calculadora RPN (Reverse Polish Notation).

Soporta:
- Operaciones básicas (+, -, *, /)
- Funciones matemáticas (sqrt, log, ln, exp, potencias)
- Trigonometría en grados
- Comandos de pila (dup, swap, drop, clear)
- Memorias (00 a 09)
- Manejo de errores mediante RPNError
- Tests integrados con unittest
"""

import sys
import math
import unittest


class RPNError(Exception):
    """Excepción personalizada para errores RPN."""


def safe_pop(stack):
    """Extrae un valor de la pila validando que no esté vacía."""
    if not stack:
        raise RPNError("Pila insuficiente")
    return stack.pop()


def safe_pop2(stack):
    """Extrae dos valores de la pila."""
    b = safe_pop(stack)
    a = safe_pop(stack)
    return a, b


def rpn_eval(expr: str):
    """
    Evalúa una expresión en notación RPN.

    :param expr: expresión en formato string
    :return: resultado numérico
    """
    stack = []
    mem = {f"{i:02d}": 0.0 for i in range(10)}

    # -------------------------
    # Operaciones básicas
    # -------------------------
    def op_add(a, b): return a + b
    def op_sub(a, b): return a - b
    def op_mul(a, b): return a * b

    def op_div(a, b):
        if b == 0:
            raise RPNError("División por cero")
        return a / b

    ops = {
        "+": op_add,
        "-": op_sub,
        "*": op_mul,
        "/": op_div
    }

    # -------------------------
    # Funciones matemáticas
    # -------------------------
    def f_sqrt(x):
        if x < 0:
            raise RPNError("Raíz negativa")
        return math.sqrt(x)

    funcs = {
        "sqrt": f_sqrt,
        "log": math.log10,
        "ln": math.log,
        "ex": math.exp,
        "10x": lambda x: 10 ** x,
        "1/x": lambda x: 1 / x if x != 0 else (_ for _ in ()).throw(RPNError("División por cero")),
        "chs": lambda x: -x
    }

    # -------------------------
    # Trigonometría (grados)
    # -------------------------
    trig = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tg": lambda x: math.tan(math.radians(x))
    }

    # -------------------------
    # Constantes
    # -------------------------
    consts = {
        "p": math.pi,
        "e": math.e,
        "j": (1 + math.sqrt(5)) / 2
    }

    # -------------------------
    # Procesamiento
    # -------------------------
    for token in expr.split():

        # Número
        try:
            stack.append(float(token))
            continue
        except ValueError:
            pass

        # Constantes
        if token in consts:
            stack.append(consts[token])
            continue

        # Operaciones binarias
        if token in ops:
            a, b = safe_pop2(stack)
            stack.append(ops[token](a, b))
            continue

        # Funciones unarias
        if token in funcs:
            x = safe_pop(stack)
            stack.append(funcs[token](x))
            continue

        # Trigonometría
        if token in trig:
            x = safe_pop(stack)
            stack.append(trig[token](x))
            continue

        # Potencia
        if token == "yx":
            a, b = safe_pop2(stack)
            stack.append(a ** b)
            continue

        # Pila
        if token == "dup":
            stack.append(stack[-1] if stack else (_ for _ in ()).throw(RPNError("Pila insuficiente")))
            continue

        if token == "swap":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente")
            stack[-1], stack[-2] = stack[-2], stack[-1]
            continue

        if token == "drop":
            safe_pop(stack)
            continue

        if token == "clear":
            stack.clear()
            continue

        # Memorias
        if token.startswith("STO"):
            key = token[3:]
            if key not in mem:
                raise RPNError("Memoria inválida")
            mem[key] = safe_pop(stack)
            continue

        if token.startswith("RCL"):
            key = token[3:]
            if key not in mem:
                raise RPNError("Memoria inválida")
            stack.append(mem[key])
            continue

        raise RPNError(f"Token inválido: {token}")

    if len(stack) != 1:
        raise RPNError("Resultado inválido")

    return stack[0]


# =========================
# TESTS
# =========================

class TestRPN(unittest.TestCase):
    """Tests del evaluador RPN."""

    def test_basico(self):
        self.assertEqual(rpn_eval("3 4 +"), 7)

    def test_complejo(self):
        self.assertEqual(rpn_eval("5 1 2 + 4 * + 3 -"), 14)

    def test_error(self):
        with self.assertRaises(RPNError):
            rpn_eval("3 0 /")


# =========================
# MAIN
# =========================

def main():
    """Punto de entrada principal."""
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        unittest.main(argv=[sys.argv[0]])
        return

    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("RPN> ")
        print(rpn_eval(expr))
    except RPNError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()