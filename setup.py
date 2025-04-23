from setuptools import setup, find_packages

setup(
    name='TelegramBot',
    version='1.0',
    description='Telegram Bot for Model Monitoring.',
    url='https://github.com/camgbus/TelegramBot',
    keywords='python setuptools',
    packages=find_packages(include=['tb', 'tb.*']),
)