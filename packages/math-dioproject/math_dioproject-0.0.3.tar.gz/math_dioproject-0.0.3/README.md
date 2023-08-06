# Calculadora_DioProject

Description:
The package math_dioproject is used to:

	- Solve algorithms problems
	- Check if a number is prime
	- Check if the input result in a square or rectangle

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install math_dioproject

```bash
pip install math_dioproject
```

## Usage

```python
from math_dioproject.basicfunctions import simples as s
from math_dioproject.basicfunctions import complex as c
from math_dioproject.verificador import verifier as v

s.soma(3, 5) #Print the result of 3+5
s.divi(3, 5) #Print the result of 3/5
s.mult(3, 5) #Print the result of 3*5
s.sub(3, 5) #Print the result of 3-5

c.expo(3,2) #Print the result of 3^2
c.raiz(9) #Print the result of 9 square root

v.primo(27) #Print if the number is prime or not
v.quadrado(4, 4, 4, 4) #Print if the input result in a square
v.retangulo(9, 9, 5, 5) #Print if the input result in a rectangle

```

## Author
Marco Crippa

## License
MIT License

Copyright (c) 2022 Marco Crippa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.