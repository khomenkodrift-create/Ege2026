from re import finditer

with open() as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = rf'{number}([+*]{number})+' # если в условии "-" то  ([-*]{number})

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

#шаблон можно выучить

from re import finditer
with open() as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = rf'{number}([-*{number}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

from re import finditer:
with open() as file:
    data = file.readline()
number = r'([1-9][0-9]*|0)'
pattern = rf'{number}([+*{number}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))



from re import finditer
with open() as file:
    data = file.readline()
number = r'([1-9][0-9]*|0)'
pattern = rf'({number}([-*{number}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))




from re import finditer
with open() as file:
    data = file.readline()

number = r'([1-9][0-9])*|0'
pattern = rf'({number}([-*{number}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))


from re import finditer
with open() as file:
    data = file.readline()
number = r'([1-9][0-9])*|0'
matches = rf'({number}([+*{number}]))+'
pattern = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

from re import finditer
with open() as file:
    data = file.readline()

number = r'([1-9][0-9])*|0'
pattern = rf'({number}([+*{number}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
