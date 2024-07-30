from setuptools import setup, find_packages

setup(
    name='test_package01',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add any command line scripts here
        ],
    },
    # Optional
    author='Rahul',
    author_email='rahul.madhavi@sscinc.com',
    description='testmodoule',
    url='https://github.com/rahulmadhavissnc/test_package01',
)
