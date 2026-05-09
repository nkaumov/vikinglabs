from pathlib import Path
from datetime import datetime
import json

# Папка, в которой находится файл программы.
# Pathlib позволяет создавать пути одинаково удобно в Windows, Linux и macOS.
BASE_DIR = Path(__file__).resolve().parent

# Папка для хранения данных создается автоматически рядом с программой.
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# JSON-файл с заметками.
NOTES_FILE = DATA_DIR / "notes.json"


def print_header():
    """Выводит шапку программы."""
    print("=" * 50)
    print("                 ДНЕВНИК ЗАМЕТОК")
    print("=" * 50)


def load_notes():
    """Загружает список заметок из JSON-файла."""
    if not NOTES_FILE.exists():
        return []

    try:
        with NOTES_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except json.JSONDecodeError:
        print("Внимание: файл JSON поврежден или пуст. Будет создан новый список заметок.")
        return []


def save_notes(notes):
    """Сохраняет список заметок в JSON-файл."""
    with NOTES_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)


def create_note():
    """Создает новую заметку и сохраняет ее в JSON-файл."""
    print("\n--- Создание новой заметки ---")

    title = input("Введите заголовок заметки: ").strip()
    while not title:
        print("Ошибка: заголовок не должен быть пустым.")
        title = input("Введите заголовок заметки: ").strip()

    text = input("Введите текст заметки: ").strip()
    while not text:
        print("Ошибка: текст заметки не должен быть пустым.")
        text = input("Введите текст заметки: ").strip()

    now = datetime.now()

    notes = load_notes()
    next_id = len(notes) + 1

    note = {
        "id": next_id,
        "title": title,
        "text": text,
        "created_at": now.strftime("%d.%m.%Y %H:%M:%S"),
        "created_date": now.strftime("%d.%m.%Y")
    }

    notes.append(note)
    save_notes(notes)

    print("\nЗаметка успешно сохранена!")
    print(f"Дата и время создания: {note['created_at']}")


def show_note(note):
    """Выводит одну заметку в красивом виде."""
    print("-" * 50)
    print(f"Заметка #{note.get('id', '-')}")
    print(f"Дата: {note.get('created_at', '-')}")
    print(f"Заголовок: {note.get('title', '-')}")
    print(f"Текст: {note.get('text', '-')}")


def show_all_notes():
    """Показывает все заметки из JSON-файла."""
    print("\n--- Все заметки ---")

    notes = load_notes()

    if not notes:
        print("Заметок пока нет.")
        return

    for note in notes:
        show_note(note)

    print("-" * 50)
    print(f"Количество заметок: {len(notes)}")


def get_valid_search_date():
    """Запрашивает дату для поиска и проверяет формат ДД.ММ.ГГГГ."""
    while True:
        date_text = input("Введите дату для поиска (ДД.ММ.ГГГГ): ").strip()

        try:
            datetime.strptime(date_text, "%d.%m.%Y")
            return date_text
        except ValueError:
            print("Ошибка: дата должна быть в формате ДД.ММ.ГГГГ. Например: 15.09.2024")


def find_notes_by_date():
    """Ищет и показывает заметки, созданные в выбранный день."""
    print("\n--- Поиск заметок по дате ---")

    search_date = get_valid_search_date()
    notes = load_notes()

    found_notes = [note for note in notes if note.get("created_date") == search_date]

    if not found_notes:
        print(f"Заметки за дату {search_date} не найдены.")
        return

    print(f"\nНайденные заметки за {search_date}:")
    for note in found_notes:
        show_note(note)

    print("-" * 50)
    print(f"Найдено заметок: {len(found_notes)}")


def show_menu():
    """Показывает меню действий."""
    print("\nВыберите действие:")
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Найти заметку по дате")
    print("4. Выход")


def main():
    """Главная функция программы."""
    print_header()

    while True:
        show_menu()
        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            create_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            find_notes_by_date()
        elif choice == "4":
            print("\nРабота программы завершена.")
            break
        else:
            print("\nОшибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()
