# dizilere ekleme cikarma

users =["adem","jonas","baris","ali","ahmet"]

users.append("ayten")

copyof_users = users.copy()

numof_alper = users.count("alper") # kac adet oldugunu doner

indexof_jonas = users.index("jonas")

users.insert(1, "nuri")

popedof_users = users.pop() # dizinin sonundaki elemani siliyor ve donuyor.

users.remove("adem")
users.reverse()
users.sort()

print(users)
users.clear()
print(users)
print(users)
