import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]

html_theme_options = {
    'has_sidebar': True,
    'no_sidebar': [
        "singlepage"
    ],
    'toc_title': 'Main Links'
}

html_theme = 'garri'