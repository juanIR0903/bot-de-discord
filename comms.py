import random as r, string as s, discord as d, os
i = ""
largo = 25

def psw (lend):

    elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation

    password = ''

    for i in range(lend):
        password += r.choice(elements)
    return password

def flip_coin():
    coin = ['😀CARA', '✝️CRUZ']
    return r.choice(coin)

def memes():
    memesdir = r.choice(os. listdir("image"))
    with open (f"image/{memesdir}", "rb") as img:
        picture = d.File(img)
    return picture

def psw (calcu):

    calculo = ""

    love = ""

    for i in range(calcu):
        love += r.choice(calculo)
    return love