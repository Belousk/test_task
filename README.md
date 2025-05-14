# 📊 Salary Report Generator

Скрипт на Python для генерации отчёта по зарплатам сотрудников из CSV-файлов. Используется только стандартная библиотека.

---

## 📦 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Belousk/test_task.git
cd salary-report
```

2. Перейдите в папку проекта:

```bash
cd Solution
```
(Опционально) создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
Установите зависимости для тестов:
```bash
pip install -r requirements.txt
```

3. Запустите скрипт, передав один или несколько `.csv` файлов и указав тип отчёта:

```bash
python3 main.py files/data1.csv files/data2.csv --report payout
```

### ✅ Пример вывода:

```
                name                 hours rate  payout
Design
--------------- Bob Smith            150   40    $6000
--------------- Carol Williams       170   60    $10200
                                     320         $16200

Marketing
--------------- Alice Johnson        160   50    $8000
                                     160         $8000
```

---

## 📁 Возможности

- Группировка по отделам (Design, Marketing и т.д.).
- Поддержка файлов с колонками `rate`, `salary` или `hourly_rate` — они автоматически нормализуются.
- Порядок колонок может быть произвольным.
- Можно обрабатывать несколько файлов сразу.

---

## 🧪 Тестирование

Проект покрыт тестами с использованием `pytest`.

1. Установите `pytest`, если ещё не установлен:

```bash
pip install pytest
```

2. Запустите тесты из корня проекта:

```bash
pytest
```

---

## 📌 Структура проекта

```
Solution/
├── main.py                  # Точка входа
├── reports/
│   └── payout_report.py     # Реализация отчёта payout
├── parsers/
│   └── csv_parser.py        # Парсер CSV
├── utils/
│   └── column_mapper.py     # Унификация названий колонок
├── tests/
│   ├── test_csv_parser.py   # Тесты парсера
│   └── test_payout_report.py# Тесты отчёта
└── README.md
```

---

## ⚠️ Обработка ошибок

- Если передан неизвестный тип отчёта — будет показано сообщение об ошибке.
- Если файл не найден или повреждён — скрипт завершится с объяснением.

---

## 📤 Пример

```bash
python3 main.py example1.csv example2.csv --report payout
```

---

