import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4
    assert calculate(8, 0, '/') == 'Ошибка: Деление на ноль.'

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_sub():
    assert calculate(8, 5, '-') == 3
    assert calculate(8, 9, '-') == -1
    assert calculate(-9, 9, '-') == -18


def test_calculate_mul():
    assert calculate(-8, -5, '*') == 40
    assert calculate(1.5, 3, '*') == 4.5


def test_calculate():
    assert calculate(8, '111', '*') == 888

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
