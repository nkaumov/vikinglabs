# Лабораторная работа: Журнал наблюдений

Простая консольная программа на Python для ведения журнала ежедневных наблюдений.

## Состав проекта

- `main.py` - основной файл программы
- `data/observations.txt` - файл с данными, создается автоматически после запуска
- `run_windows.bat` - быстрый запуск на Windows
- `report_observations_journal.docx` - отчет по лабораторной работе

## Запуск в Windows PowerShell / терминале VS Code

```bash
python main.py
```

Если команда `python` не работает, попробуйте:

```bash
py main.py
```

## Запуск в Google Colab

1. Откройте Google Colab.
2. Загрузите файл `main.py`.
3. Выполните в ячейке:

```python
import platform
print(platform.system())
%run main.py
```

В Colab программа запускается в Linux-среде.
