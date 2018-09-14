from setuptools import setup


setup(
    name="flask-sql",
    version="v1.0.0",
    license='BSD',
    author='Dong Zhang',
    author_email='785576549@qq.com',
    description='Origin SQL statement for flask',
    packages=['flask_sql'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'SQLAlchemy>=0.8.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
