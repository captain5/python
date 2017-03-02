#coding=utf-8
#!/usr/bin/env python
PROJECT = 'cliffdemo'
# Change docs/sphinx/conf.py too!
VERSION = '0.1'
from setuptools import setup, find_packages
try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''
setup(
    name=PROJECT,
    version=VERSION,
    description='Demo app for cliff', #项目描述
    long_description=long_description,
    author='Doug Hellmann',                 #项目作者
    author_email='doug.hellmann@gmail.com', #项目Email
    url='', #项目主页 
    download_url='', #项目下载地址 
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],
    platforms=['Any'], #适用于任何操作系统平台
    scripts=[],
    provides=[],
    install_requires=['cliff'], #安装时需求的模块，这里需要cliff，执行时会自动安装。
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        #主入口
        'console_scripts': [
            'cliffdemo = cliffdemo.main:main'
        ],
        #命令行对应的执行模块，例如files对应的就是cliffdemo.list:Files
        'cliff.demo': [
            'simple = cliffdemo.simple:Simple',
            'two_part = cliffdemo.simple:Simple',
            'error = cliffdemo.simple:Error',
            'list files = cliffdemo.list:Files',
            'files = cliffdemo.list:Files',
            'file = cliffdemo.show:File',
            'show file = cliffdemo.show:File',
			'login = cliffdemo.login:Login',
        ],
    },
    zip_safe=False,
)