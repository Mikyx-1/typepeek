from setuptools import setup, find_packages

setup(
    name='typepeek',
    version='0.2.0',
    author='Le Hoang Viet',
    author_email='lehoangviet2k@gmail.com',
    url='https://github.com/Mikyx-1/typepeek',
    description='A lightweight Python package to infer runtime type hints from real data',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords='type hints, type inference, python types, static typing, runtime analysis',
    platforms='any',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.7',
    install_requires=[
        # No external dependencies for now
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
