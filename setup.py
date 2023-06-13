from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-openai-formatted-response-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_openai_formatted_response_example.ico': ['copy.svg']},
    description='Implementing response of chatGPT(plain text and source) as desktop application with Python',
    url='https://github.com/yjg30737/pyqt-openai-formatted-response-example.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.14',
        'pyperclip',
        'pygments'
    ]
)