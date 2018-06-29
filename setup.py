from setuptools import setup

setup(
    name='athena',
    packages=['athena'],
    include_package_data=True,
    install_requires=[
        'boto3',
        'PyGithub',
        'docopt'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ]
)
