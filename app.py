import streamlit as st
import os
from google import genai
from google.genai.errors import APIError # É bom para tratar erros

# --- CHAVE DE API (SUA CHAVE REAL) ---
# Se você definiu como variável de ambiente (MELHOR PRÁTICA), use:
# api_key = os.getenv("GEMINI_API_KEY") 
api_key = "AIzaSyAuqvAA-m7BfEekEjf8NDyo9q8OAhKS_GY" 

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Erro ao inicializar o cliente Gemini: {e}")
    st.stop()

# --- Configurações da Página ---
st.set_page_config(
    page_title="Agente de Otimização de Perfil (Recruiter Sênior)",
    layout="wide"
)

# --- Título Principal e Introdução ---
st.title("💼 Agente de Otimização de Perfil")
st.markdown("Seu Recrutador Sênior pessoal para analisar e aprimorar textos de perfil (LinkedIn, CV).")
st.markdown("---")

# --- Área de Entrada do Usuário ---
# Usamos o 'text_area' para permitir entradas longas de texto.
perfil_text = st.text_area(
    "Cole aqui o texto do seu perfil (Ex: Seção 'Sobre' do LinkedIn ou uma Experiência Profissional):",
    height=250,
    placeholder="Ex: 'Sou um profissional dinâmico e proativo...' Digite o texto que deseja otimizar."
)

def generate_recruiter_prompt(user_text):
    """
    Cria o prompt completo, definindo a Persona, a Tarefa e a Estrutura de Saída.
    """
    system_prompt = """
    Você é um Recrutador Sênior e Analista de Talentos de uma empresa de tecnologia de ponta.
    Sua missão é ser extremamente crítico e helpful. Você deve analisar o texto de perfil 
    (seja seção 'Sobre' do LinkedIn ou descrição de experiência) fornecido pelo usuário.

    Aplique a técnica de Chain-of-Thought (CoT) para justificar sua análise em três etapas.

    A saída DEVE ser estritamente formatada em blocos Markdown separados, exatamente como o exemplo:

    ---
    ### 1. 🎯 Análise Estrutural (CoT: Pense Passo a Passo)
    Descreva como você analisou o texto, focando em: clareza do impacto, uso de métricas, e adequação ao cargo.
    
    ### 2. ❌ Pontos Fracos Atuais
    Liste com bullet points os 3 maiores problemas do texto, com foco na falta de 'palavras-chave' ou 'resultados quantificáveis'.

    ### 3. ✨ Versão Otimizada e Impactante
    Forneça uma reescrita completa e profissional do texto, integrando resultados quantificáveis e verbos de ação fortes.
    Use o tom de voz de um líder de equipe focado em resultados.
    ---
    """

    user_prompt = f"O texto do perfil a ser analisado é o seguinte:\n\n---\n{user_text}\n---"

    return system_prompt, user_prompt

# ... (Seu código Streamlit inicial, imports e api_key) ...

# --- Função de Chamada à API ---
def get_optimization_result(system_prompt, user_prompt):
    """
    Função de chamada à API adaptada para Gemini com o system_prompt embutido
    """
    # Combinamos o system_prompt e o user_prompt para garantir que o modelo 
    # entenda a instrução e a tarefa em um único turno de conversa.
    full_prompt = system_prompt + "\n\n--- INÍCIO DO TEXTO DO USUÁRIO ---\n\n" + user_prompt

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Um bom modelo para esta tarefa
            contents=[
                # Passamos o prompt completo como uma mensagem de usuário
                {"role": "user", "parts": [{"text": full_prompt}]}
            ],
            config=genai.types.GenerateContentConfig(
                temperature=0.7,
                # Outras configurações como max_output_tokens, se necessário
            )
        )
        
        # O resultado vem na propriedade 'text' da resposta
        return response.text
        
    except APIError as e:
        # Erro específico da API (ex: chave inválida, limite excedido)
        return f"Ocorreu um Erro na API do Gemini: {e}. Verifique sua chave de API e limite de uso."
    except Exception as e:
        # Outros erros de execução
        return f"Ocorreu um erro desconhecido: {e}"
# --- Área de Entrada do Usuário (dentro do seu 'app.py') ---
# ... (Código do st.text_area) ...

# --- Botão de Análise (Substitua a simulação por este bloco) ---
if st.button("Analisar e Otimizar Perfil"):
    if perfil_text:
        # 1. Gerar os prompts baseados na entrada
        system_p, user_p = generate_recruiter_prompt(perfil_text)
        
        # Feedback visual para o usuário
        with st.spinner("🚀 Analisando o perfil com o olhar de um Recrutador Sênior..."):
            
            # 2. Chamar a API do LLM
            optimization_result = get_optimization_result(system_p, user_p)

        # 3. Exibir o resultado formatado
        st.subheader("✅ Resultados Detalhados da Análise")
        
        # O resultado é puro Markdown, então o Streamlit o renderiza perfeitamente!
        st.markdown(optimization_result)
        
        st.markdown("---")
        st.success("Análise concluída!")

    else:
        st.warning("Por favor, cole algum texto na área acima para iniciar a análise.")
        
