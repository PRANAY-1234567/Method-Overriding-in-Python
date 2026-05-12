# 🔄 Method Overriding in Python

## 📌 Description

This Python program demonstrates the concept of **Method Overriding** in Object-Oriented Programming (OOP).
A child class `B` overrides the `first()` method of parent class `A` while still accessing the parent version using `super()`.

---

## 🚀 Features

* Demonstrates **inheritance**
* Shows **method overriding**
* Uses `super()` to call parent class method
* Executes both parent and child implementations

---

## 🛠️ How It Works

### 1️⃣ Parent Class `A`

Contains:

* `first()`
* `second()`

---

### 2️⃣ Child Class `B`

```python id="t9k3pl"
class B(A)
```

👉 Inherits class `A`

Overrides:

```python id="w3m8qx"
def first(self)
```

Inside overridden method:

```python id="g7x2mv"
super().first()
```

👉 Calls original method from parent class.

Then:

```python id="k2p9zl"
print("Inside new method first")
```

adds new functionality.

---

## 💻 Code

```python id="n4q7xp"
# Method Overriding

class A:
    def first(self):
        print("Inside method first")

    def second(self):
        print("Inside method second")


class B(A):   # Inheriting class A
    def first(self):
        super().first()   # Calling parent class method
        print("Inside new method first")


class Inh4:
    @staticmethod
    def main():
        obj = B()
        obj.first()
        obj.second()


# Calling main method
Inh4.main()
```

---

## ▶️ Output

```id="y8m2qa"
Inside method first
Inside new method first
Inside method second
```

---

## 🧠 Key Concepts

### ✔ Method Overriding

When child class provides its **own implementation** of a parent class method.

```python id="c4x9pt"
def first(self)
```

in class `B` overrides:

```python id="s1k7mv"
def first(self)
```

from class `A`.

---

### ✔ `super()` Keyword

```python id="u6p3zx"
super().first()
```

👉 Calls parent class version of method.

---

### ✔ Runtime Polymorphism

Method executed depends on:

* object type at runtime

---

## 📚 Concepts Used

* Inheritance
* Method overriding
* Runtime polymorphism
* `super()` keyword

---

## 🎯 Advantages of Method Overriding

* Modify inherited behavior
* Extend parent functionality
* Achieve runtime polymorphism

---

## ⚠️ Important Difference

### Without `super()`

Only child method runs.

### With `super()`

Both parent and child methods run.

---

## 🔧 Future Improvements

* Override constructors
* Add multilevel inheritance
* Demonstrate abstract method overriding
* Add method overloading example

---

## 📄 License

This project is open-source and free to use.
