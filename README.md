# Dashboard de Vendas 📊🛒

##Este é um projeto de dashboard interativo construído com [Streamlit](https://streamlit.io/) para análise e visualização de dados de vendas. Ele permite filtrar dados, gerar gráficos dinâmicos e exportar resultados personalizados em CSV.
---

## 📦 Funcionalidades

✅ Visualização da base de dados completa  
✅ Filtros por categoria, preço e data da compra  
✅ Exportação dos dados filtrados para CSV  
✅ Gráficos interativos com Plotly:
- Receita total por estado
- Receita mensal#
- Receita por categoria
- Vendas e receita por vendedor
- Mapa de calor das vendas

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

## 📁 Estrutura do Projeto

```bash
├── app.py               # Arquivo principal do dashboard
├── dataframe.py         # Página com os filtros e exportação
├── dataset.py           # Importação e pré-processamento do DataFrame
├── graficos.py          # Funções para geração de gráficos
├── utils.py             # Funções utilitárias
├── data/
│   └── vendas.csv       # Base de dados utilizada


---

## 🚀 Como Executar o Projeto

1. Clone este repositório:

```bash
git clone https://github.com/Drade-Pires/Dashbord_vendas_streamlit.git
cd Dashbord_vendas_streamlit
 
 2. Crie um ambiente virtual(opcional)

 python -m venv venv
venv\Scripts\activate  # No Windows
source venv/bin/activate  # No Linux/macOS

3. Instale as dependencias

pip install -r requirements.txt

4. execute o programa

streamlit run app.py

🧩 Funcionalidades
Visualização de receita mensal, por estado, categoria e vendedor

Gráfico de mapa interativo com Plotly

Métricas de total de vendas e quantidade de pedidos

Página separada com filtros, visualização e download da base de dados filtrada

📚 Base do Projeto
Este projeto foi desenvolvido com base no curso Desenvolvendo Dashboards em Python, disponível na plataforma Udemy.

🙋‍♂️ Autor
Jhonatan de Andrade Pires
📍 Araucária, Paraná
📧 jhonatandeandradepires@gmail.com
🔗 LinkedIn

📝 Licença
Este projeto está licenciado sob a MIT License.
