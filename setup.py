from setuptools import setup

setup(
    name='vusic',
    packages=['vusic'],
    version='0.22',
    include_package_data=True,
    description='A CLI to manage scripts!',
    author='vusic',
    author_email='jacob.smith@unb.ca',
    url='https://github.com/vusic/vusic-cli',
    install_requires=[
        'click',
        'Pillow'
    ],
    entry_points={
        'console_scripts': ['vusic=vusic.main:main']
    }
)