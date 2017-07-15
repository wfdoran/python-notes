# scipy notes

## curve fit

```python
import numpy as np
from scipy.optimize import curve_fit

def f(x,a,b):
    return np.sin(a * x + b)
    
x = np.linspace(0,10,100)
y = f(x,0.5,2.0)
yy = y + 0.5 * np.random.normal(size = len(x))

params, conv = curve_fit(f, x, yy)

print(params)