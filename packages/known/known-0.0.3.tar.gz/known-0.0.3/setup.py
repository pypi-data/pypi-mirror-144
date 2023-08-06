from setuptools import setup

setup(
    name =          'known',
    version =       '0.0.3',  # 0.0.x is for unstable versions
    url =           "https://github.com/NelsonSharma/Public",
    author =        "Nelson.S",
    author_email =  "mail.nelsonsharma@gmail.com",
    description =   '~',
    long_description="~",
    long_description_content_type="text/markdown",
    #py_modules =    [""],
    packages =      ['known'],
    license =       'Apache2.0',
    package_dir =   { '' : 'src'},
    install_requires = [],
    include_package_data=True
)

# cd ..../src
# python38 -m build
# python38 -m twine upload dist/*
# NelsonSharma

# python38 -m pip install -e ./