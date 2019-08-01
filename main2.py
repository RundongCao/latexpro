import numpy as np
import scipy as sp
import re
import sys
from types import *

if __name__ == '__main__':
    #str1 = np.loadtxt('Input/image_latex1001-1010.txt', delimiter=',', dtype=np.str, encoding='UTF-8')
    f = open('Input/latex_new_test.txt','r', encoding='UTF-8')
    str1 = f.readlines()
    print(np.shape(str1))

    file = open('Output/latex_new_test_out.txt','w', encoding='UTF-8')

    #print(len(str1[0][:]))
    #str2 = str1[:][1]
    rows = len(str1)
    #print(str2)

    lists = []

    frac_reg = r"\\frac\{[^{}]*\}\{[^{}]*\}"
    # exp_reg1 = "([1-9]\d*\.\d*|0\.\d*[1-9]\d*)\^\{[^{}]*\}"
    exp_reg1 = r"\([^()]+\)\^\d+"
    exp_reg2 = r"\d*\.?\d*\^\{[^{}]*\}"

    delimiter = "-", "*", "+", "=", "(", ")", "/", ">", "<", "[", "]", "...", ":", \
                r"\approx", r"\%", r"\circ", r"\leq", r"\geq", r"\neq", \
                "平方千米", "公顷", "平方米", "平方分米", "平方厘米", "平方毫米", \
                "元", "角", "亿", "万", "千米", "分米", "厘米", "毫米", "公分", "米", \
                "km^3", "m^3", "dm^3", "cm^3", "mm^3", "mL", "L", \
                "km^2", "m^2", "dm^2", "cm^2", "mm^2", "km", "dm", "cm", "mm", "m", \
                "吨", "千克", "克", "公斤", "斤", "kg", "g", "t", "个", "%", \
                "年", "月", "天", "日", "小时", "时", "周", "分钟", "分", "毫秒", "秒"

    regpattern = '|'.join(map(re.escape,delimiter))

    #a1 = re.split(regpattern,str2[0])
    #print(list(filter(lambda a: a!='',a1)))

    num_err = 0
    for i in range(0, rows):
        print(i+1)

        str2 = ''.join(str1[i])
        print(str2)
        str2 = str2.split(' ')[1]

        res, num = re.subn(frac_reg, "FF", str2)
        res, num = re.subn(exp_reg1, "EE", res)
        res, num = re.subn(exp_reg2, "EE", res)
        #print(type(res))

        try:
            #print(res)
            l = re.split(regpattern, res)
            l = list(filter(lambda a: a != '', l))

            index = 0
            for item in l:
                if item is '\n':
                    continue
                if "FF" in item:#r"\frac"
                    l[index] = "分数"
                    res = res.replace(item, "分数")
                elif "EE" in item:
                    l[index] = "指数"
                    res = res.replace(item, "指数")
                elif type(eval(item)) == int:
                    l[index] = "整数"
                    res = res.replace(item, "整数", 1)
                elif type(eval(item)) == float:
                    l[index] = "小数"
                    res = res.replace(item, "小数", 1)

                #print(res)
                index = index + 1
        except Exception as e:
            num_err = num_err + 1
            print(e)
            res = "Error"

        print(res)
        file.write(str1[i].strip('\n'))
        file.write(' ')

        file.write(res.strip('\n'))
        file.write('\n')

        lists.append(l)


    print("Number of error lines is {}".format(num_err))

    #np.savetxt('Output/out1.txt', np.array(lists))
    file.close()