
# 💼 Agente de Otimização de Perfil com Engenharia de Prompt

# Descrição do Projeto

Este projeto demonstra a aplicação prática da Engenharia de Prompt para criar um agente de IA especializado. O Agente de Otimização de Perfil atua como um Recrutador Sênior, analisando textos (como a seção "Sobre" do LinkedIn ou descrições de experiência) e fornecendo feedback estruturado para aprimoramento.

Utilizamos a biblioteca Streamlit para construir uma interface de usuário rápida e funcional e a API do Gemini (Google AI) para o processamento de linguagem natural, aplicando técnicas avançadas como o Chain-of-Thought (CoT) no System Prompt para garantir uma análise crítica e de alta qualidade.

## Pré-requisitos

Para rodar este agente localmente, você precisará ter o Python (versão 3.8+) instalado em sua máquina e uma Chave de API do Gemini.

Chave de API do Gemini: Obtenha sua chave gratuitamente no Google AI Studio https://ai.google.dev/

Clone o Repositório:

```Bash
git clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git

cd NomeDoSeuRepositorio
```

## 🛠️ Instalação e Configuração

1. Ambiente Virtual (Recomendado)

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto:

```Bash
\# Cria o ambiente virtual

python -m venv venv

\# Ativa o ambiente virtual (Windows)

.\venv\Scripts\activate

\# Ativa o ambiente virtual (macOS/Linux)

\# source venv/bin/activate
```
2. Instalação das Dependências

Instale as bibliotecas necessárias:

```Bash
pip install streamlit google-genai
```
3. Configuração da Chave de API

O projeto exige sua chave de API do Gemini para funcionar. Você tem duas opções para configurá-la:

Opção A: Variável de Ambiente (Recomendada)

Crie uma variável de ambiente chamada GEMINI\_API\_KEY com o valor da sua chave.

Windows (CMD):

```Bash
set GEMINI\_API\_KEY="SUA\_CHAVE\_AQUI"
```
macOS/Linux:

```Bash
export GEMINI\_API\_KEY="SUA\_CHAVE\_AQUI"
```
Opção B: Direto no Código (app.py)

Se preferir, você pode inserir a chave diretamente no arquivo app.py, na seção de inicialização do cliente:


\# app.py, linha ~15

api\_key = "SUA\_CHAVE\_GEMINI\_AQUI" # Insira aqui

client = genai.Client(api\_key=api\_key)


## ▶️ Como Rodar o Chatbot

Com a chave configurada e o ambiente ativado, execute o Streamlit:

```Bash
python -m streamlit run app.py
```
O aplicativo será aberto automaticamente no seu navegador em http://localhost:8501.

## ⚙️ Tecnologias Utilizadas

Streamlit: Framework Python para prototipagem e interface do usuário.

Google Gemini API: Utilizado para o processamento do System Prompt e geração da análise otimizada.

Python: Linguagem principal do projeto.

## 🧠 Destaques de Engenharia de Prompt

Este projeto é uma prova da minha habilidade em:

Definição de Persona: O System Prompt define claramente a persona como um "Recrutador Sênior" para garantir um tom de análise adequado.

Chain-of-Thought (CoT): O prompt de instrução força o modelo a realizar uma análise estruturada e justificada antes de fornecer a versão otimizada.

Estruturação de Output: O modelo é instruído a retornar o resultado em blocos Markdown bem definidos (Pontos Fracos, Sugestões e Versão Otimizada), facilitando a leitura e a integração no Streamlit.

# 🤝 Contato

Conecte-se comigo no LinkedIn para discutir Engenharia de Prompt, IA e futuros projetos:

[https://www.linkedin.com/in/valdinei-borges-39868b125]
