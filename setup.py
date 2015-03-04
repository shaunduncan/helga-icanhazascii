from setuptools import setup, find_packages


setup(
    name='helga-icanhazascii',
    version='0.1.0',
    description="A helga match plugin that will show ASCII art for certain keywords.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Framework :: Twisted',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='helga icanhazascii ascii art',
    author="Shaun Duncan",
    author_email="shaun.duncan@gmail.com",
    url="https://github.com/shaunduncan/helga-icanhazascii",
    packages=find_packages(),
    py_modules=['helga_icanhazascii'],
    include_package_data=True,
    zip_safe=True,
    entry_points=dict(
        helga_plugins=[
            'icanhazascii = helga_icanhazascii:icanhazascii',
        ],
    ),
)
