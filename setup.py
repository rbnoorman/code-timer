from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
    
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup (
 name = 'Pomocodo',
 description = 'A simple commandline timer based on the Pomodoro technique',
 version = '1.0.4',
 packages = find_packages(), # list of all packages
 install_requires = install_requires,
 python_requires='>=3.8', # any python greater than 3.8
 entry_points='''
        [console_scripts]
        pomocodo=pomocodo.__main__:main
    ''',
 include_package_data=True,
 author="Ruben Noorman",
 keyword="pomodoro, cli, terminal, timer, productivity, coding",
 long_description=README,
 long_description_content_type="text/markdown",
 license='MIT',
 url='https://github.com/rbnoorman/code-timer',
 download_url='https://github.com/rbnoorman/code-timer/archive/main.zip',
  dependency_links=dependency_links,
  author_email='rbnoorman@protonmail.com',
  classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
    ]
)