# -*- coding: gbk-*-
"""
* ���ߣ�������
* ʱ�䣺2022/1/25 14:00
* ���ܣ����Python��������ڷ�����pypi.org
* ˵�����뿴����.txt���ⷢ�����ʹ��ѧ��˼�����������
"""
import sys

from setuptools import setup,find_packages
#from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='algpros',
    version='0.0.3',
    packages=find_packages(),
    url='https://site-5888287-8893-396.mystrikingly.com/',
    license='MIT License',
    author='algfwq',
    author_email='3104374883@qq.com',
    description='��������Ч��̿�pycharm�棬����㼯������Чģ�飬�ɰ�����Ӳ���Ƽ���������������Ҫ���ߣ�����',
    long_description='��������Ч��̿�pycharm�棬����㼯������Чģ�飬�ɰ�����Ӳ���Ƽ���������������Ҫ���ߣ�����',
    requires=["requests"]
)


