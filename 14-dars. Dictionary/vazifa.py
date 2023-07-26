ota = {}
ism = input("Otangizni ismini kiriting:\n>>>")
familiya = input("Otangizni familiyasini kiriting:\n>>>")
t_yil = int(input("Tug'ilgan yilini kiriting:\n>>>"))
t_joyi = input("Tug'ilgan joyini kiriting:\n>>>")
ota['ism'] = ism
ota['familiya'] = familiya
ota['t_yili'] = t_yil
ota['t_joyi'] = t_joyi

print(f"Otamning ismi {ota['ism'].title()}, familiyasi {ota['familiya'].title()}, {ota['t_yili']} yilda {ota['t_joyi'].capitalize()} da tug'ilgan")
    