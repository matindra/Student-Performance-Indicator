from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of libraries in requirements.txt file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[library_name.replace("\n","") for library_name in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(name='Student Performance Indicator',
      version='0.0.1',
      description='Student Performance Indicator Industry level project',
      author='Matindra Malik',
      author_email='matindramalik@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
      )
