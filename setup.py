from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api Python Flask'
__long_description__ = 'This is an API to Flask Api planet b2w'

__author__ = 'Vinicius Nascimento'
__author_email__ = 'nascimento.vinicius32@gmail.com'

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/viniciusnascimento95/api-b2w.git',
    keywords='API, MongoDB',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)