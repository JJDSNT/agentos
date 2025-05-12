import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Recupera os parâmetros
model_name = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:0.5b")
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Inicializa o modelo
llm = Ollama(model=model_name, base_url=base_url)

# Define o prompt para execução da ação
template = (
    "Você é um agente executor. Recebeu a seguinte ação do plano:\n\n"
    "{acao}\n\n"
    "Descreva como ela seria executada na prática, incluindo etapas, ferramentas necessárias, e possíveis riscos."
)
prompt = PromptTemplate.from_template(template)

# Cria a cadeia
chain = LLMChain(llm=llm, prompt=prompt)

# Teste manual
if __name__ == "__main__":
    acao = "Criar um chatbot de atendimento ao cliente usando WhatsApp Business API e integração com CRM"
    resultado = chain.run(acao=acao)
    print("\n🛠️ Execução simulada da ação:\n")
    print(resultado)
c