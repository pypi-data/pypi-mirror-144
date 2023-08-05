# cyclo: solving cyclotomic equation by radicals
```
cyclo(n, recur=True):
  solve cyclotomic equation by radicals
  return n-th roots of unity (except 1)
        [exp(2pi ij/n) for j=1,2,...,n-1]
  if recur is True, q-th roots of unity (q<n) are
    recursively replaced by radical expressions
  reference:
    J. P. Tignol
      "Galois Theory of Algebraic Equations" chapter 12
```
# example code:
```
from sympy.printing import print_latex
from cyclo import cyclo

z = cyclo(17)
print_latex(z[0]+z[-1]) # 2cos(2pi/17)
```