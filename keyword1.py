from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize Ollama model
llm = Ollama(model="llama2") 

# Define the prompt template for keyword extraction
keyword_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    You are an AI trained to analyze policy documents.
    
    Given the following text:
    ---
    {text}
    ---
    Extract **5-7 relevant keywords**.

    **Output Format:**  
    - One keyword per line.
    """
)

# Create LangChain keyword extraction chain
keyword_chain = LLMChain(llm=llm, prompt=keyword_prompt)

def extract_keywords(text):
    response = keyword_chain.run({"text": text})
    return response.strip().split("\n")

if __name__ == "__main__":
    test_text = "GDPR requires organizations to comply with data protection policies."
    print("🔹 Extracted Keywords:", extract_keywords(test_text))
