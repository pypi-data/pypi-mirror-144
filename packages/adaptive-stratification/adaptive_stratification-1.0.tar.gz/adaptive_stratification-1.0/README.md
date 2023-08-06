# Adaptive Stratification

This package provides an implementation of the adaptive stratification sampling method to estimate quantities of interest of the form

![equation](http://www.sciweavers.org/tex2img.php?eq=Q%20%3D%20%5Cmathbb%7BE%7D%5Cleft%28%7Bf%28%5Cboldsymbol%7B%5Cxi%7D%29%7D%5Cright%29&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

where the random vector satisfies

![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cboldsymbol%7B%5Cxi%7D%5Csim%5Ctext%7BUni%7D%5Cleft%28%7B%5B0%2C1%5D%7D%5Ed%5Cright%29%5Cquad%5Ctext%7Band%7D%5Cquad%20f%5Ccolon%7B%5B0%2C1%5D%7D%5Ed%5Cto%5Cmathbb%7BR%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

is a given function.

## Example: Using the Sampler

```python
# Import the module containing the sampling routines
from stratification import AdaptiveStratification

# Create a sampler for function func
sampler = AdaptiveStratification(func, d, N_max, N_new_per_stratum, alpha, type='hyperrect')

# Solve (return a tuple)
result = sampler.solve()
```
Input arguments:

* `func`: implementation of given function of interest that defines the quantity of interest. It needs to be callable, accepting one m-times-n-dimensional numpy array as input and returns a m-dimensional numpy array;
* `d`: dimension of the stochastic domain;
* `N_max`: number of total samples to be used;
* `N_new_per_stratum`: targeted average number of samples per stratum, controlling the adaptation;
* `alpha`: number between zero and one, defining the hybrid allocation rule;
* `type`: type of tessellation procedure, i.e., via hyper-rectangles (`type='hyperrect'`) or simplices (`type='simplex'`)

## More Information

See the [Github repository](https://github.com/SKrumscheid/ADSS) for more details.
