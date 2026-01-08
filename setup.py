from setuptools import setup, find_packages

setup(
    name='TDDICPAC',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pypost7D @ git+https://gitlab.com/symmehub/py7DPost.git',
        'pandas',
        'numpy',
        'matplotlib',
        'scipy',
        'ipympl',
        'jupyterlab',
    ],
    include_package_data=True,
    description='Description de votre package',
    author='Emile Roux',
    author_email='emile.roux@univ-smb.fr',
    url='https://github.com/EmileRouxSMB/MECA-DIC-TDPAC',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
