import os.path
import sys

from setuptools import setup

if sys.version_info < (3, 4):
    raise Exception('Asphalt requires at least Python 3.4')

here = os.path.dirname(__file__)
readme = open(os.path.join(here, 'README.rst')).read()
extra_requirements = {(3, 4): ['typing >= 3.5.0b1']}

setup(
    name='asphalt',
    use_scm_version={
        'local_scheme': 'dirty-tag'
    },
    description='An asyncio based microframework for service oriented applications',
    long_description=readme,
    author='Alex Grönholm',
    author_email='alex.gronholm@nextday.fi',
    url='https://github.com/asphalt-framework/asphalt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    license='Apache License 2.0',
    zip_safe=False,
    packages=[
        'asphalt.core'
    ],
    setup_requires=[
        'setuptools_scm >= 1.7.0'
    ],
    install_requires=[
        'setuptools',  # this is here to tell downstream packagers that it needs pkg_resources
        'PyYAML >= 3.11'
    ] + extra_requirements.get(sys.version_info[:2], []),
    extras_require={
        ':python_version == "{}.{}"'.format(major, minor): pkg
        for ((major, minor), pkg) in extra_requirements.items()
    },
    entry_points={
        'console_scripts': [
            'asphalt = asphalt.core.command:main'
        ]
    }
)
