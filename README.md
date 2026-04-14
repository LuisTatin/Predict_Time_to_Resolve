# 🚀 Predict-TTR: End-to-End MLOps Pipeline para Gestão de Manutenção

Este repositório apresenta uma solução completa de **Machine Learning Operations (MLOps)** para prever o **Time to Resolve (TTR)** de chamados de manutenção. O projeto simula um cenário real de uma plataforma CMMS (como a Infraspeak), onde a previsibilidade do tempo de reparo é crítica para a otimização de SLAs e alocação de recursos técnicos.

## 📋 Contexto de Negócio
Na gestão de ativos, a incerteza sobre o tempo de conclusão de uma manutenção gera gargalos operacionais e insatisfação do cliente. Este projeto utiliza **Inteligência Artificial** para estimar o tempo de resolução com base em:
* **Idade do Ativo/Edifício:** Impacto de infraestruturas obsoletas.
* **Senioridade do Técnico:** Correlação entre experiência e velocidade de entrega.
* **Complexidade do Problema:** Diferenciação entre categorias (Elétrico, Hidráulico, etc.).
* **Prioridade:** Gestão de urgências e impacto no fluxo de trabalho.

## 🛠️ Stack Tecnológica
* **Linguagem:** Python 3.14 (Latest)
* **Banco de Dados:** PostgreSQL (Persistência Relacional)
* **Armazenamento de Dados:** Apache Parquet (Alta performance e compressão)
* **Machine Learning:** XGBoost (Algoritmo de Gradient Boosting)
* **MLOps & Tracking:** MLflow (Gestão de experimentos e modelos)
* **Artifact Store:** MinIO (Simulação de AWS S3)
* **Infraestrutura:** Docker & Docker-Compose (Ambiente agnóstico e reprodutível)

## 🏗️ Arquitetura do Sistema
O projeto segue o princípio de desacoplamento e modularização:
1.  **Data Generation:** Script Python simula dados de manutenção com correlações reais de negócio.
2.  **Persistence:** Dados são armazenados em um banco PostgreSQL rodando em container.
3.  **Ingestion Layer:** Extração via SQL para formato Parquet, garantindo snapshots imutáveis.
4.  **Preprocessing:** Feature Engineering, tratamento de categorias e versionamento de artefatos (Encoders).
5.  **Training & Tracking:** Treinamento integrado ao MLflow, registrando métricas (MAE, R2) e hiperparâmetros.
6.  **Inference:** Script de predição capaz de carregar o modelo diretamente do Artifact Store.

## 🚀 Como Executar

### Pré-requisitos
* Docker e Docker-Compose instalados.
* Python 3.12+ (recomendado).

### Passo a Passo
1.  **Subir a Infraestrutura:**
    ```bash
    docker-compose up -d
    ```

2.  **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Executar o Pipeline:**
    ```bash
    python src/data_gen.py
    python src/ingestion.py
    python src/preprocessing.py
    python src/train.py
    ```

4.  **Testar Predição:**
    ```bash
    python src/predict.py
    ```

## 📈 Resultados Obtidos
O modelo XGBoost alcançou um **R² de 0.99** e um **MAE (Mean Absolute Error) de ~520 segundos**, demonstrando alta capacidade de capturar as nuances das regras de negócio.

---
**Desenvolvido por Luis Tatin**



# 🚀 Predict-TTR: End-to-End MLOps Pipeline for Maintenance Management

This repository showcases a complete **MLOps** solution designed to predict the **Time to Resolve (TTR)** for maintenance work orders. The project simulates a real-world scenario within a CMMS platform (like Infraspeak), where repair time predictability is crucial for SLA optimization.

## 📋 Business Context
In asset management, uncertainty regarding maintenance completion times leads to operational bottlenecks. This project leverages **AI** to estimate resolution times based on:
* **Asset/Building Age:** Impact of legacy infrastructure.
* **Technician Seniority:** Correlation between expertise and speed.
* **Problem Complexity:** Categorical differentiation (Electrical, Plumbing, etc.).
* **Priority Levels:** Emergency management and workflow impact.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **Database:** PostgreSQL
* **Data Storage:** Apache Parquet
* **Machine Learning:** XGBoost
* **MLOps & Tracking:** MLflow
* **Artifact Store:** MinIO (S3-compatible)
* **Infrastructure:** Docker & Docker-Compose

## 🏗️ System Architecture
1.  **Data Generation:** Synthetic data with business correlations.
2.  **Persistence:** Containerized PostgreSQL storage.
3.  **Ingestion Layer:** SQL to Parquet extraction.
4.  **Preprocessing:** Feature engineering and Encoder versioning.
5.  **Training & Tracking:** MLflow integration for metrics and hyperparams.
6.  **Inference:** Script to load models directly from the Artifact Store.

## 🚀 Getting Started

### Prerequisites
* Docker and Docker-Compose installed.
* Python 3.12+.

### Step-by-Step
1.  **Spin up Infrastructure:**
    ```bash
    docker-compose up -d
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Pipeline:**
    ```bash
    python src/data_gen.py
    python src/ingestion.py
    python src/preprocessing.py
    python src/train.py
    ```

4.  **Test Inference:**
    ```bash
    python src/predict.py
    ```

## 📈 Results
The XGBoost model achieved an **R² of 0.99** and an **MAE of ~520 seconds**, capturing the business nuances successfully.

---
**Developed by Luis Tatin**
