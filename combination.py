#!/usr/bin/python
# -*- coding: utf-8 -*-

#################################################
# FileName:combination.py
# Author:ShiLei
# create Date:2017/10/14
# Main Content（Function Name、parameters、returns）
#################################################

import re
from Tkinter import *
import tkMessageBox
from scipy.special import comb

root = Tk()
# 设置窗口名称
root.title("重集的r-组合")
# 设置窗口大小
root.geometry('300x230')
l1 = Label(root, text="r值:")
l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
rvalue = StringVar()
rinput = Entry(root, textvariable=rvalue)
rvalue.set(" ")
rinput.pack()

l2 = Label(root, text="n值:")
l2.pack()
nvalue = StringVar()
ninput = Entry(root, textvariable=nvalue)
nvalue.set(" ")
ninput.pack()

l3 = Label(root, text="k值(逗号作为间隔):")
l3.pack()
kvalue = StringVar()
kinput = Entry(root, textvariable=kvalue)
kvalue.set(" ")
kinput.pack()

def r_conbination(n, r, k):
    result = 0
    regExk = re.compile('^([0-9]*,)*[0-9]*$')
    regExnr = re.compile('^[0-9]+$')
    resultk = regExk.match(k.strip())
    resultn = regExnr.match(n.strip())
    resultr = regExnr.match(r.strip())
    if not resultk:
        tkMessageBox.showinfo(title='warn', message='k参数格式错误')
        return
    if not resultn:
        tkMessageBox.showinfo(title='warn', message='n参数格式错误')
        return
    if not resultr:
        tkMessageBox.showinfo(title='warn', message='r参数格式错误')
        return
    klistArr = [int(i) for i in k.split(',')]
    n = int(n.strip())
    r = int(r.strip())
    if len(klistArr) != n:
        tkMessageBox.showinfo(title='warn', message='k,n参数格式错误')
        return
    string1 = "问题:求解重集B={"
    for q in range(n-1):
        string1 = string1 + str(klistArr[q]) + '*' + 'a' + str(q+1) + ', '
    string1 = string1 + str(klistArr[n-1]) + '*' + 'a' + str(n) + '}的' + str(r) +'-组合数?\n\n'
    string1 += "令S为集合B'的所有"+ str(int(r))+"-组合的集合\n令"
    for i in range(n):
        string1 += 'p' + str(i+1) +'表示S中至少含有' +str(klistArr[i]) +'个a'+str(i+1)+'这一性质\n'
    print string1
    for i in range(pow(2, n)):
        numstr = bin(i).replace('0b', '')
        Fr = r
        sign = 1
        total = 0
        aproperty = []
        for p in range(len(numstr)):
            if numstr[len(numstr)-1-p] == '1':
                Fr = Fr - (klistArr[p] + 1)
                sign *= -1
                total += 1
                aproperty.append('a'+str(p+1))
        if Fr >= 0:
            result += comb(n + Fr - 1, Fr)*sign
        if aproperty:
            print "满足性质" + ','.join(aproperty) + '所对应集合的个数为:F(' + str(n) +',' +str(Fr) +')'
        else:
            print '全集S的个数为:F(' + str(n) +',' +str(Fr)+')'
    string = str("重集B={")
    for q in range(n-1):
        string = string + str(klistArr[q]) + '*' + 'a' + str(q+1) + ', '
    string = string + str(klistArr[n-1]) + '*' + 'a' + str(n) + '}的' + str(r) +'-组合数为:' + str(int(result))
    print string
    tkMessageBox.showinfo(title='结果', message=string)


def on_click():
    R = rvalue.get()
    N = nvalue.get()
    K = kvalue.get()
    r_conbination(N, R, K)


Button(root, text="press", command=on_click).pack()
root.mainloop()

