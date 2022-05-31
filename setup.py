import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wiktionary_translate',  # How you named your package folder (MyLib)
    version='0.1.1',  # Start with a small number and increase it with every change you make
    license='mpl-2.0',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Get English translations of foreign word with Wiktionary',
    # Give a short description about your library
    author='Marvin Perzi',  # Type in your name
    author_email='hashcod3@protonmail.com',  # Type in your E-Mail
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Persie0/wiktionary_translate',  # Provide either the link to your github or to your website
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",  # I explain this later on
    keywords=['wiktionary', 'dictionary'],  # Keywords that define your package best
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',  # Again, pick a license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
