# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext as tksctxt
import tkinter.ttk as ttk
import pynyac as nyac

def btn1cmd(txtin, txtout, txtnum, locselc):
    txtout.delete('1.0', tk.END)
    try:
        salt = int(txtnum.get('1.0', 'end-1c'))
    except ValueError:
        txtout.insert('1.0', 'Error: Salt is not a valid integer!')
        txtout.tag_add('errorstyle', '1.0', 'end-1c')
        txtout.tag_config('errorstyle', foreground='red')
        return
    txtout.insert('1.0', nyac.nyaencode(txtin.get('1.0', 'end-1c'),
                                        locselc.get(),
                                        salt))

def btn2cmd(txtin, txtout, txtnum, locselc):
    txtout.delete('1.0', tk.END)
    try:
        salt = int(txtnum.get('1.0', 'end-1c'))
    except ValueError:
        txtout.insert('1.0', 'Error: Salt is not a valid integer!')
        txtout.tag_add('errorstyle', '1.0', 'end-1c')
        txtout.tag_config('errorstyle', foreground='red')
        return
    txtout.insert('1.0', nyac.nyadecode(txtin.get('1.0', 'end-1c'),
                                        locselc.get(),
                                        salt))

def main():
    win = tk.Tk()
    win.geometry('800x600')
    tk.Label(win,
             text='Nya 🐈 Encrypt',
             font=('serif', 35),
             fg='green',
             anchor='c').pack()
    win.option_add('*TCombobox*Listbox.font', ('monospace', 12))
    locselc = ttk.Combobox(win,
                           font=('monospace', 12),
                           values=tuple(nyac.nya_locales.keys()))
    locselc.set(list(nyac.nya_locales.keys())[0])
    locselc.place(x=600, y=80)
    locselc_hint = tk.Label(win,
                            text='Locale:',
                            font=('serif', 12))
    locselc_hint.place(x=540, y=80)
    txtfld1 = tksctxt.ScrolledText(win,
                                   wrap=tk.WORD,
                                   font=('serif', 16),
                                   width=28,
                                   height=15)
    txtfld1.place(x=20, y=110)
    txtfld2 = tksctxt.ScrolledText(win,
                                   wrap=tk.WORD,
                                   font=('serif', 16),
                                   width=28,
                                   height=15)
    txtfld2.place(x=410, y=110)
    txtfld3 = tk.Text(win,
                      font=('monospace', 12),
                      height=1,
                      width=32)
    txtfld3.place(x=60, y=80)
    txtfld3_hint = tk.Label(win,
                            text='Salt:',
                            font=('serif', 12))
    txtfld3_hint.place(x=20, y=80)
    btn1 = tk.Button(win,
                     text='Encode Text',
                     font=('monospace', 16),
                     fg='green',
                     command=lambda: btn1cmd(txtfld1, txtfld2, txtfld3, locselc))
    btn1.place(x=150, y=550)
    btn2 = tk.Button(win,
                     text='Decode Text',
                     font=('monospace', 16),
                     fg='green',
                     command=lambda: btn2cmd(txtfld2, txtfld1, txtfld3, locselc))
    btn2.place(x=520, y=550)
    win.mainloop()

if __name__ == '__main__':
    main()
