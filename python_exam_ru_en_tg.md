# 📝 Python Exam — RU / EN / TG

- [Русский](#русский)
- [English](#english)
- [Тоҷикӣ](#тоҷикӣ)

---

# Русский

# 📝 Python Exam

**Продолжительность:** 2 часа

---

## Часть 1. Исправьте ошибки

Исправьте ошибки в следующих программах так, чтобы они работали корректно.

### Задача 1

```python
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i + 1])
```

### Задача 2

```python
x = int(input())

try:
    print(100 / x)
```

### Задача 3

```python
if name = "Admin":#
    print("Welcome")
```

### Задача 4

```python
import random

print(random.randint(100))
```

### Задача 5

```python
file = open("data.txt", "r")
file.write("Hello")
```

---

## Часть 2. Практические задания

### Задача 1. Работа со строками

Пользователь вводит строку.

Необходимо вывести:

* количество символов;
* количество слов;
* количество гласных букв;
* строку в обратном порядке.

### Задача 2. Работа со списками и модулем `random`

Сгенерируйте список из **30 случайных чисел** в диапазоне от **1 до 100**.

Выведите:

* максимальное число;
* минимальное число;
* среднее значение;
* количество чётных чисел;
* отсортированный список.

### Задача 3. Функции

Создайте функцию:

```python
def analyze(numbers):
    pass
```

Функция должна возвращать:

* сумму элементов;
* среднее значение;
* максимальный элемент;
* минимальный элемент.

Продемонстрируйте работу функции на примере списка чисел.

### Задача 4. Работа с файлами

Создайте файл **students.txt**.

Пользователь вводит имена студентов.

Ввод продолжается до тех пор, пока пользователь не введёт:

```text
stop
```

После завершения ввода необходимо:

1. сохранить все имена в файл;
2. прочитать данные из файла;
3. вывести список студентов в алфавитном порядке.

### Задача 5. Объектно-ориентированное программирование

Создайте класс **Student**.

**Поля класса:**

* `name`
* `age`
* `score`

**Методы класса:**

* `show_info()` — выводит информацию о студенте;
* `increase_score(points)` — увеличивает балл (максимальное значение — 100);
* `is_excellent()` — возвращает `True`, если балл не меньше 90, иначе `False`.

Создайте список минимум из **5 объектов** класса `Student`.

Выведите:

* информацию обо всех студентах;
* студента с самым высоким баллом;
* средний балл всей группы.

### Задача 6. Игра «Guess the Number»

Создайте игру, в которой компьютер случайным образом загадывает число от **1 до 100**.

Пользователь должен угадать это число.

После каждой попытки программа должна выводить:

* **«Больше»**, если загаданное число больше;
* **«Меньше»**, если загаданное число меньше.

После того как число будет угадано, необходимо вывести:

* количество попыток;
* время, затраченное на игру (используя модуль `datetime`).

---

# English

# 📝 Python Exam

**Duration:** 2 hours

---

## Part 1. Fix the Errors

Fix the errors in the following programs so that they work correctly.

### Task 1

```python
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i + 1])
```

### Task 2

```python
x = int(input())

try:
    print(100 / x)
```

### Task 3

```python
if name = "Admin":
    print("Welcome")
```

### Task 4

```python
import random

print(random.randint(100))
```

### Task 5

```python
file = open("data.txt", "r")
file.write("Hello")
```

---

## Part 2. Practical Tasks

### Task 1. Working with Strings

The user enters a string.

Output:

* the number of characters;
* the number of words;
* the number of vowels;
* the string in reverse order.

### Task 2. Working with Lists and the `random` Module

Generate a list of **30 random numbers** in the range from **1 to 100**.

Output:

* the maximum number;
* the minimum number;
* the average value;
* the count of even numbers;
* the sorted list.

### Task 3. Functions

Create a function:

```python
def analyze(numbers):
    pass
```

The function must return:

* the sum of the elements;
* the average value;
* the maximum element;
* the minimum element.

Demonstrate how the function works using a sample list of numbers.

### Task 4. Working with Files

Create a file named **students.txt**.

The user enters student names.

Input continues until the user enters:

```text
stop
```

After input is finished, you must:

1. save all the names to the file;
2. read the data back from the file;
3. print the list of students in alphabetical order.

### Task 5. Object-Oriented Programming

Create a class **Student**.

**Class fields:**

* `name`
* `age`
* `score`

**Class methods:**

* `show_info()` — prints information about the student;
* `increase_score(points)` — increases the score (the maximum value is 100);
* `is_excellent()` — returns `True` if the score is 90 or higher, otherwise `False`.

Create a list of at least **5 objects** of the `Student` class.

Output:

* information about all students;
* the student with the highest score;
* the average score of the whole group.

### Task 6. "Guess the Number" Game

Create a game in which the computer randomly picks a number from **1 to 100**.

The user must guess this number.

After each attempt, the program must output:

* **"Higher"** if the secret number is greater than the guess;
* **"Lower"** if the secret number is less than the guess.

Once the number is guessed, output:

* the number of attempts;
* the time spent on the game (using the `datetime` module).

---

# Тоҷикӣ

# 📝 Имтиҳони Python

**Давомнокӣ:** 2 соат

---

## Қисми 1. Хатоҳоро ислоҳ кунед

Хатоҳоро дар барномаҳои зерин тавре ислоҳ кунед, ки дуруст кор кунанд.

### Масъалаи 1

```python
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i + 1])
```

### Масъалаи 2

```python
x = int(input())

try:
    print(100 / x)
```

### Масъалаи 3

```python
if name = "Admin":
    print("Welcome")
```

### Масъалаи 4

```python
import random

print(random.randint(100))
```

### Масъалаи 5

```python
file = open("data.txt", "r")
file.write("Hello")
```

---

## Қисми 2. Супоришҳои амалӣ

### Масъалаи 1. Кор бо сатрҳо

Корбар сатр ворид мекунад.

Лозим аст чоп карда шавад:

* шумораи аломатҳо;
* шумораи калимаҳо;
* шумораи ҳарфҳои садонок;
* сатр бо тартиби баръакс.

### Масъалаи 2. Кор бо рӯйхатҳо ва модули `random`

Рӯйхати **30 адади тасодуфиро** дар фосилаи аз **1 то 100** созед.

Чоп кунед:

* адади максималӣ;
* адади минималӣ;
* арзиши миёна;
* шумораи ададҳои ҷуфт;
* рӯйхати мураттабшуда.

### Масъалаи 3. Функсияҳо

Функсияи зеринро созед:

```python
def analyze(numbers):
    pass
```

Функсия бояд баргардонад:

* ҷамъи унсурҳо;
* арзиши миёна;
* унсури калонтарин;
* унсури хурдтарин.

Кори функсияро дар мисоли рӯйхати ададҳо нишон диҳед.

### Масъалаи 4. Кор бо файлҳо

Файли **students.txt**-ро созед.

Корбар номҳои донишҷӯёнро ворид мекунад.

Воридкунӣ то он вақте идома меёбад, ки корбар ворид кунад:

```text
stop
```

Пас аз анҷоми воридкунӣ лозим аст:

1. ҳамаи номҳоро дар файл нигоҳ доред;
2. маълумотро аз файл хонед;
3. рӯйхати донишҷӯёнро аз рӯи тартиби алифбо чоп кунед.

### Масъалаи 5. Барномасозии объектгаро (ООП)

Синфи **Student**-ро созед.

**Майдонҳои синф:**

* `name`
* `age`
* `score`

**Методҳои синф:**

* `show_info()` — маълумот дар бораи донишҷӯро чоп мекунад;
* `increase_score(points)` — холро зиёд мекунад (ҳадди аксар — 100);
* `is_excellent()` — агар хол на камтар аз 90 бошад, `True` ва дар акси ҳол `False` бармегардонад.

Рӯйхатеро аз на камтар аз **5 объекти** синфи `Student` созед.

Чоп кунед:

* маълумот дар бораи ҳамаи донишҷӯён;
* донишҷӯро бо баландтарин хол;
* холи миёнаи тамоми гурӯҳ.

### Масъалаи 6. Бозии «Guess the Number»

Бозиеро созед, ки дар он компютер ба таври тасодуфӣ адади аз **1 то 100**-ро интихоб мекунад.

Корбар бояд ин ададро ҳадс занад.

Пас аз ҳар кӯшиш барнома бояд чоп кунад:

* **«Зиёдтар»**, агар адади интихобшуда калонтар бошад;
* **«Камтар»**, агар адади интихобшуда хурдтар бошад.

Пас аз ҳадс задани адад лозим аст чоп карда шавад:

* шумораи кӯшишҳо;
* вақти сарфшуда барои бозӣ (бо истифодаи модули `datetime`).
