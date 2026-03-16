import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 
 
api_key = "xxxxxxxxxxxx" 

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Erro ao inicializar o cliente Gemini: {e}")
    st.stop()

st.set_page_config(
    page_title="Agente de Otimização de Perfil (Recrutador Sênior)",
    layout="wide"
)

st.title("💼 Agente de Otimização de Perfil")
st.markdown("Olá!! Sou seu Recrutador Sênior pessoal para analisar e aprimorar textos do seu perfil (LinkedIn, CV).")
st.markdown("---")

perfil_text = st.text_area(
    "Cole aqui o texto do seu perfil (Ex: Seção 'Sobre' do LinkedIn ou uma Experiência Profissional):",
    height=250,
    placeholder="Ex: 'Sou um profissional dinâmico e proativo, gostaria que avaliasse meu perfil' Digite o texto que deseja otimizar ou que seja analisado."
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


def get_optimization_result(system_prompt, user_prompt):
    """
    Função de chamada à API adaptada para Gemini com o system_prompt embutido
    """

    full_prompt = system_prompt + "\n\n--- INÍCIO DO TEXTO DO USUÁRIO ---\n\n" + user_prompt

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  
            contents=[
                {"role": "user", "parts": [{"text": full_prompt}]}
            ],
            config=genai.types.GenerateContentConfig(
                temperature=0.7,
            )
        )
        
        return response.text
        
    except APIError as e:
        return f"Ocorreu um Erro na API do Gemini: {e}. Verifique sua chave de API e limite de uso."
    except Exception as e:
        return f"Ocorreu um erro desconhecido: {e}"

if st.button("Analisar e Otimizar Perfil"):
    if perfil_text:
        system_p, user_p = generate_recruiter_prompt(perfil_text)        
        with st.spinner("🚀 Analisando o perfil com o olhar de um Recrutador Sênior..."):            
            optimization_result = get_optimization_result(system_p, user_p)
        st.subheader("✅ Resultados Detalhados da Análise")        
        st.markdown(optimization_result)        
        st.markdown("---")
        st.success("Análise concluída!")
    else:
        st.warning("Por favor, cole algum texto na área acima para iniciar a análise.")
        
