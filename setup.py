from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='zetemple',
    version='1.0.0',
    url='https://github.com/sasaki77/zetemple',
    license=license,
    maintainer='Shinya Sasaki',
    maintainer_email='shinya.sasaki@kek.jp',
    description='EPICS client to send metrics '
                'from IOC to Zabbix with host template',
    long_description=readme,
    packages=find_packages(exclude=('tests', 'scripts')),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zabbix_utils',
        'zabbix-epics-py',
    ],
    extras_require={
        'develop': [
            'pytest',
            'pytest-cov',
            'pycodestyle'
            ]
    },
    entry_points={
        'console_scripts': ['zetemple=zetemple.zetemple:main'],
    },
)
