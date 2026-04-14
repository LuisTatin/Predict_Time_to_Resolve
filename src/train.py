import pandas as pd
import xgboost as xgb
import mlflow
import mlflow.xgboost
from sklearn.metrics import mean_absolute_error, r2_score
from pathlib import Path
import os

# 1. Configurações de Caminhos e Ambiente
BASE_DIR = Path(__file__).resolve().parent.parent
TRAIN_PATH = BASE_DIR / "data" / "processed" / "train.parquet"
TEST_PATH = BASE_DIR / "data" / "processed" / "test.parquet"

# Configurações para o MLflow conversar com o MinIO (S3 local)
os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:9000"
os.environ['AWS_ACCESS_KEY_ID'] = "admin"
os.environ['AWS_SECRET_ACCESS_KEY'] = "password123"

# 2. Conectar ao Servidor MLflow
# Lembre-se: use a porta 5001 se foi a que você liberou no Mac
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("Infraspeak_TTR_Prediction")


def train():
    print("🚀 Iniciando treinamento com MLflow...")

    # Carregar dados
    if not TRAIN_PATH.exists():
        print(f"Erro: Arquivo {TRAIN_PATH} não encontrado!")
        return

    train_df = pd.read_parquet(TRAIN_PATH)
    test_df = pd.read_parquet(TEST_PATH)

    X_train = train_df.drop(columns=['tempo_resolucao_s'])
    y_train = train_df['tempo_resolucao_s']
    X_test = test_df.drop(columns=['tempo_resolucao_s'])
    y_test = test_df['tempo_resolucao_s']

    # Iniciar uma "Corrida" (Run) no MLflow
    with mlflow.start_run(run_name="XGBoost_Final_Adjusted"):
        # Hiperparâmetros
        params = {
            "objective": "reg:squarederror",
            "n_estimators": 100,
            "max_depth": 5,
            "learning_rate": 0.1,
            "random_state": 42
        }

        mlflow.log_params(params)

        # Treinamento
        model = xgb.XGBRegressor(**params)
        model.fit(X_train, y_train)

        # Predição e Métricas
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        mlflow.log_metric("mae_seconds", mae)
        mlflow.log_metric("r2_score", r2)

        print(f"Métricas: MAE: {mae:.2f}s | R2: {r2:.2f}")

        # --- A CORREÇÃO ESTÁ AQUI ---
        # Definimos um exemplo de entrada para o MLflow entender o schema
        input_example = X_test.iloc[[0]]

        # Salvamos o modelo (usando a função recomendada nas versões novas)
        mlflow.xgboost.log_model(
            xgb_model=model,
            artifact_path="model_ttr",
            input_example=input_example
        )

        print("✅ Treino concluído e modelo registrado com sucesso!")


if __name__ == "__main__":
    train()