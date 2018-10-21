from setuptools import setup

setup(
    name='vuesic',
    packages=['vuesic'],
    version='0.22',
    include_package_data=True,
    description='A CLI to manage scripts!',
    author='Vuesic',
    author_email='jacob.smith@unb.ca',
    url='https://github.com/vuesic/vuesic-cli',
    install_requires=[
        'click',
        'Pillow'
    ],
    entry_points={
        'console_scripts': ['vuesic=vuesic.main:main']
    }
)