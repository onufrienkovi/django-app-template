from setuptools import find_packages
from setuptools import setup

from {{ cookiecutter.app_package }} import VERSION

REQUIREMENTS = ["Django>=2.2", "requests", "typing-extensions", "psycopg2-binary", "environs", "structlog"]

extras_require = {
    "test": ["pytest-cov", "pytest-django", "pytest"],
    "lint": ["flake8", "wemake-python-styleguide", "isort"],
    "doc": ["sphinx-glpi-theme", "sphinx", "rinohtype"],
}

extras_require["dev"] = (
    extras_require["test"] +  # noqa: W504
    extras_require["lint"] +  # noqa: W504
    extras_require["doc"]
)

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="{{ cookiecutter.app_name }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=VERSION,
    url="{{ cookiecutter.url }}",
    extras_require=extras_require,
    packages=find_packages(exclude=["tests", "docs", "scripts"]),
    install_requires=REQUIREMENTS,
    python_requires=">=3.7",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules"],
)
