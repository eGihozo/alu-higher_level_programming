# Python 3: Mutable, Immutable... Everything Is an Object!

![Cover picture: add your image here](your-image-url)

## Introduction

In Python, everything is an object: numbers, strings, lists, functions, even classes. Every variable is a name that points to an object in memory. Once you understand that, many surprises disappear, like why changing one list can silently change another. This post covers `id` and `type`, mutable and immutable objects, and how Python passes arguments to functions.

## id and type

`type()` tells you the class of an object. `id()` returns its identity, which in CPython is its memory address.

```python
>>> a = 89
>>> type(a)
<class 'int'>
>>> id(a)
10105184
>>> b = a
>>> id(b) == id(a)
True
```

`==` compares values, while `is` compares identity (same `id`).

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2
True
>>> l1 is l2
False
```

## Mutable objects

A mutable object can be changed in place after it is created, and its `id` stays the same. The built-in mutable types are `list`, `dict`, `set` and `bytearray`.

```python
>>> l = [1, 2, 3]
>>> id(l)
140234567890
>>> l.append(4)
>>> l
[1, 2, 3, 4]
>>> id(l)
140234567890
```

## Immutable objects

An immutable object cannot be changed after creation. Any "change" creates a new object. The built-in immutable types are numbers (`int`, `float`, `complex`), `bool`, `str`, `tuple`, `frozenset` and `bytes`.

```python
>>> a = 1
>>> id(a)
10105056
>>> a += 1
>>> id(a)
10105088
```

An immutable object is stored once in memory, and variables are just references to it.

Memory schema 1, assignment and aliasing of an immutable int:

```
a = 89         a --+
b = a          b --+--> [ int 89 ]

a = a + 1      a ----> [ int 90 ]
               b ----> [ int 89 ]   (unchanged)
```

Memory schema 2, alias of a mutable list:

```
l1 = [1, 2, 3]   l1 --+
l2 = l1          l2 --+--> [ 1, 2, 3 ]

l1.append(4)     l1 --+
                 l2 --+--> [ 1, 2, 3, 4 ]
```

## Why it matters and how Python treats them differently

Assignment (`b = a`) never copies an object. It makes a second name (an alias) for the same object. With immutable objects this is safe, because the object can never change under you. With mutable objects it is not, because a change through one name is visible through every other name.

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]   # builds a NEW list
>>> l2
[1, 2, 3]
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 += [4]       # extends IN PLACE
>>> l2
[1, 2, 3, 4]
```

To get an independent copy, use `l[:]` or `l.copy()`.

**Integer pre-allocation.** CPython creates the integers from -5 to 256 (262 objects) at startup and reuses them. In the CPython source these limits are `NSMALLNEGINTS` (5) and `NSMALLPOSINTS` (257, so the range goes up to 256). Whenever your code needs an int in that range, CPython returns the existing object instead of creating a new one. These values were chosen because small integers are the most used in programs, so reusing them saves memory and time.

```python
>>> a = 89
>>> b = 89
>>> a is b
True
>>> a = 1000
>>> b = 1000
>>> a is b
False
```

**Special case: tuples and frozensets.** They are immutable, but they can contain mutable objects. The container cannot change, but the objects inside it can.

```python
>>> t = ([1, 2], 3)
>>> t[0].append(99)
>>> t
([1, 2, 99], 3)
```

Also remember that `(1)` is just an int, and a one-element tuple needs a comma: `(1,)`.

## How arguments are passed to functions

Python passes arguments by assignment: the parameter becomes a new name for the same object. For an immutable object, rebinding the parameter does not affect the caller. For a mutable object, modifying it in place does.

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)        # 1 (int is immutable)

def append_four(n):
    n.append(4)

l = [1, 2, 3]
append_four(l)
print(l)        # [1, 2, 3, 4] (list is mutable)

def assign_value(n, v):
    n = v       # only rebinds the local name

l1, l2 = [1, 2, 3], [4, 5, 6]
assign_value(l1, l2)
print(l1)       # [1, 2, 3]
```

## Conclusion

Know whether an object is mutable, remember that names are references, and use `is`, `id` and copies when you need to be sure. That removes most of Python's "mysterious" behaviour.
