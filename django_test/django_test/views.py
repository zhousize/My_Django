'''
Author: zhoushizhe.vendor zhoushizhe.vendor@sensetime.com
Date: 2022-06-21 11:29:59
LastEditors: zhoushizhe.vendor zhoushizhe.vendor@sensetime.com
LastEditTime: 2022-06-21 15:33:32
FilePath: \django_test\django_test\views.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from django.http import HttpResponse


def print_web1(request):
    #例如增加一个http://127.0.0.1:8000/page/1/ 的返回对象
    return HttpResponse('这是编号为1的网页')


def print_web2(request):
    #例如增加一个http://127.0.0.1:8000/page/2/ 的返回对象
    return HttpResponse('这是编号为2的网页')


def page_num(request,num):
    return HttpResponse(f'这是编号为{num}的网页')


def print_str(request,_str):
    # 增加一个字符串的url地址
    return HttpResponse(f'这是一个字符串为{_str}')


def print_int(request,_int):
    # 增加一个整数的url地址
    return HttpResponse(f'这是一个数字为{_int}')


def print_slug(request,_slug):
    # 增加一个ASSIC字符和特色符合的url地址
    return HttpResponse(f'这是一个ASCII以及字符为{_slug}')


def print_path(request,_path):
    # 增加一个全能的url地址
    return HttpResponse(f'这是一个ASCII以及字符为{_path}')


def print_algo(request,x,y,z):
    # 增加一个算法的url地址
    num = int(x) + int(z)
    return HttpResponse(f'整数{x}加上整数{z}得到的结果为:{num}')
 