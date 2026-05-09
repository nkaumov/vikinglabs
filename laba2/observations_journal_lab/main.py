from pathlib import Path
from datetime import datetime

# Папка, в которой находится файл программы
BASE_DIR = Path(__file__).resolve().parent

# Папка для данных. Она будет создана автоматически рядом с программой.
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "observations.txt"


def prepare_storage():
    """Создает папку data и файл журнала, если их еще нет."""
    DATA_DIR.mkdir(exist_ok=True)
    DATA_FILE.touch(exist_ok=True)


def print_header():
    """Выводит заголовок программы."""
    print("=" * 46)
    print("        ЖУРНАЛ НАБЛЮДЕНИЙ TORA LASH & BROW")
    print("=" * 46)


def input_date():
    """Запрашивает дату и проверяет формат ГГГГ-ММ-ДД."""
    while True:
        date_text = input("Введите дату (ГГГГ-ММ-ДД): ").strip()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Ошибка: дата должна быть в формате ГГГГ-ММ-ДД, например 2024-09-15.")


def input_rating():
    """Запрашивает оценку и проверяет, что это целое число от 1 до 10."""
    while True:
        rating_text = input("Введите оценку (1-10): ").strip()
        try:
            rating = int(rating_text)
            if 1 <= rating <= 10:
                return rating
            print("Ошибка: оценка должна быть в диапазоне от 1 до 10.")
        except ValueError:
            print("Ошибка: введите целое число.")


def add_record():
    """Добавляет новую запись в файл журнала."""
    print("\n--- Добавление новой записи ---")
    date_text = input_date()

    observation = input("Введите текст наблюдения: ").strip()
    while not observation:
        print("Ошибка: текст наблюдения не должен быть пустым.")
        observation = input("Введите текст наблюдения: ").strip()

    # Символ | используется как разделитель, поэтому заменяем его в тексте наблюдения.
    observation = observation.replace("|", "/")

    rating = input_rating()

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date_text} | {rating} | {observation}\n")

    print("\nЗапись успешно добавлена!")


def read_records():
    """Читает записи из файла и возвращает список кортежей: дата, оценка, текст."""
    records = []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(" | ", 2)
            if len(parts) == 3:
                date_text, rating_text, observation = parts
                try:
                    records.append((date_text, int(rating_text), observation))
                except ValueError:
                    # Некорректные строки пропускаются, чтобы программа не завершалась с ошибкой.
                    continue

    return records


def show_records():
    """Выводит все записи в виде таблицы и показывает статистику."""
    print("\n--- Все записи ---")
    records = read_records()

    if not records:
        print("Журнал пока пуст.")
        return

    date_width = 12
    rating_width = 7
    text_width = 42

    border = "+" + "-" * date_width + "+" + "-" * rating_width + "+" + "-" * text_width + "+"
    print(border)
    print(f"|{'Дата':^{date_width}}|{'Оценка':^{rating_width}}|{'Текст':^{text_width}}|")
    print(border)

    for date_text, rating, observation in records:
        short_text = observation[:text_width - 3] + "..." if len(observation) > text_width else observation
        print(f"|{date_text:^{date_width}}|{rating:^{rating_width}}|{short_text:<{text_width}}|")

    print(border)

    average_rating = sum(record[1] for record in records) / len(records)
    print("\nСтатистика:")
    print(f"Всего записей: {len(records)}")
    print(f"Средняя оценка: {average_rating:.2f}")


def clear_journal():
    """Очищает файл журнала после подтверждения пользователя."""
    answer = input("Вы действительно хотите очистить журнал? (да/нет): ").strip().lower()
    if answer in ("да", "д", "yes", "y"):
        DATA_FILE.write_text("", encoding="utf-8")
        print("Журнал очищен.")
    else:
        print("Очистка отменена.")


def print_menu():
    """Выводит меню действий."""
    print("\nВыберите действие:")
    print("1. Добавить запись")
    print("2. Показать все записи")
    print("3. Очистить журнал")
    print("4. Выход")


def main():
    """Главная функция программы."""
    prepare_storage()
    print_header()

    while True:
        print_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            clear_journal()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()
