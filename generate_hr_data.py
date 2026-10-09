import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
#pacote openpyxl    #pip install openpyxl

# Garantir reprodutibilidade dos dados simulados
np.random.seed(42)
random.seed(42)

N_EMPLOYEES = 200
START_DATE = datetime(2021, 1, 1)
END_DATE = datetime(2025, 12, 31)

# Departamentos e Cargos do Setor de Soja/Trading (Nome, Salário Mínimo, Salário Máximo)
departments_cargos = {
    "Comercial & Trading": [
        ("Trader de Commodities", 8500, 15000),
        ("Analista de Trading", 4500, 7500),
        ("Assistente Comercial", 3000, 4200)
    ],
    "Logística Portuária": [
        ("Coordenador de Logística", 7000, 11000),
        ("Analista de Logística Portuária", 4200, 6800),
        ("Assistente de Agenciamento", 2800, 3800)
    ],
    "Operações & Armazéns": [
        ("Supervisora de Operações", 6500, 9500),
        ("Analista de Qualidade e Grãos", 3800, 5800),
        ("Operador de Silo/Terminal", 2500, 3500)
    ],
    "TI & Dados": [
        ("Engenheiro de Dados", 7500, 12000),
        ("Analista de Business Intelligence", 4800, 7800),
        ("Suporte Técnico", 2800, 4000)
    ],
    "Financeiro & Risco": [
        ("Analista de Risco e Hedging", 5500, 9000),
        ("Analista Financeiro", 4200, 6500),
        ("Assistente Contábil", 2800, 3800)
    ],
    "RH & Administrativo": [
        ("Analista de RH", 4000, 6200),
        ("Assistente Administrativo", 2500, 3500)
    ]
}

first_names = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", 
               "Isabela", "João", "Karen", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", 
               "Rafaela", "Rodrigo", "Sophia", "Thiago", "Beatriz", "Caio", "Fernanda", "Gabriel"]

last_names = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", 
              "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes"]

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

data = []

for i in range(1, N_EMPLOYEES + 1):
    emp_id = f"SOJA-{i:03d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    gender = random.choice(["Feminino", "Masculino"])
    
    dept = random.choice(list(departments_cargos.keys()))
    cargo_tuple = random.choice(departments_cargos[dept])
    
    cargo, sal_min, sal_max = random.choice(departments_cargos[dept])
    salario = round(random.uniform(sal_min, sal_max), 2)
    
    if "Coordenador" in cargo or "Supervisora" in cargo or ("Trader" in cargo and salario > 11000):
        nivel = "Liderança / Sênior"
    elif "Analista" in cargo or "Engenheiro" in cargo:
        nivel = random.choice(["Pleno", "Sênior"])
    else:
        nivel = "Júnior / Operacional"
        
    admissao = random_date(datetime(2019, 1, 1), datetime(2025, 6, 30))
    is_demitido = random.random() < 0.35 # ~35% de taxa histórica de turnover
    
    if is_demitido:
        min_demissao = max(admissao + timedelta(days=90), START_DATE)
        if min_demissao < END_DATE:
            demissao = random_date(min_demissao, END_DATE)
            status = "Desligado"
            tipo_desligamento = random.choice(["Voluntário (Pedido)", "Voluntário (Pedido)", "Involuntário (Demissão)"])
            motivo = random.choice([
                "Proposta de Outra Empresa", "Salário/Benefícios", 
                "Desalinhamento com Liderança", "Performance", "Reestruturação"
            ]) if tipo_desligamento == "Voluntário (Pedido)" else "Performance / Reestruturação"
        else:
            demissao = None
            status = "Ativo"
            tipo_desligamento = "N/A"
            motivo = "N/A"
    else:
        demissao = None
        status = "Ativo"
        tipo_desligamento = "N/A"
        motivo = "N/A"
        
    data.append({
        "ID_Colaborador": emp_id,
        "Nome": name,
        "Genero": gender,
        "Departamento": dept,
        "Cargo": cargo,
        "Nivel": nivel,
        "Salario_Atual": salario,
        "Data_Admissao": admissao.strftime("%Y-%m-%d"),
        "Data_Demissao": demissao.strftime("%Y-%m-%d") if demissao else "",
        "Status": status,
        "Tipo_Desligamento": tipo_desligamento,
        "Motivo_Desligamento": motivo,
        "Tipo_Contrato": "CLT"
    })

df = pd.DataFrame(data)

# Exportar bases
df.to_csv("dados_rh_soybean_corp.csv",
index=False, encoding="utf-8-sig") 
df.to_excel("dados_rh_soybean_corp.xlsx", index=False)
print("Base de dados de RH para o Power BI gerada com sucesso!")