"""
Yet another import order style

Visit <https://github.com/jwodder/flake8-import-order-jwodder> for more
information.
"""

__version__      = '0.1.0.dev1'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'flake8-import-order-jwodder@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/flake8-import-order-jwodder'

from flake8_import_order.styles import AppNexus, Google

class JWodder(AppNexus):
    @staticmethod
    def sorted_names(names):
        return sorted(names)

    @staticmethod
    def import_key(import_):
        modules = [Google.name_key(module) for module in import_.modules]
        return (import_.type, import_.level, modules, import_.names)
