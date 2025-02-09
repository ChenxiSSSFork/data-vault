from pytest import raises
from data_vault.parameters import ParametresValidator
from test_integration import patch_ipython_globals


def test_method():
    validator = ParametresValidator()
    import json
    with patch_ipython_globals({'json': json}):
        assert validator.function('json.loads')
    
    with patch_ipython_globals({'json': json}):
        with raises(AttributeError):
            validator.function('json.does_not_exist')
