🚀 Predict-TTR: End-to-End MLOps Pipeline para Gestão de Manutenção (Pt-BR + EN)
Este repositório apresenta uma solução completa de Machine Learning Operations (MLOps) para prever o Time to Resolve (TTR) de chamados de manutenção. O projeto simula um cenário real de uma plataforma CMMS (como a Infraspeak), onde a previsibilidade do tempo de reparo é crítica para a otimização de SLAs e alocação de recursos técnicos.

📋 Contexto de Negócio
Na gestão de ativos, a incerteza sobre o tempo de conclusão de uma manutenção gera gargalos operacionais e insatisfação do cliente. Este projeto utiliza Inteligência Artificial para estimar o tempo de resolução com base em:

Idade do Ativo/Edifício: Impacto de infraestruturas obsoletas.

Senioridade do Técnico: Correlação entre experiência e velocidade de entrega.

Complexidade do Problema: Diferenciação entre categorias (Elétrico, Hidráulico, etc.).

Prioridade: Gestão de urgências e impacto no fluxo de trabalho.

🛠️ Stack Tecnológica
Linguagem: Python 3.14 (Latest)

Banco de Dados: PostgreSQL (Persistência Relacional)

Armazenamento de Dados: Apache Parquet (Alta performance e compressão)

Machine Learning: XGBoost (Algoritmo de Gradient Boosting)

MLOps & Tracking: MLflow (Gestão de experimentos e modelos)

Artifact Store: MinIO (Simulação de AWS S3)

Infraestrutura: Docker & Docker-Compose (Ambiente agnóstico e reprodutível)

🏗️ Arquitetura do Sistema
O projeto segue o princípio de desacoplamento e modularização:

Data Generation: Script Python simula dados de manutenção com correlações reais de negócio.

Persistence: Dados são armazenados em um banco PostgreSQL rodando em container.

Ingestion Layer: Extração via SQL para formato Parquet, garantindo snapshots imutáveis.

Preprocessing: Feature Engineering, tratamento de categorias e versionamento de artefatos (Encoders).

Training & Tracking: Treinamento integrado ao MLflow, registrando métricas (MAE, R2) e hiperparâmetros.

Inference: Script de predição capaz de carregar o modelo diretamente do Artifact Store.

🚀 Como Executar
Pré-requisitos

Docker e Docker-Compose instalados.

Python 3.12+ (recomendado).

Passo a Passo

Subir a Infraestrutura:

Bash
docker-compose up -d
Acesse o MLflow em http://localhost:5001 e o MinIO em http://localhost:9001 (Crie o bucket mlflow-artifacts).

Instalar Dependências:

Bash
pip install -r requirements.txt
Executar o Pipeline:

Bash
python src/data_gen.py      # Gera e salva no SQL
python src/ingestion.py     # SQL -> Parquet
python src/preprocessing.py # Limpeza e Encoding
python src/train.py         # Treino e Log no MLflow
Testar Predição:

Bash
python src/predict.py
📈 Resultados Obtidos
O modelo XGBoost alcançou um R² de 0.99 e um MAE (Mean Absolute Error) de ~520 segundos, demonstrando alta capacidade de capturar as nuances das regras de negócio injetadas no simulador de dados. Todas as métricas podem ser comparadas historicamente através da interface do MLflow.

☁️ Cloud Readiness (AWS)
Este projeto foi desenhado para ser Cloud Agnostic. A migração para a AWS envolve:

RDS (PostgreSQL): Substituindo o container de DB.

S3: Substituindo o MinIO para armazenamento de modelos.

AWS Fargate/App Runner: Para hospedar o servidor MLflow.

AWS Lambda: Para executar a lógica de predição em regime Serverless.

Desenvolvido por Luis Tatin


🚀 Predict-TTR: End-to-End MLOps Pipeline for Maintenance Management
This repository showcases a complete Machine Learning Operations (MLOps) solution designed to predict the Time to Resolve (TTR) for maintenance work orders. The project simulates a real-world scenario within a CMMS (Computerized Maintenance Management System) platform—similar to Infraspeak—where repair time predictability is crucial for SLA optimization and technical resource allocation.

📋 Business Context
In asset management, uncertainty regarding maintenance completion times leads to operational bottlenecks and customer dissatisfaction. This project leverages Artificial Intelligence to estimate resolution times based on:

Asset/Building Age: Impact of legacy infrastructure on repair complexity.

Technician Seniority: Correlation between expertise and delivery speed.

Problem Complexity: Categorical differentiation (Electrical, Plumbing, HVAC, etc.).

Priority Levels: Emergency management and its impact on workflow throughput.

🛠️ Tech Stack
Language: Python 3.14 (Latest)

Database: PostgreSQL (Relational Persistence)

Data Storage: Apache Parquet (High-performance columnar storage)

Machine Learning: XGBoost (Gradient Boosting Regressor)

MLOps & Tracking: MLflow (Experiment tracking and model registry)

Artifact Store: MinIO (S3-compatible local storage)

Infrastructure: Docker & Docker-Compose (Agnostic and reproducible environment)

🏗️ System Architecture
The project follows clean code principles, ensuring decoupling and modularity:

Data Generation: Python script simulating maintenance data with real-world business correlations.

Persistence: Data is stored in a containerized PostgreSQL database.

Ingestion Layer: SQL-based extraction to Parquet format, ensuring immutable data snapshots.

Preprocessing: Feature engineering, categorical encoding, and artifact versioning (Encoders).

Training & Tracking: MLflow-integrated training, logging metrics (MAE, R²), and hyperparameters.

Inference: Prediction script capable of loading models directly from the Artifact Store.

🚀 Getting Started
Prerequisites

Docker and Docker-Compose installed.

Python 3.12+ (recommended).

Step-by-Step

Spin up Infrastructure:

Bash
docker-compose up -d
Access MLflow at http://localhost:5001 and MinIO at http://localhost:9001 (Create the mlflow-artifacts bucket).

Install Dependencies:

Bash
pip install -r requirements.txt
Run the Pipeline:

Bash
python src/data_gen.py      # Generate and save to SQL
python src/ingestion.py     # SQL -> Parquet
python src/preprocessing.py # Cleaning and Encoding
python src/train.py         # Training and MLflow Logging
Test Inference:

Bash
python src/predict.py
📈 Results
The XGBoost model achieved an R² of 0.99 and an MAE (Mean Absolute Error) of ~520 seconds, demonstrating a high capacity to capture the nuances of the business rules injected into the data simulator. All metrics can be historically compared via the MLflow UI.

☁️ Cloud Readiness (AWS)
This project is designed to be Cloud Agnostic. Migration to AWS involves:

Amazon RDS (PostgreSQL): Replacing the DB container.

Amazon S3: Replacing MinIO for artifact storage.

AWS Fargate/App Runner: To host the MLflow tracking server.

AWS Lambda: To execute inference logic in a Serverless environment.

Developed by Luis Tatin
Connect with me on LinkedIn
