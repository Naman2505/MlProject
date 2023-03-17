from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot = '_e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will install required libraries from requirements.txt file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements

setup(
name='mlProject',
version='0.0.1',
author = 'naman',
author_email = 'naman.tiwari2505@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)