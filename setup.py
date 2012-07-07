import os
from setuptools import setup, find_packages

from admin_views import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-admin-views',
    version=".".join(map(str, VERSION)),
    description='django-admin-views is a simple way to add custom admin views and direct URLs to the Django admin'
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/frankwiles/django-admin-views',
    packages=find_packages(),
    package_data={
        'admin_views': [
            'templates/admin/*',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

