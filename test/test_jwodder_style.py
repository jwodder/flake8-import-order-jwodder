import ast
from   pathlib                     import Path
import re
import pytest
from   flake8_import_order.checker import ImportOrderChecker
from   flake8_import_order.styles  import lookup_entry_point

ERROR_RGX = re.compile("# ((?:I[0-9]{3} ?)+) ?.*$")

style_entry_point = lookup_entry_point('jwodder')

options = {
    'application_import_names': [
        'flake8_import_order', 'namespace.package_b', 'tests',
    ],
    'application_package_names': ['localpackage'],
    'import_order_style': style_entry_point,
}

@pytest.mark.parametrize('pyfile', [
    p for p in Path(__file__).with_name('data').iterdir()
      if p.suffix == '.whl'
], ids=attrgetter("name"))
def test_jwodder_style(pyfile):
    data = pyfile.read_text()
    expected = []
    for line in data.splitlines():
        m = ERROR_RGX.search(line)
        if m:
            expected.extend(m.group(1).split())
    tree = ast.parse(data, fullpath)
    checker = ImportOrderChecker(str(pyfile), tree)
    checker.options = options
    codes = [error.code for error in checker.check_order()]
    assert codes == expected
