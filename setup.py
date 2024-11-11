from setuptools import find_packages,setup
from typing import List

HYPEN_E ='-e .'
def get_requirements(file_path:str) ->List[str]:
    requiremnets = []
    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets=[req.replace("\n","") for req in requiremnets]

        if HYPEN_E in requiremnets:
            requiremnets.remove(HYPEN_E)

setup(
    name='mlproject',
    version='0.0.1',
    author='Dhruv',
    author_email='dhruvshrinet@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),

)