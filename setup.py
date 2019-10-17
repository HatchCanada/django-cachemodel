from setuptools import setup, find_packages
import os

exec(compile(open(os.path.join(os.path.dirname(__file__), 'cachemodel/version.py')).read(), os.path.join(os.path.dirname(__file__), 'cachemodel/version.py'), 'exec'))


setup(
    name='django-cachemodel',
    version=".".join(map(str, VERSION)),
    packages = find_packages(),

    author = 'Concentric Sky',
    author_email = 'django@concentricsky.com',
    description = 'Concentric Sky\'s cachemodel library',
    license = 'Apache2'
)
