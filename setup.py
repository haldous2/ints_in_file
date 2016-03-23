from setuptools import setup, find_packages

setup(
    name='ints_in_file',
    version='0.0.1',
    description='Display percentage of integers in a file',
    url='https://github.com/haldous2/ints_in_file',
    author='Eric Westman',
    author_email='haldous2@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: End Users',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='integers file search',
    packages=find_packages(exclude=['docs','extras',]),
    #install_requires=['mysql-python'],
    # pip install -e .['dev','test]
    extras_require={
        'dev': ['mock>=1.3.0','nose>=1.3.7','webtest>=2.0.18'],
        'test': ['mock>=1.3.0','nose>=1.3.7','webtest>=2.0.18'],
    },
)
