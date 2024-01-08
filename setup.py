from setuptools import setup, find_packages

VERSION = "0.0.0"

DESCRIPTION = ('Nexo: A versatile Python web framework that combines simplicity with powerful features, '
               'offering an efficient solution for web development.')

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="nexo",
    version=VERSION,
    author="Muhammad Fiaz",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/muhammad-fiaz/nexo',
    packages=find_packages(),
    keywords=[
        'python', 'web framework', 'web development', 'nexo'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',
    install_requires=[

    ],
    license='MIT License',
    project_urls={
        'Source Code': 'https://github.com/muhammad-fiaz/nexo',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/nexo/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/nexo#readme'
    },
)

print("Happy Coding!")
