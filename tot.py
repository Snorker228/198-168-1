#1. Веселая семейка:
import random

def catch_ball():
    return random.random() < 0.7

def ask_question():
    return "Какой столицей Франции является Париж?"

def play_game():
    print("Начинаем игру!")
    
    # Компьютер бросает мяч
    if catch_ball():
        print("Вы поймали мяч!")
        answer = input(ask_question() + " (Да/Нет) ")
        if answer.lower() == "да":
            print("Правильный ответ!")
        else:
            print("Неправильный ответ.")
    else:
        print("Вы не поймали мяч.")
        print("Компьютер отвечает на вопрос.")
        if random.random() < 0.5:
            print("Компьютер ответил правильно.")
        else:
            print("Компьютер ответил неправильно.")
    
    # Игрок бросает мяч
    if catch_ball():
        print("Компьютер поймал мяч!")
        if random.random() < 0.5:
            print("Компьютер ответил правильно.")
        else:
            print("Компьютер ответил неправильно.")
    else:
        print("Компьютер не поймал мяч.")
        answer = input(ask_question() + " (Да/Нет) ")
        if answer.lower() == "да":
            print("Правильный ответ!")
        else:
            print("Неправильный ответ.")

play_game()

#2. Встраивание функций:
def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        reversed_numbers.append(reversed_num)
        if is_palindrome(num):
            print(f"{num} является палиндромом.")
    print("Список с перевернутыми числами:", reversed_numbers)

#3. Сложный процент:

def calculate_final_amount(initial_amount, annual_interest_rate, num_years):
    final_amount = initial_amount * (1 + annual_interest_rate) ** num_years
    return final_amount
initial_amount = float(input("Введите начальную сумму для инвестирования: "))
annual_interest_rate = float(input("Введите годовую процентную ставку (в десятичной форме): "))
num_years = int(input("Введите количество лет для инвестирования: "))

final_amount = calculate_final_amount(initial_amount, annual_interest_rate, num_years)
print(f"Итоговая сумма через {num_years} лет: {final_amount:.2f}")

#4. Теория игр:
import random
def create_doors(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for i in prize_indices:
        doors[i] = "приз"
    return doors
def simulate_game(doors):
    # Игрок 1 выбирает дверь
    player1_choice = random.randint(0, len(doors) - 1)
    # Открывается одна из дверей, за которой нет приза
    unopened_doors = [i for i in range(len(doors)) if i != player1_choice and doors[i] == "пусто"]
    opened_door = random.choice(unopened_doors)
    # Игрок 2 решает, менять ли свой выбор
    player2_change_choice = random.choice([True, False])
    # Определение результатов игры
    if player2_change_choice:
        for i in range(len(doors)):
            if i != player1_choice and i != opened_door:
                player2_choice = i
                break
    else:
        player2_choice = player1_choice
    win_if_change = 1 if doors[player2_choice] == "приз" else 0
    win_if_stay = 1 if doors[player1_choice] == "приз" else 0
    return (win_if_change, win_if_stay)
# Пример использования
num_doors = 3
num_prizes = 1
doors = create_doors(num_doors, num_prizes)
print("Двери:", doors)
win_if_change, win_if_stay = simulate_game(doors)
print("Вероятность выигрыша, если игрок меняет выбор:", win_if_change)
print("Вероятность выигрыша, если игрок остается при своем выборе:", win_if_stay)
#5. Лутбоксы:

import random
import colorama
from colorama import Fore, Style
# Инициализация colorama
colorama.init()
# Списки предметов
common_items = ["Меч", "Щит", "Кольцо", "Броня", "Лук"]
rare_items = ["Посох Стихии", "Арбалет Громовержца", "Амулет Защиты", "Плащ Невидимости", "Перчатки Силы"]
epic_items = ["Посох Магии", "Лук Ветра", "Щит Героя", "Броня Титана", "Клинок Правосудия"]
legendary_items = ["Меч Короля", "Броня Древних", "Посох Вечности", "Лук Судьбы", "Арбалет Богов"]
# Шанс выпадения каждого типа предметов
common_chance = 0.7
rare_chance = 0.2
epic_chance = 0.1
legendary_chance = 0.05
# Счетчики для подсчета выпавших предметов
common_count = 0
rare_count = 0
epic_count = 0
legendary_count = 0
# Гарант легендарного предмета
guarantee_counter = 0
# Открытие 20 лутбоксов
for _ in range(20):
    random_chance = random.random()
    if random_chance < legendary_chance:
        legendary_item = random.choice(legendary_items)
        print(f"{Fore.ORANGE}{legendary_item}{Style.RESET_ALL}")
        legendary_count += 1
        guarantee_counter = 0
    elif random_chance < legendary_chance + epic_chance:
        epic_item = random.choice(epic_items)
        print(f"{Fore.MAGENTA}{epic_item}{Style.RESET_ALL}")
        epic_count += 1
        guarantee_counter += 1
    elif random_chance < legendary_chance + epic_chance + rare_chance:
        rare_item = random.choice(rare_items)
        print(f"{Fore.BLUE}{rare_item}{Style.RESET_ALL}")
        rare_count += 1
        guarantee_counter += 1
    else:
        common_item = random.choice(common_items)
        print(f"{Fore.WHITE}{common_item}{Style.RESET_ALL}")
        common_count += 1
        guarantee_counter += 1
    
    if guarantee_counter == 20:
        legendary_item = random.choice(legendary_items)
        print(f"{Fore.ORANGE}{legendary_item} (Гарантированный){Style.RESET_ALL}")
        legendary_count += 1
        guarantee_counter = 0
print()
print(f"Обычных предметов: {Fore.WHITE}{common_count}{Style.RESET_ALL}")
print(f"Редких предметов: {Fore.BLUE}{rare_count}{Style.RESET_ALL}")
if epic_count > 3:
    print(f"Эпических предметов: {Fore.MAGENTA}{epic_count} (Удача!){Style.RESET_ALL}")
else:
    print(f"Эпических предметов: {Fore.MAGENTA}{epic_count}{Style.RESET_ALL}")
if legendary_count > 1:
    print(f"Легендарных предметов: {Fore.ORANGE}{legendary_count} (Большая удача!){Style.RESET_ALL}")
else:
    print(f"Легендарных предметов: {Fore.ORANGE}{legendary_count}{Style.RESET_ALL}")
