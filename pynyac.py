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
nya_wordlist = {
    'zh_cn': [
        '喵', '咪', '呜', '呐',
        '嗷', '噜', '呼', '啊',
        '嘛', '呢', '唔', '呣',
        '嘧', '唉', '哦', '呕'
    ],
    'emoji': [
        '🐱', '😸', '😾', '😺', '😻',
        '😼', '😽', '😹', '😿', '🙀'
    ]
}


def nyastep(base):
    "Calculate how many symbols will be used to encode a unicode"
    return math.ceil(math.log(0xfffff, base))


def nyasbox(sz):
    "Generate an sbox, you can customize it as you will"
    sbox = list(range(0, sz))
    for i in range(1, math.ceil(math.sqrt(sz))):
        for j in range(i, sz, i):
            sbox[j-i], sbox[j] = sbox[j], sbox[j-i]
    return sbox


def nyaencode(text, locale):
    "Encode text with locale"
    s = ''
    dlen = len(nya_wordlist[locale])
    step = nyastep(dlen)
    sbox = nyasbox(dlen)
    for c in text:
        n = ord(c)
        for i in range(0, step):
            j = n % dlen
            n //= dlen
            s += nya_wordlist[locale][sbox[j]]
            # state transfer
            sbox.insert(dlen - j, sbox.pop())
    return s


def nyadecode(text, locale):
    "Decode text with locale"
    s = ''
    dlen = len(nya_wordlist[locale])
    step = nyastep(dlen)
    sbox = nyasbox(dlen)
    cnt = 0
    while cnt < len(text):
        n = 0
        b = 1
        for i in range(0, step):
            j = sbox.index(
                nya_wordlist[locale].index(text[cnt + i]))
            n += (b * j)
            b *= dlen
            # state transfer
            sbox.insert(dlen - j, sbox.pop())
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
    for key in nya_wordlist:
        print(key)
    loc = input('Please choose a locale:')
    if mode == 'e':
        print(nyaencode(tmpstr, loc))
    if mode == 'd':
        print(nyadecode(tmpstr, loc))
