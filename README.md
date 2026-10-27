# Шишиморов Ярослав Сергеевич, группа 221141, вариант 1, лабораторная №1

## Дисциплина: Методы и технологии программирования (часть 1)
### Лабораторная работа № 1: «Система контроля версий Git. Работа с ней»

---

## 📋 Информация о работе

- **Студент:** Шишиморов Ярослав Сергеевич
- **Группа:** 221141
- **Вариант:** 1
- **Номер лабораторной работы:** №1
- **Тема:** Система контроля версий Git (управление репозиторием, ветвление, слияние, разрешение конфликтов, настройка хуков)
- **Уровень выполнения:** Повышенный (3 задания средней сложности + 2 задания повышенной сложности для получения оценки «повышенная»)

---

## 🎯 Состав заданий (Вариант 1)

| Уровень сложности | № | Формулировка задания | Выполнение / Доказательство |
|---|:---:|---|---|
| **Средняя сложность** | **1** | Установить Git и настроить имя, email. | Настроены `user.name` и `user.email`, подтверждение в отчёте ниже. |
| **Средняя сложность** | **3** | Добавить файл, сделать коммит. | Создан модуль `src/calculator.py`, зафиксирован коммитом `feat: add calculator module and tests (Task 3)`. |
| **Средняя сложность** | **5** | Создать ветку feature, добавить новый файл. | Создана ветка `feature`, добавлен `src/string_utils.py`, выполнено слияние с `git merge --no-ff`. |
| **Повышенная сложность** | **1** | Разрешить конфликт при слиянии веток. | Смоделирован и разрешён конфликт в ветке `conflict-demo` в файле `src/calculator.py` со слиянием `--no-ff`. |
| **Повышенная сложность** | **4** | Настроить Git hook для проверки кода flake8. | Разработан скрипт `hooks/pre-commit` и скрипт установки `hooks/install_hooks.py`. |

---

## 🛠️ Подробный отчёт и доказательства выполнения заданий

### 1. Задание средней сложности №1: Настройка имени и email в Git
Конфигурация пользователя Git выполнена глобально и локально в репозитории:
```bash
git config --global user.name "Yaroslav"
git config --global user.email "y.shishimorov@gmail.com"
```
Подтверждение вывода команды `git config --list --show-origin`:
```text
file:C:/Users/manyf/.gitconfig    user.name=Yaroslav
file:C:/Users/manyf/.gitconfig    user.email=y.shishimorov@gmail.com
```

### 2. Задание средней сложности №3: Добавление файла и первый коммит
В проект добавлен базовый модуль математических операций `src/calculator.py` и его модульные тесты `tests/test_calculator.py`. Изменения проиндексированы и зафиксированы с семантическим сообщением:
```bash
git add src/calculator.py tests/test_calculator.py main.py
git commit -m "feat: add calculator module and tests (Task 3)"
```

### 3. Задание средней сложности №5: Создание ветки feature и добавление файла
1. Создана ветка `feature` и осуществлён переход на неё:
   ```bash
   git checkout -b feature
   ```
2. В ветке `feature` создан новый модуль `src/string_utils.py` с функциями работы со строками (`reverse_string`, `is_palindrome`, `count_vowels`) и тесты `tests/test_string_utils.py`.
3. Изменения зафиксированы коммитом в ветке `feature`:
   ```bash
   git commit -m "feat: add string utilities module and tests in feature branch (Task 5)"
   ```
4. Выполнен возврат в ветку `main` и слияние с флагом `--no-ff` (для обязательного создания явного merge-коммита согласно требованиям преподавателя):
   ```bash
   git checkout main
   git merge --no-ff feature -m "merge: merge branch feature into main with --no-ff (Task 5)"
   ```

### 4. Задание повышенной сложности №1: Разрешение конфликта при слиянии веток
Для демонстрации разрешения конфликта:
1. Создана отдельная ветка `conflict-demo`:
   ```bash
   git checkout -b conflict-demo
   ```
2. В файле `src/calculator.py` функция деления была модифицирована (добавлено округление результата до 4 знаков) и закоммичена:
   ```python
   def divide(a: float, b: float) -> float:
       """Деление числа a на b с округлением до 4 знаков."""
       if b == 0:
           raise ZeroDivisionError("Деление на ноль невозможно.")
       return round(a / b, 4)
   ```
3. Выполнен возврат в ветку `main`, где в тех же самых строках файла `src/calculator.py` была добавлена другая модификация (кастомный текст ошибки деления на ноль) и закоммичена:
   ```python
   def divide(a: float, b: float) -> float:
       """Безопасное деление чисел a и b с проверкой входных данных."""
       if b == 0:
           raise ZeroDivisionError("Деление на ноль строго запрещено математикой.")
       return float(a / b)
   ```
4. При попытке слияния ветки `conflict-demo` в ветку `main` Git закономерно зафиксировал конфликт содержимого:
   ```text
   Auto-merging src/calculator.py
   CONFLICT (content): Merge conflict in src/calculator.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```
5. В файле образовались стандартные маркеры конфликта Git:
   ```python
   <<<<<<< HEAD
       """Безопасное деление чисел a и b с проверкой входных данных."""
       if b == 0:
           raise ZeroDivisionError("Деление на ноль строго запрещено математикой.")
       return float(a / b)
   =======
       """Деление числа a на b с округлением до 4 знаков."""
       if b == 0:
           raise ZeroDivisionError("Деление на ноль невозможно.")
       return round(a / b, 4)
   >>>>>>> conflict-demo
   ```
6. Конфликт был успешно разрешён объединением обеих доработок (сохранена детальная ошибка и добавлено округление до 4 знаков):
   ```python
   def divide(a: float, b: float) -> float:
       """Безопасное деление числа a на b с проверкой нуля и округлением до 4 знаков."""
       if b == 0:
           raise ZeroDivisionError("Деление на ноль строго запрещено математикой.")
       return round(float(a / b), 4)
   ```
7. Разрешённый файл был добавлен в индекс и закоммичен:
   ```bash
   git add src/calculator.py
   git commit -m "merge: resolve merge conflict in divide function between main and conflict-demo (Task 1 Повышенная)"
   ```

### 5. Задание повышенной сложности №4: Настройка Git hook для flake8
По правилам кафедры («*Скрипт хука кладите в папку hooks/ репозитория, .git/hooks на GitHub не попадает*»):
- Скрипт проверки помещён в репозиторий: `hooks/pre-commit`.
- Хук перехватывает все подготовленные к коммиту (`staged`) файлы с расширением `.py`, запускает на них `flake8 --max-line-length=120` (либо синтаксическую валидацию через `py_compile`), и в случае наличия ошибок форматирования или синтаксиса блокирует создание некорректного коммита с кодом возврата `1`.
- Создан вспомогательный скрипт установки `hooks/install_hooks.py`, копирующий хук в локальную папку `.git/hooks/` и делающий его исполняемым:
  ```bash
  python hooks/install_hooks.py
  ```

---

## 🌳 Полный граф коммитов репозитория

```text
* e4d65e3 (HEAD -> main) fix: adjust english vowels set in count_vowels function
*   ae80724 merge: resolve merge conflict in divide function between main and conflict-demo (Task 1 Повышенная)
|\  
| * 3cfcd25 (conflict-demo) feat: add 4-decimal precision to divide in conflict-demo branch
* | d1ae794 feat: add custom zero division message to divide in main branch
|/  
*   6c0cf36 merge: merge branch feature into main with --no-ff (Task 5)
|\  
| * a716b28 (feature) feat: add string utilities module and tests in feature branch (Task 5)
|/  
* 5afe714 feat: add Git pre-commit hook with flake8 verification (Task 4 Повышенная)
* 039a47e feat: add calculator module and tests (Task 3)
* 0118035 chore: initial repository structure and .gitignore
```

---

## 🚀 Запуск проекта и тестов

### Запуск демонстрационной программы:
```bash
python main.py
```

### Запуск автоматических тестов:
```bash
python -m unittest discover tests
```
*Результат: 8 тестов успешно пройдено (OK).*

---
