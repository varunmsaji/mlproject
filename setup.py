from setuptools import find_packages,setup
from typing import List


hypen_e_dot ='-e .'
def get_requirements(filepath:str)-> List[str]:
    '''this functin return list of requirements'''
    requirements=[]
    with open(filepath) as f:
        requirements = f.readlines()
        [req.replace("\n","")for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
     

setup(
    name="mlproject",
    version='0.1.0',
    author = 'varun',
    author_email='varunmsaji01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)