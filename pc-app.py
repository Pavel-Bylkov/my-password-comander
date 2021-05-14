# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                             QLabel, QListWidget, QLineEdit, QTextEdit,
                             QInputDialog, QHBoxLayout, QVBoxLayout)
import json
from datetime import datetime

# https://password-commander.ru.uptodown.com/windows
# http://pascom.ru/screenshots
#

file_name = "data.json"


def is_password_good(password):
    """Функция проверки пароля, на соответствие правилам безопасного пароля"""
    if len(password) < 8:
        return False
    flag_u, flag_l, flag_d = False, False, False
    for s in password:
        if not flag_u and s >= "A" and s <= "Z":
            flag_u = True
        if not flag_l and s >= "a" and s <= "z":
            flag_l = True
        if not flag_d and s >= "0" and s <= "9":
            flag_d = True
        if flag_u and flag_l and flag_d:
            return True
    return False

def _generate_password(length, chars):
    import random
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

def get_random_passwords(n, a, b, u, length, sec=True, double=False):
    """Функция генерирует заданное количество случайных паролей

    n - количество паролей в результирующем списке
    a, b - числа, процент букв, чисел
    u - процентное соотношение Заглавных букв
    length - длина пароля
    sec - True - Исключать неоднозначные символы ilO
    double - True - Разрешить повторение символов и цифр
    :return list"""
    import random
    digits = "0123456789"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    n_d = length * b // 100
    n_c = length * a // 100
    n_u = n_c * u // 100
    n_s = length - n_c - n_d
    if sec:
        lowercase = lowercase.replace("i", "")
        lowercase = lowercase.replace("l", "")
        uppercase = uppercase.replace("O", "")
    result = []
    for _ in range(n):
        if not double:
            chars = (random.sample(digits * (n_d // 10 + 1), n_d) +
                     random.sample(punctuation * (n_s // 13 + 1), n_s) +
                     random.sample(uppercase * (n_u // len(uppercase) + 1), n_u) +
                     random.sample(lowercase * (n_c - n_u // len(lowercase) + 1), n_c - n_u))
        else:
            chars = list(_generate_password(n_d, digits) + _generate_password(n_s, digits) +
                         _generate_password(n_u, uppercase) + _generate_password(n_d, lowercase))
        random.shuffle(chars)
        result.append("".join(chars))
    return result


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        self.setWindowTitle("Password Commander v=1.0")
        self.init_gui()

    def init_gui(self):
        pass


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


main()