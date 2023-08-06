# mrange

Install via 
`conda install numba`
`pip install mrange`

Import via
`from mrange import mrange`

## Description
mrange is used to remove nested range loops
### Input: 
`n_s = (n_1, n_2, ..., n_m)` 
Tuple of integers (or array when using `mrange_array`)
### Output: 
Generator outputting `len(n_s)` values with every call, generating every combination of values in the intervals `[0,1,...,n_s[i]-1]`
### Use:
```
for a, b, ..., m in mrange((n_a, n_b, ..., n_m)):
    ...
Replaces:
for a in range(n_a):
    for b in range(n_b):
       ...
           for m in range(n_m):
               ...
```
## Authors: 
By Michael Schilling, with the help of Francesco Preti