# History

## 0.1.2 (2022-03-29)
- Allows `array_like.__array__()` to throw exceptions.
  - Now, `array_like_info(obj)` degrades to vanilla `repr(obj)` if `obj.__array__()` throws exception. Before, it did nothing, but let caller to handle the exception.
- rename `arraydebug.recover_repr()` to `arraydebug.disable()`.
- rename `arraydebug.inject_repr()` to `arraydebug.enable()`.
  - `enable()` also refresh `arraydebug.repr_fn_table` now.

## 0.1.0 (2022-03-27)

* First release on PyPI.
* Support numpy.ndarray, torch.Tensor.
* Support objects with `__array__` method.
* Setup github CI workflow.
