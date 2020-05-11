import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aiomirai',
    version='0.3.0',
    description='A framework for Tencent QQ headless client \'Mirai\'.',
    author='water_lift',
    author_email='0xWATERx0@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='qq mirai qqbot',
    url='https://github.com/water-lift/aiomirai',
    packages=setuptools.find_packages(include=('aiomirai', 'aiomirai.*')),
    package_data={
        '': ['*.pyi'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        "Framework :: AsyncIO",
        'Framework :: Robot Framework',
        'Framework :: Robot Framework :: Library',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'httpx',
    ],
    extras_require={
        'all': ['quart'],
        'report': ['quart'],
    },
    python_requires='>=3.7',
)
