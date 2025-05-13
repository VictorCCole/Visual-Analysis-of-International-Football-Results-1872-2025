# 📊 Análise Visual de Resultados Internacionais no Futebol (1872–2025)

Este projeto tem como objetivo aplicar técnicas de manipulação e visualização de dados utilizando Python, com base no dataset histórico de partidas internacionais de futebol (disponível no Kaggle).

---

## 📁 Dataset Utilizado

- **Fonte:** [International football results from 1872 to 2023 - Kaggle](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)
- **Arquivo:** `results.csv`

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.10
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Folium
- Geopy

---

## 🔍 Visualizações Criadas

| Tipo         | Descrição                                          | Ferramenta |
|--------------|----------------------------------------------------|------------|
| Estático     | Número de partidas por década                      | Matplotlib |
| Estático     | Top 10 seleções com mais vitórias                  | Seaborn    |
| Interativo   | Evolução do total de gols por ano                  | Plotly     |
| Mapa         | Localização das partidas internacionais (amostra)  | Folium + Geopy |

---

## ▶️ Como Executar

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/VictorCCole/Visual-Analysis-of-International-Football-Results-1872-2025.git
   cd Visual-Analysis-of-International-Football-Results-1872-2025
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Certifique-se de que o arquivo results.csv está na mesma pasta do script.
4. Execute o script principal:
   ```bash
   python main.py
   ```
---

## 📂 Arquivos Gerados
partidas_por_decada.png – Gráfico estático

top10_vitorias.png – Gráfico estático

total_gols_ano.html – Gráfico interativo em HTML

mapa_partidas.html – Mapa interativo com marcadores de cidades

---

## 👨‍🎓 Requisitos da Tarefa
Este projeto atende a todos os critérios definidos:

✅ 2 visualizações estáticas

✅ 2 visualizações interativas (gráfico e mapa)

✅ Uso de bibliotecas ensinadas em aula

✅ Implementado 100% em Python

---

## 📬 Autor
Nome: Victor C. Cole

Curso: Ciência da Computação

Disciplina: Data Science

Data: Maio de 2025
   
