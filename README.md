
# 🚀 Predict-TTR: End-to-End MLOps Pipeline para Gestão de Manutenção (Pt BR + EN)

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![MLflow](https://img.shields.io/badge/MLOps-MLflow-0194E2?logo=mlflow)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-F37626?logo=xgboost)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?logo=postgresql)

Este repositório apresenta uma solução completa de **Machine Learning Operations (MLOps)** projetada para prever o **Time to Resolve (TTR)** de chamados de manutenção. O projeto simula um cenário real de uma plataforma CMMS (como a Infraspeak), demonstrando o ciclo de vida completo de um modelo de Inteligência Artificial, desde a geração de dados até à inferência, com foco em boas práticas de engenharia de software.

---

## 📌 Project Overview (Visão de Negócio)

* **Problem Statement:** Na gestão de infraestruturas e facilities, a incerteza sobre o tempo de conclusão de uma manutenção gera gargalos operacionais, dificuldades na alocação de técnicos e quebras de SLA (Service Level Agreement).
* **Value Proposition:** Esta solução utiliza Inteligência Artificial para estimar o tempo de resolução de cada ticket no momento em que é criado. Isto permite uma gestão proativa de expectativas, priorização inteligente de técnicos seniores para tarefas complexas e otimização do fluxo de trabalho.
* **KPIs de Sucesso Impactados:**
  * Redução da taxa de violação de SLAs.
  * Aumento da precisão no planeamento da agenda dos técnicos.
  * Melhoria no CSAT (Customer Satisfaction Score) devido à previsibilidade.

---

## 🏗️ Architecture & Engineering

A arquitetura foi desenhada seguindo o princípio de desacoplamento, garantindo que cada etapa do pipeline seja agnóstica e reprodutível através de contentores Docker.

### 1. Data Pipeline
* **Data Synthesizer:** Como forma de demonstrar a infraestrutura, os dados são gerados de forma sintética (via `Faker`) simulando correlações reais de negócio (idade do edifício, complexidade do problema, senioridade do técnico e prioridade).
* **Ingestion Layer:** Extração de dados relacionais de um banco PostgreSQL para o formato `Apache Parquet` (compressão Snappy), garantindo alta performance de leitura e snapshots imutáveis para o treino.

### 2. Model Stack & MLOps
* **Algoritmo:** `XGBoost Regressor` - Selecionado pela sua robustez e performance líder na indústria para dados tabulares não estruturados.
* **Tracking & Versionamento:** O `MLflow` é utilizado como servidor central para registar parâmetros, métricas (MAE, R2) e versionar os artefatos do modelo.
* **Artifact Store Local:** Integração de um contentor `MinIO` simulando um ambiente Cloud S3 (`s3://mlflow-artifacts/`), onde os modelos treinados e os encoders (`label_encoder.joblib`) são guardados com segurança.

---

## 🚀 Get Started (Quick Start)

Qualquer pessoa na equipa consegue correr este pipeline e ter a infraestrutura MLOps local a funcionar em menos de 5 minutos.

### Pré-requisitos
* Docker e Docker-Compose
* Python 3.12+ (ambiente virtual recomendado)

### 3 Comandos para o Sucesso

**1. Levantar a Infraestrutura MLOps (PostgreSQL, MinIO, MLflow Server)**
```bash
docker-compose up -d
```
*(Podes aceder ao painel do MLflow em `http://localhost:5001` e ao MinIO em `http://localhost:9001`)*

**2. Instalar as Dependências**
```bash
pip install -r requirements.txt
```

**3. Executar o Pipeline E2E (Ingestão -> Pré-processamento -> Treino)**
```bash
python src/data_gen.py && python src/ingestion.py && python src/preprocessing.py && python src/train.py
```

**🔥 Testar uma Inferência (Simulando a criação de um ticket):**
> **Nota:** Antes de correr, atualiza a variável `run_id` no ficheiro `src/predict.py` com o ID gerado pelo MLflow no terminal durante a fase de treino.
```bash
python src/predict.py
```

---

## 📊 Model Performance & Engineering Excellence

* **Performance:** O modelo atinge um **R² de 0.99** e um **MAE de ~520 segundos**. 
  > *Transparência e Maturidade Analítica:* Como o pipeline atual recorre a dados sintéticos onde a variável target (TTR) deriva de uma fórmula matemática com a adição de ruído normal, as métricas de avaliação do modelo são naturalmente altas. O principal foco deste repositório é demonstrar a excelência da **arquitetura de engenharia** preparada para receber dados reais de produção.
* **Engineering Highlights:**
  * Separação clara de responsabilidades (SOLID).
  * Feature Engineering versionada (os codificadores de features categóricas são serializados para garantir consistência na inferência).
  * Log do schema de input do modelo no MLflow para facilitar futuros deployments.

---

## 🛡️ AI Ethics & Best Practices

* **Reprodutibilidade:** Toda a dependência sistémica está encapsulada em contentores (`docker-compose.yml`), eliminando o problema do "funciona apenas na minha máquina". O `random_state` é fixo em todas as operações estocásticas para garantir resultados idênticos a cada execução.
* **Interpretabilidade (Planeado):** Por se tratar de um modelo de árvore de decisão (XGBoost) com alto impacto operacional, estão planeadas integrações com *SHAP values* para que os gestores de manutenção compreendam o porquê de um TTR estimado ser elevado (ex: "Foi devido à idade da infraestrutura ou à falta de experiência do técnico alocado?").

---

## 🛣️ Future Work (Roadmap)

Sendo este um projeto orgânico, os próximos passos lógicos para evoluir o nível de maturidade do MLOps são:
1. **Model Serving:** Envolver o script de predição numa API utilizando `FastAPI` para permitir consumo em tempo real pelo frontend.
2. **CI/CD:** Implementação de GitHub Actions para correr testes de regressão (Pytest) aos scripts sempre que houver um novo push.
3. **Data Quality & Drift:** Adicionar ferramentas como *EvidentlyAI* ou *Great Expectations* para monitorização contínua do comportamento dos dados (Data Drift) com alertas em caso de degradação da precisão.

---
**Desenvolvido por Luis Tatin**


# 🚀 Predict-TTR: End-to-End MLOps Pipeline for Maintenance Management

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![MLflow](https://img.shields.io/badge/MLOps-MLflow-0194E2?logo=mlflow)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-F37626?logo=xgboost)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?logo=postgresql)

This repository presents a comprehensive **Machine Learning Operations (MLOps)** solution designed to predict the **Time to Resolve (TTR)** for maintenance work orders. The project simulates a real-world scenario within a CMMS platform (like Infraspeak), demonstrating the full lifecycle of an AI model, from data generation to inference, with a strong emphasis on software engineering best practices.

---

## 📌 Project Overview (Business Vision)

* **Problem Statement:** In infrastructure and facility management, uncertainty regarding the completion time of maintenance tasks creates operational bottlenecks, challenges in technician allocation, and SLA (Service Level Agreement) breaches.
* **Value Proposition:** This solution leverages AI to estimate the resolution time of each ticket the moment it is created. This enables proactive expectation management, intelligent prioritization of senior technicians for complex tasks, and workflow optimization.
* **Impacted Success KPIs:**
  * Reduction in SLA violation rates.
  * Increased accuracy in technician schedule planning.
  * Improvement in CSAT (Customer Satisfaction Score) due to enhanced predictability.

---

## 🏗️ Architecture & Engineering

The architecture was designed following the decoupling principle, ensuring that each stage of the pipeline is agnostic and reproducible via Docker containers.

### 1. Data Pipeline
* **Data Synthesizer:** To demonstrate the infrastructure, data is generated synthetically (via `Faker`) simulating real business correlations (building age, problem complexity, technician seniority, and priority).
* **Ingestion Layer:** Extraction of relational data from a PostgreSQL database into `Apache Parquet` format (Snappy compression), ensuring high read performance and immutable snapshots for training.

### 2. Model Stack & MLOps
* **Algorithm:** `XGBoost Regressor` - Selected for its robustness and industry-leading performance on unstructured tabular data.
* **Tracking & Versioning:** `MLflow` is used as the central server to log parameters, metrics (MAE, R2), and version model artifacts.
* **Local Artifact Store:** Integration of a `MinIO` container simulating an S3 Cloud environment (`s3://mlflow-artifacts/`), where trained models and encoders (`label_encoder.joblib`) are securely stored.

---

## 🚀 Get Started (Quick Start)

Anyone on the team can run this pipeline and have the local MLOps infrastructure up and running in under 5 minutes.

### Prerequisites
* Docker and Docker-Compose
* Python 3.12+ (virtual environment recommended)

### 3 Commands to Success

**1. Spin up the MLOps Infrastructure (PostgreSQL, MinIO, MLflow Server)**
```bash
docker-compose up -d
```
*(You can access the MLflow UI at `http://localhost:5001` and MinIO at `http://localhost:9001`)*

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the E2E Pipeline (Ingestion -> Preprocessing -> Training)**
```bash
python src/data_gen.py && python src/ingestion.py && python src/preprocessing.py && python src/train.py
```

**🔥 Test an Inference (Simulating a ticket creation):**
> **Note:** Before running, update the `run_id` variable in the `src/predict.py` file with the ID generated by MLflow in the terminal during the training phase.
```bash
python src/predict.py
```

---

## 📊 Model Performance & Engineering Excellence

* **Performance:** The model achieves an **R² of 0.99** and an **MAE of ~520 seconds**. 
  > *Transparency and Analytical Maturity:* Because the current pipeline relies on synthetic data where the target variable (TTR) is derived from a mathematical formula with added normal noise, the model's evaluation metrics are naturally high. The main focus of this repository is to demonstrate the excellence of the **engineering architecture**, which is ready to ingest real production data.
* **Engineering Highlights:**
  * Clear separation of concerns (SOLID principles).
  * Versioned Feature Engineering (categorical feature encoders are serialized to ensure consistency during inference).
  * Logging of the model's input schema in MLflow to facilitate future deployments.

---

## 🛡️ AI Ethics & Best Practices

* **Reproducibility:** All systemic dependencies are encapsulated in containers (`docker-compose.yml`), eliminating the "it works on my machine" problem. The `random_state` is fixed across all stochastic operations to guarantee identical results on every run.
* **Interpretability (Planned):** Given that this is a decision tree model (XGBoost) with high operational impact, integrations with *SHAP values* are planned so that maintenance managers can understand why an estimated TTR is high (e.g., "Was it due to the age of the infrastructure or the lack of experience of the allocated technician?").

---

## 🛣️ Future Work (Roadmap)

As this is an organic project, the logical next steps to evolve the MLOps maturity level are:
1. **Model Serving:** Wrap the prediction script in an API using `FastAPI` to enable real-time consumption by the frontend.
2. **CI/CD:** Implement GitHub Actions to run regression tests (Pytest) on the scripts whenever there is a new push.
3. **Data Quality & Drift:** Add tools like *EvidentlyAI* or *Great Expectations* for continuous monitoring of data behavior (Data Drift), triggering alerts in case of accuracy degradation.

---
**Developed by Luis Tatin**
