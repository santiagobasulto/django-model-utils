from setuptools import setup, find_packages
import os.path


"""
long_description = (open('README.rst').read() +
                    open('CHANGES.rst').read() +
                    open('TODO.rst').read())
"""
long_description = "Django model utils"

setup(
    name='model-utils',
    version='0.1',
    description='Django model utilities',
    long_description=long_description,
    author='Santiago Basulto',
    author_email='santiago.basulto@gmail.com',
    url='http://bitbucket.org/carljm/django-model-utils/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    tests_require=["Django>=1.1"],
    test_suite='runtests.runtests'
)
