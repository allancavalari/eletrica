# Elétrica

Com base na biblioteca interna de números complexos do Python (cmath), este módulo implementa as classes “Fasor” e “Impedância”, assim como, funções auxiliares, para cálculos de circuitos elétricos de corrente alternada no domínio da frequência.

[Introdução](#introdução) | [Modo de uso](#modo-de-uso) | [Classes](#classes) | [Funções auxiliares](#funções-auxiliares)  | [Exemplos](#exemplos-de-aplicações) | [Notas](#notas)

---

# Introdução

Um sinal senoidal com velocidade angular constante pode ser representado no domínio da frequência utilizando fasores.

```
Fasor é um número complexo que representa a amplitude e a fase de uma senoide.
```

Um número complexo, dentre vários formatos, geralmente é representado no formato retangular:

<img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;z&space;=&space;x&space;&plus;&space;y*i" title="\large z = x + y*i" />

Onde:

> x = valor real

> y = valor imaginário

> <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;i&space;=&space;\sqrt{-1}" title="\large i = \sqrt{-1}" />

Ou, no formato polar:

<img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;z&space;=&space;r\measuredangle&space;\theta" title="\large z = r\measuredangle \theta" />

Onde:

> <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;r&space;=&space;{\sqrt{x^2&plus;y^2}}" title="\large r = {\sqrt{x^2+y^2}}" />
 
> <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;\theta&space;=&space;\arctan&space;{(\frac{y}{x})}" title="\large \theta = \arctan {(\frac{y}{x})}" />

A representação no domínio da frequência simplifica a análise de circuitos lineares excitados por fontes senoidais. 

Assim, como os sinais senoidais podem ser representados através de números complexos (fasores), os demais elementos como resistência, capacitância e indutância também podem ser representados através de impedâncias complexas, através do seu modelo no domínio da frequência.

Embora o Python permita a utilização de "j" ao invés de "i" para a unidade imaginária, na Engenharia Elétrica é usual a aplicação dos números complexos em formatos diferentes do adotado por padrão nesta linguagem.

Formato para fasores:

> <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;z&space;=&space;r\measuredangle&space;\theta" title="\large z = r\measuredangle \theta" /> (formato polar, sendo <img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /> em graus)

Formato para impedâncias complexas:

> <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\large&space;z&space;=&space;x&space;&plus;&space;j*y" title="\large z = x + j*y" />

Considerando j = i
 
# Modo de uso

1- Instalar a biblioteca:

```python
pip install eletrica
```

2- Incluir a biblioteca em seu script:
  
```python
from eletrica import *
```

Observação: Este módulo possui como dependência a biblioteca NumPy. A instalação é realizada automaticamente, se necessária. Alternativamente, pode-se importar somente as funções que serão utilizadas em seu script:

```python
from eletrica import Fasor, Impedancia
```

# Classes

O módulo é baseado na classe "eletrica", a qual utiliza como base os números complexos da biblioteca base do Python. As classes "Fasor" e "Impedancia" são derivações da classe "eletrica", para formalidade na inserção dos dados do problema em análise. Os resultados de quaisquer operação entre Fasores e Impedâncias, automaticamente, resultam em grandezas da classe "eletrica". Todas as classes três classes possuem as mesmas propriedades e métodos.

## Declaração

### Impedância
  
```py
Z = Impedancia("5.0+j10.0")
print(Z)
```

Resultado:
```
5.000000+j10.000000
```
 
### Fasor

```py
V = Fasor("10<60°")
print(V)
```

Resultado:
```
10.000000<60.00°
```

##  Propriedades
  
```py
V = Fasor("100<30°")

print(V)
# 100.000000<30.00°

print(V.polar)
# 100.000000<30.00°

print(V.retangular)
# 86.602540+j50.000000

print(V.conjugado)
# (86.60254037844388-49.99999999999999j)

print(V.fase)
# 29.999999999999993

print(V.real)
# 86.60254037844388

print(V.imag)
# 49.99999999999999
```

Observação: As propriedades **retangular** e **polar** são adequadas para a impressão de resultados, portanto, somente estas possuem formatação de casas decimais por definição. Por padrão os valores reais e imaginários de números no formato retangular e, módulo para números em formato polar, são parametrizados para até 6 casas decimais, enquanto o ângulo é formatado em duas casas decimais.

##  Métodos

As classes Fasor() e Impedancia() aceitam todos os métodos aplicados a números complexos.

# Funções auxiliares

> ### Paralelo(Z1, Z2)

Retorna o cálculo da impedância equivalente para duas impedâncias em paralelo.

```py
Z1 = Impedancia("5+j5")
Z2 = Impedancia("5+j5")
Zeq = Paralelo(Z1, Z2)
print(Zeq)
```

Resultado:
```
2.500000+j2.500000
```

> ### a()

Retorna o vetor 1<120°.

```py
a = a()
print(a)
```

Resultado:
```
1.000000<120.00°
```

## Curto-circuito

As funções para cálculo de curto-circuito retornam os resultados através de matriz 3x1 contendo as correntes de sequência zero (0,0), positiva (1,0) e negativa (2,0).

Através do resultado obtido, pode-se calcular as correntes de fase através da função `Fases()`, a qual aplica o método das componentes simétricas. As componentes de sequência podem ser obtidas de forma análoga através da função `Sequencias()`. As funções auxiliares `Vetor012()` e `VetorABC()` permitem gerar as matrizes através das correspondentes contribuições individuais.

> ### Icc1f(V, Z0, Z1, Z2, Zf)

Resulta nas correntes para o caso de curto-circuito monofásico, onde:

* Z0 = Impedância de sequência zero;
* Z1 = Impedância de sequência positiva;
* Z2 = Impedância de sequência negativa;
* Zf = Impedância de falta para a terra.

> ### Icc2f(V, Z1, Z2, Zf)

Resulta nas correntes para o caso de curto-circuito bifásico, onde:

* Z1 = Impedância de sequência positiva;
* Z2 = Impedância de sequência negativa;
* Zf = Impedância de falta entre as fases.

> ### Icc2ft(V, Z0, Z1, Z2, Zf, Zft)

Resulta nas correntes para o caso de curto-circuito bifásico-terra, onde:

* Z0 = Impedância de sequência zero;
* Z1 = Impedância de sequência positiva;
* Z2 = Impedância de sequência negativa;
* Zf = Impedância de falta;
* Zft = Impedância de falta para terra.

> ### Icc3f(V, Z1, Zf)

Resulta nas correntes para o caso de curto-circuito trifásico, onde:

* Z1 = Impedância de sequência positiva;
* Zf = Impedância de falta.

# Exemplos de aplicações

1. [Cálculo da corrente em um circuito elétrico de corrente alternada](./exemplos/exemplo01.py)
2. [Curto-circuito trifásico nos terminais de um gerador síncrono](./exemplos/exemplo02.py)
3. [Curto-circuito monofásico no terminal de um gerador síncrono](./exemplos/exemplo03.py)
4. [Curto-circuito bifásico nos terminais de um gerador síncrono](./exemplos/exemplo04.py)
5. [Curto-circuito bifásico-terra nos terminais de um gerador síncrono](./exemplos/exemplo05.py)
6. [Cálculo de curto-circuito trifásico e monofásico em um sistema elétrico de potência](./exemplos/exemplo06.py)

# Notas

- Esta documentação encontra-se em elaboração;
- Indica-se a utilização do Jupyter Notebook para elaboração de relatórios técnicos com este módulo;
- Em determinados casos, a variável auxiliar j definida por `j = complex(0,1)` pode simplificar a inserção de uma grande quantidade de impedâncias, como aplicado no [Exemplo 06](./exemplos/exemplo06.py);
- [Licença de uso](./LICENSE)
