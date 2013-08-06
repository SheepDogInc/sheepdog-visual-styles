from setuptools import setup, find_packages

import visual_styles


with open('requirements.txt', 'rb') as f:
    requirements = [line.strip()
                    for line in f.readlines()
                    if not line.startswith('-')]

setup(
    name="sheepdog_modals",
    version=visual_styles.__version__,
    author="The Sheepdog Labs team",
    author_email="development@sheepdog.com",
    description=("Style test app for Django"),
    license="BSD",
    keywords="django examples",
    url="https://github.com/SheepDogInc/sheepdog-visual-styles",
    packages=find_packages(),
    long_description="",
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
