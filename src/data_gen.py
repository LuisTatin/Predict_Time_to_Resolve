import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from faker import Faker
import random

# Lembre-se: se mudou a porta no docker para 5433, use 5433 aqui!
DATABASE_URL = "postgresql://user:password@localhost:5433/maintenance_db"
engine = create_engine(DATABASE_URL)
fake = Faker()


def generate_complex_data(n_samples=3000):
    print(f"🏗️ Gerando {n_samples} chamados de manutenção...")

    data = []
    for _ in range(n_samples):
        # 1. Definir o Edifício (Antigo vs Novo)
        edificio_idade = random.randint(1, 60)

        # 2. Tipo de Problema e sua complexidade base
        tipo = random.choice(['Elétrico', 'Hidráulico', 'Ar Condicionado', 'Elevador'])
        complexidade_base = {'Elétrico': 1.5, 'Hidráulico': 1.2, 'Ar Condicionado': 2.0, 'Elevador': 3.5}[tipo]

        # 3. Prioridade (1: Urgente, 4: Baixa)
        prioridade = np.random.choice([1, 2, 3, 4], p=[0.1, 0.3, 0.4, 0.2])

        # 4. Senioridade do Responsável
        senioridade = random.choice([1, 2, 3])  # 1: Jr, 3: Sr

        # --- CÁLCULO DO TARGET (Tempo de Resolução em Segundos) ---
        # Aqui criamos a lógica que o modelo terá que "descobrir"
        base_seconds = 3600 * 2  # 2 horas base

        # Fatores que aumentam o tempo:
        fator_idade = 1 + (edificio_idade / 100)  # Prédio velho = + tempo
        fator_prioridade = 1 / (5 - prioridade)  # Prioridade alta = foco total (menos tempo)
        fator_tecnico = 1 / senioridade  # Técnico sênior = resolve rápido

        ttr = (base_seconds * complexidade_base * fator_idade * fator_tecnico) + (fator_prioridade * 1000)

        # Adicionar um ruído aleatório para não ser uma fórmula perfeita
        ttr += np.random.normal(0, 600)

        data.append({
            'timestamp': fake.date_time_this_year(),
            'edificio_idade': edificio_idade,
            'tipo_problema': tipo,
            'prioridade': prioridade,
            'tecnico_senioridade': senioridade,
            'tempo_resolucao_s': max(ttr, 300)  # Mínimo 5 min
        })

    df = pd.DataFrame(data)

    # Salvando no Postgres (Portfólio de SQL!)
    df.to_sql('fact_tickets', engine, if_exists='replace', index=False)
    print("✅ Dados salvos com sucesso no PostgreSQL!")


if __name__ == "__main__":
    generate_complex_data()