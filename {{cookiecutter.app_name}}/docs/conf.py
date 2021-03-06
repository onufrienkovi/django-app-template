import os
import sys
from contextlib import suppress
from {{ cookiecutter.app_package }} import VERSION

sys.path.insert(0, os.path.abspath('..'))

with suppress(ImportError):
    import django  # noqa: WPS433

    # Normal django setup. That's how it should be in development:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()


project = "{{ cookiecutter.app_name }}"
author = "{{ cookiecutter.author }}"
author_email = "{{ cookiecutter.author_email }}"
copyright = f"2020, {author} <{author_email}>"  # noqa: A001

version = VERSION
release = VERSION

needs_sphinx = '1.8'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',

    # 3rd party, order matters:
    # https://github.com/wemake-services/wemake-django-template/issues/159
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
source_suffix = ['.rst']
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'alabaster'
html_theme_options = {}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
    ],
}


