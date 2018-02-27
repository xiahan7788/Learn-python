# -*- coding: utf-8 -*-
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y 

hilarious = False
# 仅仅是定义变量，没有指代格式化内容
joke_evaluation = "Isn't that joke so funny?! %r:"

#这里打印了格式化的内容，用 /r 内容更宽泛，后面是布尔常量
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# 加号并不只是代表计算数字
print w + e 