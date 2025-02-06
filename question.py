from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize Ollama model
llm = Ollama(model="llama2")

# Define the prompt template for question generation
question_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    You are an AI that generates **policy-related questions**.

    Given the following policy text:
    ---
    {text}
    ---
    Generate **3-5 relevant questions**.

    **Output Format:**  
    • Question 1  
    • Question 2  
    • Question 3  
    """
)

# Create LangChain question generation chain
question_chain = LLMChain(llm=llm, prompt=question_prompt)

def generate_questions(text):
    response = question_chain.run({"text": text})
    return response.strip().split("\n")

if __name__ == "__main__":
    test_text = "Organizations must implement data encryption policies to protect sensitive information."
    print("🔹 Generated Questions:", generate_questions(test_text))
