from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
# This will wrap prompt into [INST], <s> and other necessary tokens 
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")


pipe = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
    max_new_tokens=1000, 
    device=0 # device=-1 for CPU, device=0 for GPU
)
llm = HuggingFacePipeline(pipeline=pipe)


prompt = PromptTemplate.from_template(
    """
    Answer the question. Think step by step.

    Question: {question}

    """
)

chain = prompt | llm

question = "How far can ducks fly?"

res = chain.invoke({"question": question})

print(res)
