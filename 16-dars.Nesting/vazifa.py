mashxurlar = {
    'abu abdulloh':{
        'familiya': 'muhammad ibn ismoil',
        'tyil': 810,
        'tjoy': 'buxoro',
        'umr': 60,
        'asarlar':['Al-jome\' as-sahih', 'al-adab al-mufrad', 'at-tarix al-kabir', 'at-tarix as-sag\'ir']
    },

    'abdulla':{
        'familiya': 'qodiriy',
        'tyil': 1894,
        'tjoy': 'toshkent',
        'umr': 44,
        'asarlar':['o\'tkan kunlar', 'mehrobdan Chayon', 'obid ketmon']
    },

    'erkin':{
        'familiya': 'vohidov',
        'tyil': 1936,
        'tjoy': 'farg\'ona',
        'umr': 80,
        'asarlar':['tong nafasi', 'qo\'shiqlarim sizga', 'o\'zbegim', 'qiziquvchan Matmusa']
    },

    'alisher':{
        'familiya': 'navoiy',
        'tyil': 1441,
        'tjoy': 'xirot',
        'umr': 60,
        'asarlar':['xamsa', 'lison ut-Tayr', 'mahbub Al-Qulub', 'munojot']
    }, 
}

for ism, info in mashxurlar.items():
    print(f"\n{ism.title()} {info['familiya'].title()} "
          f"{info['tyil']}-yilda {info['tjoy'].capitalize()}da tavallud topgan. "
          f"{info['umr']} yil umr ko'rgan.\n"
          f"{ism.title()} {info['familiya'].title()}ning mashxur asarlari: "     
        )
    for asar in info['asarlar']: 
        print(asar.upper())