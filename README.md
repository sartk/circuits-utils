# circuits-utils

Usage:

python3 -i circuits.py

```
>>> c = Circuit(fraction_mode=True)
>>> print(c.v_div(1, 2) * c.v_div(1, c.pll(2, 3)) * c.v_div(2, c.pll(2, 1 + c.pll(2, 3))))
1/8
```
