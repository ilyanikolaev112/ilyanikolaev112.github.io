s=input("Верблюжий стиль: ")
for c in s:
  if c.isupper():
    print("_", end="")
    print(c.lower(), end="")
  else:
    print(c, end="")
print("")
