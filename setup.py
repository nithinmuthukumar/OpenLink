from setuptools import setup
setup(
    name='openLinks',
    version='0.0.1',
    author='Nithin Muthukumar',
    entry_points={
        'console_scripts': [
            'cli = cli:run'
        ]
    }
)