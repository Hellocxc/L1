# -*- coding: utf-8 -*-
print  "哈哈,python"

counter = 100
miles = 1000.0
name = "John"

print counter
print miles
print name

a = b = c = 1
a, b, c = 1, 2, "john"

print a
print b
print c

#字符串或串(String)
str = 'Hello World!'

print "字符串或串(String)------------------"
print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串 

#List（列表）
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print "列表(List)------------------"
print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

#元组(不能二次赋值，相当于只读列表)
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print "元组(Tuple)------------------"
print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

#字典(dictionary)
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print "字典(dictionary)------------------"
print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值

#算术运算符
a = 21
b = 10
c = 0

print "算术运算符------------------"
c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c 

c = a * b
print "3 - c 的值为：", c 

c = a / b
print "4 - c 的值为：", c 

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print "6 - c 的值为：", c

a = 10
b = 5
c = a//b 
print "7 - c 的值为：", c


# 导入 Phone 包
import Phone
 
Phone.Pots()
Phone.Isdn()
Phone.G3()
