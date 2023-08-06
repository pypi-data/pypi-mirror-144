# ArrayDebug

[![image](https://img.shields.io/pypi/v/arraydebug.svg)](https://pypi.python.org/pypi/arraydebug)
![buld](https://github.com/liqimai/arraydebug/actions/workflows/build.yaml/badge.svg)
[![Updates](https://pyup.io/repos/github/liqimai/arraydebug/shield.svg)](https://pyup.io/repos/github/liqimai/arraydebug/)
[![support-version](https://img.shields.io/pypi/pyversions/arraydebug)](https://img.shields.io/pypi/pyversions/arraydebug)
<!-- [![Documentation Status](https://readthedocs.org/projects/arraydebug/badge/?version=latest)](https://arraydebug.readthedocs.io/en/latest/?version=latest) -->

ArrayDebug generates human-friendly debug information for array-like
objects.

-   Free software: MIT license
-   Support python 3.6+
<!-- -   Documentation: <https://arraydebug.readthedocs.io>. -->

## Usage

All you need is to `import arraydebug` after `numpy`, `torch`, `pandas`, etc.

```python
>>> import numpy as np
>>> import torch
>>> import pandas as pd
>>> ...
>>> import arraydebug # import at last
```

Then you will get information of the array-like object shown in the debugger, like:
```
<Tensor: shape=(6, 4), dtype=float32, device='cpu', requires_grad=True>
```
It works with all debuggers which rely on `repr` function to display variable information.
- VSCode
- IPython
- pdb
- etc.

<!-- TODO: add PyCharm support -->

### VSCode
![](https://raw.githubusercontent.com/liqimai/arraydebug/master/images/vscode.png)


### IPython
```ipython
In [1]: import torch

In [2]: import arraydebug

In [3]: torch.ones(6, 4, requires_grad=True)
Out[3]:
<Tensor: shape=(6, 4), dtype=float32, device='cpu', requires_grad=True>
tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]], requires_grad=True)
```

### pdb
```shell
$ python -m pdb examples/example.py
...
...
...
(Pdb) tensor
<Tensor: shape=(6, 4), dtype=float32, device='cpu', requires_grad=True>
tensor([[0.0833, 0.2675, 0.4372, 0.5344],
        [0.9977, 0.6844, 0.1404, 0.2646],
        [0.7211, 0.7529, 0.1239, 0.2511],
        [0.1717, 0.6611, 0.6598, 0.9705],
        [0.5230, 0.3439, 0.0459, 0.9937],
        [0.8603, 0.6598, 0.0652, 0.1235]], requires_grad=True)
```

<!-- <pre>
<code><span style="color:green">In [1]:</span><span class="pl-k">import</span> torch

<span style="color:green">In [2]:</span><span class="pl-k">import</span> arraydebug

<span style="color:green">In [3]:</span>torch.ones(6, 4, requires_grad=True)
<span style="color:red">Out[3]:</span>
&lt;Tensor: shape=(6, 4), dtype=float32, device='cpu', requires_grad=True&gt;
tensor([[<span class="pl-c1">1.</span>, 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]], requires_grad=True)</code>
</pre> -->



## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
