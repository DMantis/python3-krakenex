from setuptools import setup

from krakenex.version import __version__, __url__

setup(
    name='krakenex',
    version=__version__,
    packages=['krakenex'],
    # package_dir={'': '.'},
    # py_modules=[splitext(basename(path))[0] for path in glob('aioxzen/*.py')],
    url=__url__,
    license='MIT',
    author='Noel Maersk, Dmitry Bogomolov',
    author_email='dmitry.mantis@protonmail.com',
    install_requires=[
        'aiohttp>=3.6.2'
    ],
    description='Minimalistic library to interact with xzen protocol',
    classifiers=[
          'Programming Language :: Python :: 3.7',
    ]
)
