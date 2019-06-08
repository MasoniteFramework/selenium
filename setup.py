from setuptools import setup, find_packages

setup(
    name="masonite-selenium",
    packages=[
        'masonite.testing',
        'masonite.testing.selenium',
        'masonite.testing.drivers.chrome',
        'masonite.testing.drivers.firefox'
    ],
    package_dir={'': 'src'},
    include_package_data=True,
    version='0.0.1',
    install_requires=[
        'selenium>=3.141,<4'
    ],
    description="Selenium Testing Package",
    author="Joseph Mancuso",
    author_email='joe@masoniteproject.com',
    url='https://github.com/MasoniteFramework/masonite',
    keywords=['masonite', 'python web framework', 'python3'],
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        'Operating System :: OS Independent',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',

        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ]
)
