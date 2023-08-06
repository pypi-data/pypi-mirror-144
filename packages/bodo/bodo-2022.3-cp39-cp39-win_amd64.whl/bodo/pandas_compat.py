import hashlib
import inspect
import warnings
import pandas as pd
_check_pandas_change = False


def _set_noconvert_columns(self):
    assert self.orig_names is not None
    eyss__ghke = {dfqgf__awybi: pzp__dqyz for pzp__dqyz, dfqgf__awybi in
        enumerate(self.orig_names)}
    bup__qbn = [eyss__ghke[dfqgf__awybi] for dfqgf__awybi in self.names]
    bks__fmref = self._set_noconvert_dtype_columns(bup__qbn, self.names)
    for ieu__fldy in bks__fmref:
        self._reader.set_noconvert(ieu__fldy)


if _check_pandas_change:
    lines = inspect.getsource(pd.io.parsers.c_parser_wrapper.CParserWrapper
        ._set_noconvert_columns)
    if hashlib.sha256(lines.encode()).hexdigest(
        ) != 'afc2d738f194e3976cf05d61cb16dc4224b0139451f08a1cf49c578af6f975d3':
        warnings.warn(
            'pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns has changed'
            )
pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns = (
    _set_noconvert_columns)
