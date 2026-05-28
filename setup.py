
from setuptools import setup,find_packages

def get_requirement()->list[str]:
    try:
        requirements_lst:list[str]= []
    
        with open("requirements.txt","r") as file:
            lines = file.readlines()
            
            for line in lines:
                requirement = line.strip()

                if requirement and requirement!= "-e .":
                    requirements_lst.append(requirement)
                
    except FileNotFoundError:
        print("requirement.txt file not found!!")
    return requirements_lst

print(get_requirement())

setup(
    name="Network Security",
    version="1.0.0",
    author="Sparsh Sharma",
    author_email ="sparshsharma0303@gmail.com",
    packages=find_packages(),
    install_requires= get_requirement()
    

    )
