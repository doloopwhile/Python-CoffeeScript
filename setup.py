#python3
#encoding: shift-jis
from distutils.core import setup
import sys
import io
import execjs

with io.open('README.md', encoding='ascii') as fp:
    long_description = fp.read()

setup(
    packages=['coffeescript'],
    package_dir={'coffeescript': 'coffeescript'},
    package_data={
        'coffeescript': ['*.js'],
    },
    data_files = [
        ('', 'README.md LICENSE'.split()),
    ],
    name='CoffeeScript',
    version=execjs.__version__,
    description='A bridge to the JS CoffeeScript compiler',
    long_description=long_description,
    author='Omoto Kenji',
    author_email='doloopwhile@gmail.com',
    url='https://github.com/doloopwhile/coffeescript',
    
    license=execjs.__license__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.2',
        'Programming Language :: JavaScript',
        'Programming Language :: CoffeeScript',
    ],
)
