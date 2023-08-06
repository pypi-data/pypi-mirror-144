import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
name="smallPowerDash",
version="4.3.2",
author="Dorian Drevon",
author_email="drevondorian@gmail.com",
description="source codes and config Files to monitor small power data",
long_description=long_description,
long_description_content_type="text/markdown",
# url="https://github.com/pypa/sampleproject",
# project_urls={
#     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
# },
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
# packages=setuptools.find_packages(),
packages=['smallPowerDash'],
# packages=setuptools.find_packages(exclude=["quickTest"]),
package_data={'': ['confFiles/*','confFiles/pictures/*']},
include_package_data=True,
install_requires=['dorianUtilsModulaire==4.3.2','openpyxl==3.0.7'],
python_requires=">=3.8"
)
