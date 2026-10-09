#🌾 People Analytics: Dashboard de Turnover & Headcount (SoyBean Trading Corp)

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Data_Analysis_Expressions-blue?style=for-the-badge)

## 🏢 Sobre a Empresa (Cenário Fictício)
A **SoyBean Trading Corp** é uma empresa fictícia do setor de agronegócio, especializada no comércio exterior, originando e exportando soja pelo Porto de Santos. Com operações integradas de trading, logística portuária, controle de qualidade em armazéns e gestão financeira de risco (hedging), a empresa conta com um quadro histórico de **200 colaboradores** distribuídos em 6 departamentos principais.

> ⚠️ **Aviso de Dados Simulados:** Todos os dados utilizados neste projeto foram gerados sinteticamente via script Python para fins puramente analíticos, acadêmicos e demonstrativos de competências em **People Analytics e Business Intelligence**.

---

## 🎯 Objetivo do Projeto
Analisar a retenção de talentos, a evolução do *headcount* e a taxa de desligamento (*turnover*) da empresa no período de **5 anos (2021 a 2025)**. 

O projeto visa responder a perguntas estratégicas do setor de Recursos Humanos e Gestão de Pessoas, tais como:
1. Qual é a evolução mensal e anual do volume de colaboradores ativos?
2. Qual é a taxa de *turnover* consolidada e por departamento?
3. Quais áreas apresentam maior índice de rotatividade e em quais períodos do ano ocorrem os picos de desligamento?

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python (`pandas`, `numpy`):** Automação e geração da base de dados simulação com regras de negócio realistas.
* **Power BI:** Modelagem de dados, criação de medidas dinâmicas em **DAX** e desenvolvimento do dashboard interativo.
* **Excel / CSV:** Armazenamento das tabelas fato e dimensões.

---

## 📁 Estrutura do Repositório
```
├── assets/                  # Imagens e GIFs demonstrativos do dashboard
├── data/                    # Bases de dados simuladas em Excel/CSV
├── scripts_python/          # Scripts automatizados para geração da base
│   └── generate_hr_data.py  # Script em Python com regras de negócio e dados sintéticos
└── README.md                # Documentação do projeto
```

---

## 📌 Próximas Etapas do Desenvolvimentos
- [x] Definição do cenário de negócio e regras de People Analytics.
- [x] Automação da base de dados sintética em Python.
- [ ] Construção do Modelo de Dados (Star Schema) e Tabela Calendário no Power BI.
- [ ] Implementação das Medidas em DAX (Headcount Ativo, Total Demissões e % Turnover).
- [ ] Desenvolvimento da **Página 1: Visão Geral do Turnover & Headcount**.
- [ ] Expansão para a **Página 2: Diagnóstico de Retenção & Motivos de Desligamento**.
