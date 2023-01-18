def foobar(n):
    if n%5 == 0 and not (n%7 == 0):
        return "Foo"
    elif n%7 == 0 and n%5 != 0:
        return "Bar"
    elif n%5 == 0 and n%7 == 0:
        return str(n)
    elif n%5 != 0 or n%7 != 0:
        return "FooBar"


print(foobar(3))
print(foobar(5))
print(foobar(7))
print(foobar(35))#35
print(foobar(54684687))#FooBar
print(foobar(1))#FooBar