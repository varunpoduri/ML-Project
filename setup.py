from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str) ->  List[str]:
    '''
    this function will return the list of req
    '''
    requirements=[]
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace('\n', ' ')  for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



setup(
    name='mlproject',
    version='0.1.0',
    author='Varun P',
    author_email='varunpoduri@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)