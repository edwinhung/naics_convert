from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Naics code translate'
LONG_DESCRIPTION = 'A small library that convert naics codes to names of sectors and industries'

# Setting up
setup(
        name="naics_convert", 
        version=VERSION,
        author="Edwin Hung",
        author_email="edh1912@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy','pandas'], 
        url="https://github.com/edwinhung/naics_convert"
        project_urls={
            "naics_convert":"https://github.com/edwinhung/naics_convert/issues"
        },
        package_data={"": ["*.xlsx"]}, # Include naics data
        keywords=['python', 'naics'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Microsoft :: Windows",
        ],
        python_requires=">=3.6"

)