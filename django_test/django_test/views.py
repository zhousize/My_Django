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
    if request.method == 'GET':  # HTTP请求方法
        name = request.GET.get('name', 'zhangsan')
        age = request.GET.get('age', '18')
        name_list = request.GET.getlist('name')
    if request.method == 'POST':
        name = request.POST.get('name', 'zhangsan')
        age = request.POST.get('age', '18')
        name_list = request.GET.getlist('name')
    url = request.path_info  # URL字符串
    cookies = request.COOKIES  # 包含所有的cookie，键和值都为字符串
    session = request.session  # 似于字典的对象，表示当前的会话
    body = request.body  # 请求体的内容(POST或PUT)
    scheme = request.scheme  # 请求协议('http'/'https')
    path = request.get_full_path()  # 请求的完整路径
    host_url = request.get_host()  # 请求的主机
    mag_head = request.META  # 请求中的元数据(消息头)
    client_url = request.META['REMOTE_ADDR']  # 客户端IP地址
    print(f'这是：{request.method}方法')
    print(f'姓名：{name},年纪:{age},所有人:{name_list}')
    print(f'url字符串:{url}')
    print(f'cookies:{cookies}')
    print(f'session:{session}')
    print(f'body:{body}')
    print(f'请求协议：{scheme}')
    print(f'完整的路径是：{path}')
    print(f'主机：{host_url}')
    print(f'消息头:{mag_head}')
    print(f'客户端地址:{client_url}')
    return HttpResponse(f'这是一个ASCII以及字符为{_path}')


def print_algo(request,x,y,z):
    # 增加一个算法的url地址
    num = int(x) + int(z)
    return HttpResponse(f'整数{x}加上整数{z}得到的结果为:{num}')
 