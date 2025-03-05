from setuptools import setup

setup(
    name='servico-restful-python',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'SQLAlchemy',
        'Flask-SQLAlchemy',
        'Flask-Seeder'
    ]
)