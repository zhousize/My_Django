'''
Author: zhoushizhe.vendor zhoushizhe.vendor@sensetime.com
Date: 2022-06-20 14:47:42
LastEditors: zhoushizhe.vendor zhoushizhe.vendor@sensetime.com
LastEditTime: 2022-06-21 11:13:11
FilePath: \django_test\django_test\wsgi.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
WSGI config for django_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
"""
WSGI 即 Web Server Gateway Interface
WEB服务网关接口的配置文件，仅部署项目时使用
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

application = get_wsgi_application()
