# Desafio MBA Engenharia de Software com IA - Full Cycle

## Pré requisitos

Rede o *[Docker Compose](docker-compose.yml)* para instalar o postgresql com PGVector em um ambiente docker
**Observação:**, é necessário ter *docker*, *Docker Desktop*, *Podman* , *Orb* rodando etc.

```shell
docker compose up -d
```

Crie um `.env` conforme [exemplo](.env.exemple)

## Passos para executar a aplicação

### 1. Ingestão de dados

Rode o *ingest.py* no terminal conforme abaixo

```shell
    python src/ingest.py
```

Resultado esperado

```txt
Ingested 67 chunks into the database
```

Deverá ser criado duas tabelas no seu postgresql, *langchain_pg_collection* e *langchain_pg_embedding*.

### 2. Executar o *chat.py*

```shell
    python src/chat.py
```

Resultado esperado

```txt
Chat iniciado! Digite sua pergunta (ou 'sair' para encerrar):
```

### Testes realizados

```txt
Pergunta: Qual é a capital do Brasil ?
Resposta: Não tenho informações necessárias para responder sua pergunta.

Pergunta: Qual é o faturamento da Alfa Agronegócio Indústria?
Resposta: O faturamento da Alfa Agronegócio Indústria é R$ 85.675.568,77.

Pergunta: Traga subtotais agrupados pelo ano da fundação
Resposta: Subtotais agrupados pelo ano da fundação:
1931: R$ 834.050.422,46
1932: R$ 555.667,04
1934: R$ 4.428.576.423,50
1937: R$ 4.773.298,76
1939: R$ 27.802.840,70
1940: R$ 12.265.308,40
1941: R$ 1.195.256.126,24
1943: R$ 371.819.545,58
1944: R$ 1.623.250.907,30
1945: R$ 850.716.786,74
1947: R$ 49.066.877,18
1948: R$ 125.868.938,96
1950: R$ 134.214.351,74
1952: R$ 121.553.728,52
1954: R$ 169.750.932,44
1958: R$ 52.059.700,58
1961: R$ 6.074.517.188,44
1962: R$ 438.510.949,06
1965: R$ 33.056.617,36
1967: R$ 193.429.808,44
1968: R$ 1.997.540.920,14
1969: R$ 496.872,96
1971: R$ 16.711.565,22
1972: R$ 1.445.750.782,92
1973: R$ 987.250,48
1976: R$ 41.697.430,40
1977: R$ 20.213.601,14
1979: R$ 8.620.142,80
1980: R$ 686.144.113,00
1981: R$ 29.647.044,74
1985: R$ 3.087.821.549,40
1986: R$ 1.970.687,84
1987: R$ 160.544.730,86
1989: R$ 1.343.361.708,26
1991: R$ 1.141.461.405,48
1992: R$ 4.246.570.914,02
1996: R$ 263.103.302,72
1998: R$ 901.436.235,58
1999: R$ 188.779.465,92
2000: R$ 243.586,84
2001: R$ 6.603.145,68
2002: R$ 9.007.106.499,22
2003: R$ 7.071.710.717,40
2005: R$ 3.269.735,56
2008: R$ 3.591.248.897,08
2009: R$ 7.221.960.779,14
2010: R$ 424.856.042,74
2011: R$ 381.654.992,66
2012: R$ 1.334.690.128,60
2016: R$ 749.003,76
2018: R$ 13.694.994,68
2019: R$ 23.147.908,60
2020: R$ 1.097.579.227,30
2021: R$ 1.971.007.465,74
2022: R$ 42.447.434,14
2023: R$ 3.289.471.445,72

Pergunta: Qual o faturamento das empresas com o primeiro nome Alfa?

Resposta: O faturamento das empresas com o primeiro nome Alfa é:
- Alfa Agronegócio Indústria: R$ 85.675.568,77
- Alfa Ambiental Participações: R$ 5.774.383,30
- Alfa Energia Holding: R$ 858.537,02
- Alfa Energia S.A.: R$ 722.875.391,46
- Alfa IA Indústria: R$ 548.789.613,65
- Alfa Imobiliária S.A.: R$ 666.804.293,08
- Alfa Logística Holding: R$ 62.934.469,48
- Alfa Saúde LTDA: R$ 131.151.997,92
- Alfa Sustentável EPP: R$ 268.505,61
- Alfa Sustentável Holding: R$ 543.366,64
- Alfa Sustentável Indústria: R$ 3.301.572,84
- Alfa Tecnologia Holding: R$ 66.776.155,12
- Alfa Telecom LTDA: R$ 80.272.365,43
- Alfa Turismo Comércio: R$ 16.528.308,68
- Alfa Turismo S.A.: R$ 227.237,24

Total: R$ 2.392.381.746,84

```
