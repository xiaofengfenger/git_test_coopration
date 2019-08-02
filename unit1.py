'''import random,string

def random_str(num,length=8):
    fp=open("result.txt",'wb')
    for i in range(num):
        chars=string.ascii_letters+string.digits
        for i in range(length):
            s=random.choice(chars)
            fp.write(''.join(s)+'\n')
    fp.close()


if __name__ == "__main__":
    random_str(20)'''




# -*- coding:utf-8 -*-
#**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random, string

def random_str(num, length = 7):
    f = open("Running_result.txt", 'wb')
    for i in range(num):                                         #range就是一个序列 缺省从0开始 num-1结束
        chars = string.ascii_letters + string.digitsc       #此处设计string的几个函数，分别有获取不同字符串的作用
        s = [random.choice(chars) for i in range(length)]        #初步猜测是和先写for再写随机获值赋值一样
            f.write(''.join(s) + '\n')
    f.close()

if __name__ == '__main__':
    random_str(200)
