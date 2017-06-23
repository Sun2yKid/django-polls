import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License', # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://sun2y.me',
    author='Sun2yKid',
    author_email='zhonghua00700@gmail.com',
    classifierss=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11.2', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 2.7.13',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)