# python_words = {
#     "integer": "Butun son",
#     "float": "O'nlik son",
#     "boolean": "Mantiqiy qiymat",
#     "for": "Biror amalni qayta-qayta bajarish tsikli",
#     "if": "Shartlarni tekshirish operatori",
# }

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")

# davlatlar = {
#     "aqsh": "washington",
#     "italiya": "rim",
#     "malaziya": "kuala-lumpur",
#     "o'zbekiston": "toshkent",
#     "qirg'iziston": "bishkek",
#     "qozog'iston": "nursulton",
#     "rossiya": "moskva",
#     "singapur": "singapur",
#     "tojikiston": "dushanbe"
# }

# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.title())

# print("Davlatlarning poytaxtlari:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# country = input("Qaysi davlatni poytaxtini bilishni xohlaysiz?\n>>>")
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqda ma'lumot yo'q")
# else:
#     print(f"{country.capitalize()}ning poytaxti {capital.title()} shahri")
    
menu = {
    "osh": 20000,
    "lag'mon": 22000,
    "non": 4000,
    "choy": 5000,
    "shashlik": 12000,
    "somsa": 6000,
    "tabaka": 15000,
}

print("3 ta taom buyurtma bering:>>>")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma.title()} yo'q")    