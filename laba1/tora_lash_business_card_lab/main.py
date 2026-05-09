from datetime import datetime

# Константа текущего года берется из системы автоматически.
CURRENT_YEAR = datetime.now().year

# ANSI-коды для розового оформления в терминале.
# Если терминал их не поддерживает, программа все равно будет работать корректно.
PINK = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def ask_non_empty_text(prompt: str) -> str:
    """Запрашивает непустую строку у пользователя."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не должно быть пустым. Повторите ввод.")


def ask_int(prompt: str, min_value: int, max_value: int) -> int:
    """Запрашивает целое число и проверяет допустимый диапазон."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"Введите число от {min_value} до {max_value}.")
        except ValueError:
            print("Ошибка: нужно ввести целое число.")


def ask_float(prompt: str, min_value: float, max_value: float) -> float:
    """Запрашивает число с плавающей точкой и проверяет допустимый диапазон."""
    while True:
        try:
            value = float(input(prompt).replace(",", ".").strip())
            if min_value <= value <= max_value:
                return value
            print(f"Введите число от {min_value} до {max_value}.")
        except ValueError:
            print("Ошибка: нужно ввести число. Например: 165.5")


def print_box(lines: list[str], width: int = 54) -> None:
    """Печатает список строк внутри декоративной рамки."""
    border = "*" * width
    print(PINK + border + RESET)
    for line in lines:
        print(PINK + "*" + RESET + line.center(width - 2) + PINK + "*" + RESET)
    print(PINK + border + RESET)


def print_card(first_name: str, last_name: str, birth_year: int, age: int, height: float) -> None:
    """Формирует и выводит личную визитку пользователя."""
    width = 54
    border = "*" * width

    card_lines = [
        "ВАША ВИЗИТКА",
        "Студия Tora Lash & Brow",
        "",
        f"Имя: {first_name}",
        f"Фамилия: {last_name}",
        f"Год рождения: {birth_year}",
        f"Возраст: {age} года/лет",
        f"Рост: {height:.1f} см",
    ]

    print(PINK + border + RESET)
    for index, line in enumerate(card_lines):
        if index < 2:
            text = line.center(width - 2)
        else:
            text = " " + line.ljust(width - 3)
        print(PINK + "*" + RESET + BOLD + text + RESET + PINK + "*" + RESET)
    print(PINK + border + RESET)


def main() -> None:
    """Основная функция программы."""
    print_box(["Личная визитка", "Tora Lash & Brow"])
    print()

    first_name = ask_non_empty_text("Введите ваше имя: ")
    last_name = ask_non_empty_text("Введите вашу фамилию: ")
    birth_year = ask_int("Введите год рождения: ", 1900, CURRENT_YEAR)
    height = ask_float("Введите ваш рост (см): ", 50.0, 250.0)

    age = CURRENT_YEAR - birth_year

    print()
    print_card(first_name, last_name, birth_year, age, height)


if __name__ == "__main__":
    main()
