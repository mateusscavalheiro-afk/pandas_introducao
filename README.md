# ⚙️ Monitoramento e Telemetria de Sensores Industriais

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-239120?style=for-the-badge&logo=file-type-vscode)

Este repositório contém uma solução em **Python** voltada para a simulação, gravação, leitura estruturada e monitoramento em tempo real de dados industriais (temperatura, pressão e produção).

---

## 📂 Estrutura e Funcionamento dos Arquivos

| Arquivo | Funcionalidade Principal | Bibliotecas |
| :--- | :--- | :--- |
| `dados_maquina.py` | Simula e grava 20 medições no arquivo `dados_sensores.csv`. | `csv`, `random` |
| `tratamento.py` | Realiza a leitura e exibição estruturada do CSV usando **Pandas**. | `pandas` |
| `sensor.py` | Executa um loop de telemetria em tempo real com alertas de limites críticos. | `random`, `time` |

---

## 🛠️ Detalhamento dos Scripts

### 🎲 1. Geração de Dados (`dados_maquina.py`)
Cria o arquivo `dados_sensores.csv` contendo 20 registros com as seguintes variáveis:
* ⏱️ **timestamp**: Horário formatado (`HH:MM:SS`).
* 🌡️ **temperatura**: Valor aleatório de `20.00` a `120.00 ºC`.
* 🎈 **pressao**: Valor aleatório de `1.00` a `8.00 atm`.
* 📦 **producao**: Unidades produzidas de `0` a `250`.

### 🐼 2. Leitura com Pandas (`tratamento.py`)
Utiliza a biblioteca **Pandas** para carregar e visualizar o arquivo `dados_sensores.csv` em formato tabular diretamente no terminal:
* Lê a estrutura das colunas automaticamente.
* Facilita futuras análises estatísticas e manipulações de DataFrames.

### 🚨 3. Telemetria e Alertas em Tempo Real (`sensor.py`)
Simula a leitura de um sensor físico em intervalos regulados por tempo (`time.sleep`):
* Realiza 5 leituras sequenciais.
* **Critério de Temperatura**: Dispara `ALERTA! TEMPERATURA ALTA` se for superior a `80ºC`.
* **Critério de Pressão**: Dispara `ALERTA! PRESSÃO ALTA` se for superior a `5 atm`.

---

## 🚀 Como Executar

1. **Instale as dependências**:
   ```bash
   pip install pandas

2. **Execute a geração do histórico CSV**:
   ```bash
   python dados_maquina.py

3. **Exiba os dados gravados via Pandas**:
   ```bash
   python tratamento.py