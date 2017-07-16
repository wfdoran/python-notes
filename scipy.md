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
```

## fsolve

```python
# (x+1)(x-3)(x-4) = x**3 - 6 * x**2 + 5 * x + 12
import numpy as np
from scipy.optimize import fsolve
poly = lambda x : x**3 - 6 * x**2 + 5 * x + 12
fsolve(poly, [0.0,2.5,5.0])
```

## numeric integration

```python
import numpy as np
import math
from scipy.integrate import quad

c = math.sqrt(2 * math.pi)
f = lambda x : np.exp(-x*x/2) / c
quad(f,-10,10)
quad(f,-10,0)
quad(f,-10,1)
quad(f,-10,2)
```

compare with 
```python
import numpy as np
import scipy.stats import norm

dist = norm(0,1)
dist.cdf(0)
dist.cdf(1)
dist.cdf(2)
```