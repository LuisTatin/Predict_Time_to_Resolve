import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
import joblib
import os

# Configuração de caminhos robusta
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "raw" / "tickets_data.parquet"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
MODELS_DIR = BASE_DIR / "models"  # Pasta para salvar o encoder


def preprocess():
    print("Iniciando pré-processamento...")

    # 1. Carregar dados
    if not INPUT_PATH.exists():
        print(f"Erro: Arquivo {INPUT_PATH} não encontrado!")
        return

    df = pd.read_parquet(INPUT_PATH)

    # 2. Feature Engineering: Tratamento de Categorias
    # Salvamos o encoder para usar na hora da predição real (Inferência)
    le = LabelEncoder()
    df['tipo_problema_encoded'] = le.fit_transform(df['tipo_problema'])

    os.makedirs(MODELS_DIR, exist_ok=True)
    joblib.dump(le, MODELS_DIR / "label_encoder.joblib")
    print(f"LabelEncoder salvo em {MODELS_DIR}")

    # 3. Seleção de Features e Target
    # Escolhemos o que realmente impacta o tempo de resolução
    features = ['edificio_idade', 'prioridade', 'tecnico_senioridade', 'tipo_problema_encoded']
    target = 'tempo_resolucao_s'

    X = df[features]
    y = df[target]

    # 4. Split de Treino e Teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Salvar os datasets processados
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    train_df.to_parquet(OUTPUT_DIR / "train.parquet", index=False)
    test_df.to_parquet(OUTPUT_DIR / "test.parquet", index=False)

    print(f"Sucesso! Dados salvos em {OUTPUT_DIR}")
    print(f"Colunas utilizadas: {features}")


if __name__ == "__main__":
    preprocess()