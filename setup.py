from setuptools import setup, find_packages

setup(
    name='opendownloader',
    version='2024.04.01',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests-futures',
        'tqdm',
        'typer'
    ],
    entry_points='''
        [console_scripts]
        opendownloader=src.main:main
    ''',
    author='Uppriez Development',
    author_email='info.neixproducer@gmail.com',
    description='A command-line tool for downloading files from URLs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/uppriezdev/OpenDownloader',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: Windows :: Mac :: Linux',
    ],
)
