# Guru dos Esforços Orientados a Resolução de Problemas

## Introdução

Este projeto analisa o desempenho dos esforços orientados a resolução de problemas em projetos comerciais ao longo do tempo (em dias) a cada mês. Foram usados métodos estatísticos como a Regra de Sturges e a Média Ponderada de Intervalos e Frequências para tirar insights dos dados.

É importante mencionar que apenas os problemas marcados como "in progress" são considerados nesta análise, visto que os problemas concluídos não são relevantes para a avaliação de desempenho no mês.

Com essa abordagem, a Conpec poderá ver o seu desempenho nesse quesito de forma mais clara, pois nossos membros poderão navegar pelos resultados exibidos na planilha do PE para cada mês do ano pelo histórico do Google Sheets.

Por exemplo, se a idade média dos problemas não resolvidos estiver aumentando ao longo do tempo, isso pode indicar que a EJ está enfrentando desafios para resolver problemas prontamente. Por outro lado, uma idade média decrescente pode sugerir que houve melhorias no processo de resolução de problemas.

## Como funciona

### 1. Formato da Planilha

A planilha de entrada deve ter os cabeçalhos das colunas, que devem incluir "start-date", "current-date" (opcional), "problem-name" (opcional), "status" e "age" (opcional).

### 2. Leitura da Planilha

A planilha deve ser baixada e salva como um arquivo CSV na pasta "data" desse projeto. O código lê a planilha de entrada e extrai as informações relevantes para a análise.

### 3. Regra de Sturges

A Regra de Sturges ajuda a determinar o número ideal de intervalos a serem usados ao dividir as idades do conjunto de problemas. Esta regra é baseada na seguinte fórmula:

$$
\text{Considere: }k = 1 + \log_2 n
\text{; Onde: } k \text{ é o número de intervalos (compartimentos) e } n \text{ é o número de problemas}
$$



A regra fornece um equilíbrio entre ter poucos ou muitos intervalos, tornando a análise mais precisa.

```python
def sturges_rule(self) -> int:
    n = len(self.problem_ages)
    return math.ceil(1 + math.log2(n))
```

### 4. Calculando intervalos

Usando o número de intervalos derivados da Regra de Sturges, o código define os intervalos de intervalo com base nas idades mínima e máxima do conjunto de problemas. Cada intervalo é determinado pela divisão do intervalo de idade total pelo número de intervalos.

```python
k = self.sturges_rule()
min_age, max_age = min(self.problem_ages), max(self.problem_ages)
interval_size = math.ceil((max_age - min_age) / k)

self.intervals = [(min_age + i * interval_size, min_age + (i + 1) * interval_size - 1) for i in range(k)]
```

### 5. Cálculo de frequência

A frequência para cada intervalo é calculada pela contagem de quantos problemas se enquadram em cada intervalo definido.

```python
self.frequencies = [sum(1 for age in self.problem_ages if a <= age <= b) for (a, b) in self.intervals]
```

### 6. Média ponderada de intervalos e frequências

Para calcular a idade média do problema, usamos a fórmula da média ponderada. A média ponderada considera quantos problemas estão em cada intervalo, atribuindo um peso maior aos intervalos com mais problemas.

A média ponderada é calculada como:

$$
\text{Média ponderada} = \frac{\sum \left(\frac{a+b}{2} \times f\right)}{\sum f}
\\
\text{Onde: } a, b \text{ são os limites do intervalo e } f \text{ é a frequência de problemas no intervalo}
$$

```python
def weighted_mean_intervals(self) -> float:
    weighted_sum = sum(((a + b) / 2) * f for (a, b), f in zip(self.intervals, self.frequencies))
    total_frequency = sum(self.frequencies)
    return weighted_sum / total_frequency if total_frequency != 0 else 0
```

## Rodando o código

Para executar o código, basta executar o arquivo `main.py` na raiz do projeto. O código lê a planilha de entrada (especifique o caminho corretamente) e exibe os resultados da análise.

Você pode ajustar o código conforme necessário para atender às suas necessidades de análise.
Por exemplo, se não quiser usar a coluna "current-date" e confiar no meu código para calcular a idade do problema, basta usar o método  ``get_problem_ages_without_curr_date_column()`` ao invés de  ``get_problem_ages_with_curr_date_column()``
