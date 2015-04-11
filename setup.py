from setuptools import setup

setup(
    name='natty',
    version='0.2.0',
    packages=['natty'],
    package_data={
        'natty': [
            'data/natty-basic-parser-0.2.0.jar'
        ],
    },
    install_requires=[
        'JPype1',
        'python-dateutil'
    ],
    author='Edward Stone',
    author_email='edwardjstone@yahoo.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
    keywords='natty',
    license='MIT',
    description='Python interface to Natty Date Parser'
)
