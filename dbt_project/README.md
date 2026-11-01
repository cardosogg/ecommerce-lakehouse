# 🛒 E-Commerce Medallion Lakehouse

Pipeline de Engenharia de Dados moderno construído localmente utilizando uma arquitetura **Medallion (Bronze, Silver, Gold)**, processando e transformando dados sem custos de nuvem.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3 (Pandas, PyArrow)
* **Orquestração & Transformação:** dbt (Data Build Tool) + `dbt-duckdb`
* **Armazenamento & Motor Analítico:** DuckDB (Ficheiro `.duckdb` local e formato Parquet)
* **Qualidade de Dados:** dbt tests (Validação de chaves primárias, unicidade e nulos)
* **Ambiente:** Linux WSL (Ubuntu) / VS Code

---

## 📂 Arquitetura e Estrutura do Projeto

O pipeline segue a arquitetura Medallion para garantir governança, qualidade e modularidade dos dados:

```text
ecommerce-lakehouse/
├── data/
│   ├── bronze/          # Dados brutos ingeridos em formato Parquet
│   └── lakehouse.duckdb # Base de dados analítica local do DuckDB
├── dbt_project/
│   ├── models/
│   │   ├── silver/      # Limpeza, tipagem e padronização (Silver)
│   │   └── gold/        # Agregações de negócio e métricas finais (Gold)
│   ├── schema.yml       # Testes de integridade e qualidade de dados
│   ├── profiles.yml     # Configuração de conexão com o DuckDB
│   └── dbt_project.yml
└── src/
    └── extract/         # Scripts de geração/ingestão de dados brutos