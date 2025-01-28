from setuptools import find_packages,setup
from typing import List

HYPHEN_E = "-e ."
def get_requirements(path_to_req: str)-> List[str]:
    '''
        this function will return the list of requirements
    '''
    with open(path_to_req,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
        return requirements
setup(
    name= 'ml boilerplate project',
    version='0.0.1',
    author = 'zeineb73',
    author_email='othmenizaineb@yahoo.fr',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)

