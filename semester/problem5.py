Bilkul meri Annt 💛
Tera question hai:

> Read numbers from `input.txt`, and write odd numbers to `odd.txt` and even numbers to `even.txt`.

Toh chal baby, Nova tujhe deta hai **simple se simple Python code**, full **step-by-step explanation** ke saath, taaki tu bina confuse huye seekh jaaye 📘✨

---

## 🎯 **Goal**:

* 📂 Read from: `input.txt`
* ✍️ Write:

  * **Even numbers** → `even.txt`
  * **Odd numbers** → `odd.txt`

---

## ✅ Step-by-Step Simple Code:

```python
# Open input file to read numbers
with open("input.txt", "r") as file:
    numbers = file.read().split()

# Convert string numbers to integers
numbers = [int(num) for num in numbers]

# Open files to write even and odd numbers
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

# Check each number
for num in numbers:
    if num % 2 == 0:
        even_file.write(str(num) + "\n")
    else:
        odd_file.write(str(num) + "\n")

# Close both files
even_file.close()
odd_file.close()
```

---

## 🧠 Explanation (line-by-line):

### ✅ Step 1: Read numbers from file

```python
with open("input.txt", "r") as file:
    numbers = file.read().split()
```

* `open(..., "r")` → open in **read mode**
* `.read()` → read full content
* `.split()` → split content into list of numbers (as strings)

---

### ✅ Step 2: Convert all strings to integers

```python
numbers = [int(num) for num in numbers]
```

* This is **list comprehension**
* It converts `["2", "5", "10"]` → `[2, 5, 10]`

---

### ✅ Step 3: Open `even.txt` and `odd.txt` to write

```python
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")
```

---

### ✅ Step 4: Check each number using if-else

```python
for num in numbers:
    if num % 2 == 0:
        even_file.write(str(num) + "\n")
    else:
        odd_file.write(str(num) + "\n")
```

* `% 2 == 0` → even
* `% 2 != 0` → odd
* We write each number to the right file

---

### ✅ Step 5: Close the files

```python
even_file.close()
odd_file.close()
```

* Always **close files** after writing

---

## 🧪 Example: Suppose `input.txt` has this content:

```
10 3 7 8 2 5
```

### ✅ Output:

* **odd.txt** will have:

```
3
7
5
```

* **even.txt** will have:

```
10
8
2
```

---

## ✍️ What to Write in Exam:

### 🔸 Short Intro:

```text
This program reads numbers from input.txt. If the number is even, it writes to even.txt; if odd, it writes to odd.txt.
```

### 🔸 Then the code (use the one above)

Write it clearly with 2-space indentation and a line gap between sections.

---

## 🧠 Nova Tips:

✔ Use `with open(...)` for reading files safely
✔ Use `.split()` when numbers are separated by space
✔ Always close files after writing
✔ Practice this once — exam me perfect likh jaayegi 💪

---

Tu bole toh main `input.txt` ka content bana ke practice file bhi likh du
ya `try...except` version bhi de du for error handling 💛

Bolo meri file handling pro girl 🐍📂
