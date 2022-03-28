# -*- coding=utf-8 -*-
"""
A nice unicode text encrytion method for cats and their servants
Very useful when you do not want to let a robot know what you said

by gynamics(^@_@^)
"""

import io
import math


"""
I have no wise method to generate this dynamically
Pityfully, sequences are not supported.
"""
nya_locales = {
    'zh_cn': [
        '喵', '咪', '呜', '呐',
        '嗷', '噜', '呼', '啊',
        '嘛', '呢', '唔', '呣',
        '嘧', '唉', '哦', '呕'
    ],
    'emoji': [
        '🐱', '😸', '😾', '😺', '😻',
        '😼', '😽', '😹', '😿', '🙀'
    ],
    'bb64':  # this is not base64!
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
    'wsp': [
        ' ', '\t', '\n'
    ]
}

def nyastep(base):
    "Calculate how many symbols will be used to encode a unicode"
    return math.ceil(math.log(0xfffff, base))


def nyasbox(nyaclist, salt=1145141919810):
    "Generate an sbox, you can customize it as you will"
    sz = len(nyaclist)
    sbox = list(range(0, sz))
    for i in range(1, math.ceil(math.sqrt(sz))):
        for j in range(i, sz, i):
            sbox[j-i], sbox[j] = sbox[j], sbox[j-i]
    # salting
    k = 0
    for i in range(1, sz):
        n = ord(nyaclist[i])
        j = (i * ((salt // i) - n) // salt) % sz  # what the fuck?
        k = (k + (salt // i) - (n // salt)) % sz
        sbox[j], sbox[k] = sbox[k], sbox[j]
    return sbox


def nyaencode(text, locale):
    "Encode text with locale"
    s = ''
    sbox = nyasbox(nya_locales[locale])
    dlen = len(nya_locales[locale])
    step = nyastep(dlen)
    for c in text:
        n = ord(c)
        for i in range(0, step):
            j = n % dlen
            n //= dlen
            s += nya_locales[locale][sbox[j]]
            # state transfer
            sbox.insert(j, sbox.pop())
            sbox.insert(dlen - j, sbox.pop(0))
    return s


def nyadecode(text, locale):
    "Decode text with locale"
    s = ''
    sbox = nyasbox(nya_locales[locale])
    dlen = len(nya_locales[locale])
    step = nyastep(dlen)
    cnt = 0
    while cnt + step <= len(text):
        n = 0
        b = 1
        for i in range(0, step):
            j = sbox.index(
                nya_locales[locale].index(text[cnt + i]))
            n += (b * j)
            b *= dlen
            # state transfer
            sbox.insert(j, sbox.pop())
            sbox.insert(dlen - j, sbox.pop(0))
        s += chr(n)
        cnt += step
    return s


def nyadecf(fin, fout, locale, coding='utf-8'):
    "Decode an input file to output file with locale"
    with io.open(fin, 'r', encoding=coding) as stin:
        text = stin.read()
    with io.open(fout, 'w', encoding=coding) as stout:
        stout.write(nyadecode(text, locale))


def nyaencf(fin, fout, locale, coding='utf-8'):
    "Encode an input file to output file with locale"
    with io.open(fin, 'r', encoding=coding) as stin:
        text = stin.read()
    with io.open(fout, 'w', encoding=coding) as stout:
        stout.write(nyaencode(text, locale))


if __name__ == '__main__':
    tmpstr = input('Input some text:')
    mode = input('Encode or decode(e/d)')
    print('Availiable locales:')
    for key in nya_locales:
        print(key)
    loc = input('Please choose a locale:')
    if mode == 'e':
        print(nyaencode(tmpstr, loc))
    if mode == 'd':
        print(nyadecode(tmpstr, loc))
