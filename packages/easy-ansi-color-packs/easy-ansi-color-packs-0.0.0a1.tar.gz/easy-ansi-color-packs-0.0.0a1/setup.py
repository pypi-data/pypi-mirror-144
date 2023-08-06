from setuptools import setup, find_packages
from pathlib import Path

version = '0.0.0a1'

readme_file = 'README.md'

description = "RGB Color Packs for use with Easy ANSI."

long_description = Path(readme_file).read_text()

# https://pypi.org/classifiers/
classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Terminals',
    'Typing :: Typed'
]

keywords = 'ANSI, easy, API, console, terminal, colors'

project_urls = {
    'Source': 'https://gitlab.com/easy-ansi/easy-ansi-color-packs',
    # 'Documentation': 'https://gitlab.com/easy-ansi/easy-ansi/-/blob/main/docs/README.md',
    # 'Demos': 'https://gitlab.com/easy-ansi/easy-ansi/-/tree/main/demos',
    'Change Log': 'https://gitlab.com/easy-ansi/easy-ansi-color-packs/-/blob/main/CHANGELOG.md',
    'Issues': 'https://gitlab.com/easy-ansi/easy-ansi-color-packs/-/issues',
    'License': 'https://gitlab.com/easy-ansi/easy-ansi-color-packs/-/blob/main/LICENSE',
    'All Documentation': 'https://gitlab.com/easy-ansi/easy-ansi-docs/-/blob/main/README.md',
    'All Easy ANSI': 'https://gitlab.com/easy-ansi'
}

packages = find_packages(include=['easyansi', 'easyansi.*'])

setup(
    name='easy-ansi-color-packs',
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/easy-ansi/easy-ansi-color-packs',
    author='Joey Rockhold',
    author_email='joey@joeysbytes.net',
    classifiers=classifiers,
    keywords=keywords,
    packages=packages,
    project_urls=project_urls,
    python_requires='>=3.6,<4'
)
