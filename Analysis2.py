import numpy as np
import scipy as sp
import re
import sys
import pandas as pd
#from sets import Set

from types import *

if __name__ == '__main__':
    f = open('Output/image_latex1001-1010_out.txt', 'r', encoding='UTF-8')
    str1 = f.readlines()

    #data1 = str1[:, 2]
    #data1 = np.concatenate((str1[:, 2], str2[:, 2], str3[:, 2], str4[:, 2]), axis=0)
    rows = len(str1)

    print("Number of rows is {}".format(rows))

#    result = set(data)
#    print(result)
#    print(len(result))

    d = {'纯分数': 0,
         '分数和整数': 0,
         '分数和小数': 0,
         '分数整数小数混合': 0,
         '含指数': 0,
         '百分数': 0,
         '纯整数四则运算': 0,
         '纯小数四则运算': 0,
         '混合四则运算': 0,
         '带字母单位': 0,
         '带汉字单位': 0,
         '约等于': 0,
         '有余数除法': 0,
         '比例': 0,
         '整数比大小': 0,
         '带括号填写': 0,
         '整数大小填写': 0,
         '小数大小填写': 0,
         '分数大小填写': 0,
         '百分数大小填写': 0,
         '长度单位大小填写': 0,
         '面积单位大小填写': 0,
         '体积单位大小填写': 0,
         '重量单位大小填写': 0,
         '时间单位大小填写': 0,
         'Error': 0}

    #d['含指数'] = d['含指数'] + 1
    #print(d['含指数'])

    #df = pd.DataFrame(data = d)
    #print(df.dtypes)

    delimiter1 = "平方千米", "公顷", "平方米", "平方分米", "平方厘米", "平方毫米", \
                 "元", "角", "亿", "万", "千米", "分米", "厘米", "毫米", "公分", "米", \
                 "吨", "千克", "克", "公斤", "斤", "个" \
                 "年", "月", "天", "日", "小时", "时", "周", "分钟", "分", "毫秒", "秒"

    delimiter2 = "km^3", "m^3", "dm^3", "cm^3", "mm^3", "mL", "L", \
                 "km^2", "m^2", "dm^2", "cm^2", "mm^2", "km", "dm", "cm", "mm", "m", \
                 "kg", "g", "t"

    delimiter3 = "+", "-", "*", "/"

    ld = "千米", "分米", "厘米", "毫米", "公分", "米", "km", "dm", "cm", "mm", "m"
    sd = "平方千米", "公顷", "平方米", "平方分米", "平方厘米", "平方毫米", "km^2", "m^2", "dm^2", "cm^2", "mm^2"
    vd = "km^3", "m^3", "dm^3", "cm^3", "mm^3", "mL", "L"
    md = "吨", "千克", "克", "公斤", "斤", "kg", "g", "t"
    td = "年", "月", "天", "日", "小时", "时", "周", "分钟", "分", "毫秒", "秒"

    regpattern1 = '|'.join(map(re.escape, delimiter1))
    regpattern2 = '|'.join(map(re.escape, delimiter2))
    regpattern3 = '|'.join(map(re.escape, delimiter3))

    regpattern4 = '|'.join(map(re.escape, ld))
    regpattern5 = '|'.join(map(re.escape, sd))
    regpattern6 = '|'.join(map(re.escape, vd))
    regpattern7 = '|'.join(map(re.escape, md))
    regpattern8 = '|'.join(map(re.escape, td))

#    Count each class
    for i in range(0, rows):

        str2 = ''.join(str1[i])
        print(str2)
        data1 = str2.split(' ')[2]


        if '分数' in data1:
            if '整数' in data1:
                if '小数' in data1:
                    d['分数整数小数混合'] = d['分数整数小数混合'] + 1
                else:
                    d['分数和整数'] = d['分数和整数'] + 1
            else:
                if '小数' in data1:
                    d['分数和小数'] = d['分数和小数'] + 1
                else:
                    d['纯分数'] = d['纯分数'] + 1

        if '指数' in data1:
            d['含指数'] = d['含指数'] + 1

        if '%' in data1:
            d['百分数'] = d['百分数'] + 1

        if r"\approx" in data1:
            d['约等于'] = d['约等于'] + 1

        if "..." in data1:
            d['有余数除法'] = d['有余数除法'] + 1

        if ":" in data1:
            d['比例'] = d['比例'] + 1

        if (">" in data1) or ("<" in data1):
            if "(整数)" in data1:
                d['整数比大小'] = d['整数比大小'] + 1

        if (">" in data1) or ("<" in data1):
            if re.search(regpattern4, data1):
                d['长度单位大小填写'] = d['长度单位大小填写'] + 1
            if re.search(regpattern5, data1):
                d['面积单位大小填写'] = d['面积单位大小填写'] + 1
            if re.search(regpattern6, data1):
                d['体积单位大小填写'] = d['体积单位大小填写'] + 1
            if re.search(regpattern7, data1):
                d['重量单位大小填写'] = d['重量单位大小填写'] + 1
            if re.search(regpattern8, data1):
                d['时间单位大小填写'] = d['时间单位大小填写'] + 1

            if '整数' in data1:
                d['整数大小填写'] = d['整数大小填写'] + 1

            if '小数' in data1:
                d['小数大小填写'] = d['小数大小填写'] + 1

            if '分数' in data1:
                d['分数大小填写'] = d['分数大小填写'] + 1

            if '%' in data1:
                d['百分数大小填写'] = d['百分数大小填写'] + 1

        if "Error" in data1:
            d['Error'] = d['Error'] + 1

        if "(" in data1 and ")" in data1:
            d['带括号填写'] = d['带括号填写'] + 1

        if re.search(regpattern1, data1):
            d['带汉字单位'] = d['带汉字单位'] + 1

        if re.search(regpattern2, data1):
            d['带字母单位'] = d['带字母单位'] + 1

        if "分数" not in data1:
            if "指数" not in data1:
                if re.search(regpattern3, data1):
                    if "整数" in data1:
                        if "小数" not in data1:
                            d['纯整数四则运算'] = d['纯整数四则运算'] + 1
                        else:
                            d['混合四则运算'] = d['混合四则运算'] + 1
                    else:
                        if "小数" in data1:
                            d['纯小数四则运算'] = d['纯小数四则运算'] + 1

        print(i)

    print(d)