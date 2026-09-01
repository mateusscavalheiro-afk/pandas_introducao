# ⚙️ Monitoramento e Telemetria de Sensores Industriais

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-239120?style=for-the-badge&logo=file-type-vscode)

Este repositório contém uma solução em **Python** voltada para a simulação, gravação, leitura estruturada, análise estatística, integração com banco de dados SQL e monitoramento em tempo real de dados industriais (temperatura, pressão e produção).

---

## 📂 Estrutura e Funcionamento dos Arquivos

| Arquivo | Funcionalidade Principal | Bibliotecas |
| :--- | :--- | :--- |
| `dados_maquina.py` | Simula e grava 20 medições no arquivo `dados_sensores.csv`. | `csv`, `random` |
| `tratamento.py` | Realiza a leitura, cálculos estatísticos e ordenação dos dados usando **Pandas**. | `pandas` |
| `sensor.py` | Executa um loop de telemetria em tempo real com alertas de limites críticos. | `random`, `time` |
| `banco_dados.py` | Conecta ao **SQLite** (`fabrica.db`), exporta dados via `to_sql`, executa consultas e inserções. | `pandas`, `sqlite3` |

---

## 🛠️ Detalhamento dos Scripts

### 🎲 1. Geração de Dados (`dados_maquina.py`)
Cria o arquivo `dados_sensores.csv` contendo 20 registros com as seguintes variáveis:
* ⏱️ **timestamp**: Horário formatado (`HH:MM:SS`).
* 🌡️ **temperatura**: Valor aleatório de `20.00` a `120.00 ºC`.
* 🎈 **pressao**: Valor aleatório de `1.00` a `8.00 atm`.
* 📦 **producao**: Unidades produzidas de `0` a `250`.

### 🐼 2. Leitura e Análise Estatística (`tratamento.py`)
Utiliza a biblioteca **Pandas** para carregar o arquivo `dados_sensores.csv` e calcular métricas operacionais:
* 📊 **Média de Temperatura**: Calcula a média das medições em ºC (`.mean()`).
* 📈 **Pressão Máxima**: Identifica o pico de pressão registrado (`.max()`).
* 📉 **Produção Mínima**: Localiza o menor volume de produção registrado (`.min()`).
* 🔀 **Ordenação**: Ordena os registros por volume de produção em ordem decrescente (`.sort_values()`).

### 🚨 3. Telemetria e Alertas em Tempo Real (`sensor.py`)
Simula a leitura de um sensor físico em intervalos regulados por tempo (`time.sleep`):
* Realiza 5 leituras sequenciais.
* **Critério de Temperatura**: Dispara `ALERTA! TEMPERATURA ALTA` se for superior a `80ºC`.
* **Critério de Pressão**: Dispara `ALERTA! PRESSÃO ALTA` se for superior a `5 atm`.

### 🗄️ 4. Persistência em Banco de Dados SQL (`banco_dados.py`)
Integra o fluxo de dados CSV com um banco relacional **SQLite** (`fabrica.db`):
* 💾 **Carga Automática**: Transforma o DataFrame do Pandas em uma tabela SQL chamada `dados_sensores` utilizando `to_sql()`.
* 🔍 **Consultas SQL**: Executa instruções de seleção (`SELECT * FROM dados_sensores`).
* ✍️ **Inserção de Registros**: Insere novos dados operacionais via queries parametrizadas (`INSERT INTO ... VALUES (?, ?, ?, ?)`) garantindo persistência com `conn.commit()`.

---
