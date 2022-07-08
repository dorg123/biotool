from setuptools import setup, find_packages

setup(
    name='biogate',
    version='1.0.0alpha1',
    packages=find_packages(),
    url='https://github.com/dorg188/biogate',
    license='Apache 2.0 License',
    author='Dor Genosar',
    author_email='dor.genosar@outlook.com',
    description='A gateway and multitool for bioinformatic data',
    entry_points={'console_scripts': ['ibio=biogate.ibio:main']},
    install_requires=['ipython', 'requests', 'traitlets']
)
