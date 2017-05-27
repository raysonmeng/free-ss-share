from setuptools import setup, find_packages
from codecs import open
from os import path

import free_ss_share

here = path.abspath(path.dirname(__file__))


"""
python setup.py develop --record installed_files.txt

python setup.py install --record installed_files.txt
sudo bash -c "cat installed_files.txt | xargs rm -rf"
"""

def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with open('requirements.txt', encoding='utf-8') as reqs:
    install_requires = [l for l in reqs.read().split('\n') if is_pkg(l)]


setup(
    name='free-ss-share',
    version=free_ss_share.__version__,
    description=long_description,
    author=free_ss_share.__author__,
    author_email=free_ss_share.__contact__,
    url=free_ss_share.__homepage__,

    packages=find_packages(
        exclude=['database']
    ),
    install_requires=install_requires,
    include_package_data=True,
    # entry_points={
    #     'console_scripts': [
    #         # "name_of_executable = module.with:function_to_execute"
    #         'spider=shadowsocks_spider.bin:main'
    #     ]
    # }
)
