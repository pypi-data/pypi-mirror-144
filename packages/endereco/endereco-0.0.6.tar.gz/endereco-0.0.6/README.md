# Endereco

## To install

```
pip install endereco
```

## To import the library

```
from endereco import Endereco
```

## Defining the CEP, UF, CIDADE, BAIRRO or ENDERECO 

```
data = Endereco('59082310')
```

## or address

```
data = Endereco('rua buzius') 
```

## Get Mensagem

```
print(data.mensagem())
```

## Get number of register

```
print(data.total())
```

## Get all address

```
print(data.resultados())
```

## All functions of address

```
print(data.resultados()[0]['uf'])
print(data.resultados()[0]['localidade'])
print(data.resultados()[0]['locNoSem'])
print(data.resultados()[0]['locNu'])
print(data.resultados()[0]['localidadeSubordinada'])
print(data.resultados()[0]['logradouroDNEC'])
print(data.resultados()[0]['logradouroTextoAdicional'])
print(data.resultados()[0]['logradouroTexto'])
print(data.resultados()[0]['baiNu'])
print(data.resultados()[0]['nomeUnidade'])
print(data.resultados()[0]['cep'])
print(data.resultados()[0]['tipoCep'])
print(data.resultados()[0]['numeroLocalidade'])
print(data.resultados()[0]['situacao'])
print(data.resultados()[0]['faixasCaixaPostal'])
print(data.resultados()[0]['faixasCep'])
```


## Links

See my [GitHub](https://github.com/claudiotorresarbe).