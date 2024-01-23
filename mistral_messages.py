from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from text_reader import read_files, write_triplets
from pathlib import Path
from prompt import messages
import json
import torch
import sys


PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")

model_name = "mistralai/Mistral-7B-Instruct-v0.2"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    do_sample=True,
    temperature=0.1,
    device_map="auto",
    torch_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=4096)

llm = HuggingFacePipeline(pipeline=pipe)

prompt_tokens = tokenizer.apply_chat_template(messages, return_tensors="pt")
prompt_text_parts = tokenizer.batch_decode(prompt_tokens)
prompt_text = ""
for part in prompt_text_parts: 
    prompt_text += part
prompt = PromptTemplate.from_template(prompt_text)

chain = prompt | llm

# Read all papers
print("Loading files...")
context_examples = read_files(PAPERS_PATH)
print("Files loaded!")

# All triplets from all papers
# List of JSON objects. One per paper
all_triplets = []

print("Extracting triplets...")
for ex in context_examples:
    file_triplets = []
    # Result is a JSON *string* with all triplets from the current paper
    res = chain.invoke({"context": ex})
    # TODO: 
    print("\n\nRAW RES IS")
    print(res)
    if "No triplets" not in res:
        # Load string into a JSON object
        try:
            parsed_json = json.loads(res)
            for triplet in parsed_json:
                file_triplets.append(triplet)
        except:
            raise Exception("LLM output is not a valid JSON!")
    all_triplets.append(file_triplets)

print("Triplets extracted!")


print("Writing triplets into files...")
# Write triplets in corresponding files
write_triplets(PAPERS_PATH, all_triplets)
print("Triplets written into files!")
