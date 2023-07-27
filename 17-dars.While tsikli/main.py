# ism = input("Ismingiz nima? ")
# familiya = input("Familiyangiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechchida? "
# yosh = int(input(savol))
# height = float(input("Bo'yingiz nechchi metr? "))

# print(f"Foydalanuvchi {ism.title()} {familiya.title()}. {yosh} yoshda. Bo'yi {height} metr!")

# son = 1
# while son <= 5:
#     print(son)
#     son += 1
# print("Dastur tugadi")

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)    
#     else:
#         print("Dastur tugadi!")

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!") 

son = 0
while son < 10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
