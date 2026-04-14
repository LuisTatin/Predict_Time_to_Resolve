import pandas as pd
from sqlalchemy import create_engine
import os
from pathlib import Path

# Configurações de ambiente (Em prod, isso viria de variáveis de ambiente)
DATABASE_URL = "postgresql://user:password@localhost:5433/maintenance_db"
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "data" / "raw" / "tickets_data.parquet"



def ingest_data():
    print("Iniciando extração de dados do PostgreSQL...")
    engine = create_engine(DATABASE_URL)

    query = """
            SELECT
                timestamp, edificio_idade, tipo_problema, prioridade, tecnico_senioridade, tempo_resolucao_s
            FROM fact_tickets
            WHERE tempo_resolucao_s IS NOT NULL \
            """

    # Lendo do Banco
    df = pd.read_sql(query, engine)

    # Cria a pasta garantindo que é o caminho absoluto
    os.makedirs(OUTPUT_PATH.parent, exist_ok=True)

    # Salvando usando o objeto Path (o pandas aceita)
    df.to_parquet(OUTPUT_PATH, index=False, compression='snappy')

    print(f"Ingestão concluída! {len(df)} registros salvos em: {OUTPUT_PATH}")


if __name__ == "__main__":
    ingest_data()