import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pwdriver',
    version='0.19.0',
    license='MIT',
    author='Jinmoo Han',
    author_email='jinmoo21@naver.com',
    description='It will download a WebDriver, and then set basic configuration automatically.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jinmoo21/pwdriver',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        'certifi>=2021.10.8',
        'chardet>=4.0.0',
        'idna>=3.3',
        'requests>=2.27.1',
        'selenium>=4.1.3',
        'urllib3>=1.26.9'
    ]
)
