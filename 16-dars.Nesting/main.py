# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$"
#       )

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil {car['narh']}$"    
#           )

# dasturchilar = {
#     'ali':['phyton', 'c++'],
#     'vali':['html', 'css', 'js'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c++', 'c#']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python', 'c++'] 
#         },
#     'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':'o\'rta-maxsus',
#            'tillar':['html', 'css', 'js']
#         },
#     'hasan':{'familiya':'husanov',
#            'tyil':1999,
#            'malumot':'maxsus',
#            'tillar':['python', 'php']
#         }          
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()} "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())