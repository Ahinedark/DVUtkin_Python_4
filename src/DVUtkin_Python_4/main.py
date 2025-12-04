"""Задание 1. Задан текст случайным образом.

Напишите функцию, которая в качестве аргументов получает:
text – исходный текст
n_word – количество слов
actions – кортеж действий.
Функция разбивает пробелами текст на необходимое количество слов различной длины
(используйте random) и к каждому получившемуся слову применяет полученные действия. К
первому слову – первое действие, ко второму слову – второе действие и т.д., к седьмому
слову – первое действие.
Действия простые:
'upper' - сделать все буквы заглавными
'reverse' - слово в обратном порядке
'double' - продублировать слово (станет слово + это же слово)
'del_digits' - удалить из слова цифры
'del_even' - удалить каждый чётный символ
'replace' - заменить каждую цифру слова на “Python”
Необязательно, но приветствуется при выполнении задания использование map(), reduce() и
т.д., а также lambda-функций.
"""

import random
import string


def apply_actions(text: str, n_word: int, actions: tuple[str]):
    """Функция для разбивки текста на слова случайной длины и применения к ним определённых действий.

    Args:
        text (str): исходный текст
        n_word (int): количество слов
        actions (tuple[str]): кортеж действий

    Returns:
        list[str]: список слов, к которым применены действия из кортежа actions
    """
    print('Исходный текст:', text, '\n')

    # Создаём список с индексами, по которым вставим пробелы в исходном тексте
    cut = random.sample(range(1, len(text) - 1), n_word - 1)
    # Вставляем пробелы по индексам с конца списка, чтобы остальные не поплыли
    cut.sort(reverse=True)
    for i in cut:
        text = text[:i] + ' ' + text[i:]
    # Создаём список со словами (разделив исходный текст по пробелам)
    words = text.split()

    print('Текст после разбивки:', text, '\n')

    # Словарь действий
    actions_map = {
        'upper': lambda word: word.upper(),
        'reverse': lambda word: word[::-1],
        'double': lambda word: word + word,
        'del_digits': lambda word: ''.join(filter(lambda ch: not ch.isdigit(), word)),
        'del_even': lambda word: ''.join(
            word[i] for i in range(len(word)) if (i + 1) % 2 == 1
        ),
        'replace': lambda word: ''.join(
            'Python' if ch.isdigit() else ch for ch in word
        ),
    }

    # Проходимся по словам, применяем к ним соответстующие действия (согласно заданию)
    result = []
    i = 0
    while i < len(words):
        result.append(actions_map[actions[i % len(actions)]](words[i]))
        # Красивый вывод {номер}: действие(слово) -> результат
        print(f'{i + 1}: {actions[i % len(actions)]}({words[i]})\t->\t{result[i]}\n')
        i += 1


n = 1000
n_word = 10
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')
text = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
apply_actions(text, n_word, actions)
