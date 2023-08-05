from setuptools import setup, find_packages
'''
python setup.py sdist
twine upload dist/*
'''

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='OSF_EIMTC',
    version='0.1.17',
    description='A Framework for Encrypted Internet and Malicious Traffic Classification.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/neyney10/PCAPFeatureExtractor',
    keywords='nfstream, pcap, network, deep-learning, extraction',
    license='MIT',
    author="Ariel University",
    author_email='ofek.bader@msmail.ariel.ac.il',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'EIMTC': ['tools/*'],
    },
    install_requires=[
        'scikit-learn',
        'NFStream',
        'pandas',
        'numpy',
        'scapy',
        'pyasn',
        'click',
    ],
)