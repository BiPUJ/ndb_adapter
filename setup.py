from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ndb_adapter',
    version=1.0,
    author='Michal Mrozek',
    author_email='michau.mrozek@student.uj.edu.pl',
    url='https://github.com/Michsior14/ndb_adapter',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Adapter for http://ndbserver.rutgers.edu/ created for biologists, bioinformatics etc.',
    long_description=long_description,
    packages='ndb_adapter',
    license='BSD',
    keywords=['ndbserver', 'ndb', 'nucleic acid database', 'adapter'],
    install_requires=['requests', 'xlrd'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Topic :: Database',
            'Topic :: Office/Business',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
    )