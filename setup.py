import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aiomirai',
    version='0.0.1',
    description='A framework for Tencent QQ headless client \'Mirai\'.',
    author='water_lift',
    author_email='0xWATERx0@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='qq mirai qqbot',
    url='https://github.com/water-lift/aiomirai',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Framework :: Robot Framework',
        'Framework :: Robot Framework :: Library',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'httpx'
    ],
    python_requires='>=3.8',
)