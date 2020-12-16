#因为函数要先定义再调用
#2.确定选择功能界面:显示余额，存款  取款
def sel_func():
    print('显示余额')
    print('存款')
    print('取款')

#3.封装函数

#1.搭建整体框架
"""输入密码登陆后显示功能；查询余额后显示功能；取完钱之后显示功能"""
print('恭喜您登陆成功')
#显示功能界面
sel_func()
print('您的余额是10000')
#显示功能界面
sel_func()

print('取了100元')
#显示功能界面
sel_func()

#4.在需要的位置调用函数


#函数注意事项 1.使用一个函数 2.测试注意事项
#需求：打印hello world
#定义函数
def info_print():
    print('hello world')
#调用函数
info_print()


"""
结论：
1.函数先定义再调用
2.没有调用函数，函数里边的代码不会执行
3.当调用函数时，解释器会回到定义函数的地方执行缩进的代码，执行完毕后，回到调用函数的地方继续向下执行
    定义函数时，函数体内部缩进的代码并没有执行
"""

# 固定函数
def add_num1():
    result=1+2
    print(result)

add_num1()
# 参数传入正式数据  做加法运算
def add_num2(a,b):  # a,b为形参
    result=a+b
    print(result)

add_num2(10,20) # 10，20为实参
add_num2(10,202)

def buy():
    return 'okok'
    print('222')    # 未执行

# 使用变量保存函数返回值
goods=buy()
print(goods)

# return 返回结果给函数调用的地方，退出当前函数

# 需求：制作一个计算器，
















