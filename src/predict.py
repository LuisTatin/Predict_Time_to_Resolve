import mlflow.xgboost
import pandas as pd
import joblib
from pathlib import Path
import os

# 1. Configurações de Ambiente (Mesmas do treino para acessar o MinIO)
os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:9000"
os.environ['AWS_ACCESS_KEY_ID'] = "admin"
os.environ['AWS_SECRET_ACCESS_KEY'] = "password123"

BASE_DIR = Path(__file__).resolve().parent.parent
ENCODER_PATH = BASE_DIR / "models" / "label_encoder.joblib"

# 2. Configurar o endereço do MLflow
mlflow.set_tracking_uri("http://localhost:5001")


def predict_new_ticket():
    # --- DADOS DO NOVO CHAMADO (Simulação) ---
    # Imagine que esses dados vieram de um formulário de uma plataforma
    novo_chamado = {
        'edificio_idade': 45,  # Prédio antigo
        'prioridade': 1,  # Urgente
        'tecnico_senioridade': 3,  # Técnico Sênior
        'tipo_problema': 'Elevador'  # Problema complexo
    }

    print(f"Novo chamado recebido: {novo_chamado}")

    # 3. Carregar o 'Tradutor' (LabelEncoder)
    if not ENCODER_PATH.exists():
        print("Erro: LabelEncoder não encontrado!")
        return
    le = joblib.load(ENCODER_PATH)

    # 4. Preparar os dados para o formato que a IA entende
    df_novo = pd.DataFrame([novo_chamado])
    df_novo['tipo_problema_encoded'] = le.transform(df_novo['tipo_problema'])

    # Selecionar as mesmas colunas do treino (na mesma ordem!)
    features = ['edificio_idade', 'prioridade', 'tecnico_senioridade', 'tipo_problema_encoded']
    X_input = df_novo[features]

    # 5. Carregar o modelo direto do MLflow
    # Pegue o RUN_ID que apareceu no seu terminal (ex: 0b8784312dc2...)
    run_id = "0b8784312dc2463d9e1d0d0812000a71"  # <--- COLOQUE O SEU RUN_ID AQUI
    model_uri = f"runs:/{run_id}/model_ttr"

    print(f"Carregando modelo da run: {run_id}...")
    model = mlflow.xgboost.load_model(model_uri)

    # 6. Realizar a Predição
    prediction_seconds = model.predict(X_input)[0]
    prediction_hours = prediction_seconds / 3600

    print("-" * 30)
    print(f"PREVISÃO DE RESOLUÇÃO:")
    print(f"Tempo estimado: {prediction_seconds:.0f} segundos")
    print(f"Em horas: {prediction_hours:.2f} horas")
    print("-" * 30)


if __name__ == "__main__":
    predict_new_ticket()