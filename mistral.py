import os
os.environ['TRANSFORMERS_CACHE'] = '/home/ubuntu/big-dir/'

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from text_reader import read_files, write_triplets
from pathlib import Path
from triplet_messages import triplet_messages
from refactor_messages import refactor_messages
import json
import torch
import sys


PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")


# ==== Base LLM for all chains ====
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

# ==== CHAIN 1: Extract triplets ====
# Tokenize previous messages
triplet_prompt_tokens = tokenizer.apply_chat_template(triplet_messages, return_tensors="pt")
# Turn tokens into list of strings
triplet_prompt_text_parts = tokenizer.batch_decode(triplet_prompt_tokens)
# Place all strings into one
triplet_prompt_text = ""
for part in triplet_prompt_text_parts: 
    triplet_prompt_text += part
# Form a prompt from that string
triplet_prompt = PromptTemplate.from_template(triplet_prompt_text)
triplet_chain = triplet_prompt | llm

# ==== CHAIN 2: Refactor triplets ====
refactor_prompt_tokens = tokenizer.apply_chat_template(refactor_messages, return_tensors="pt")
refactor_prompt_text_parts = tokenizer.batch_decode(refactor_prompt_tokens)
refactor_prompt_text = ""
for part in refactor_prompt_text_parts: 
    refactor_prompt_text += part
refactor_prompt = PromptTemplate.from_template(refactor_prompt_text)
refactor_chain = refactor_prompt | llm

# Read all papers
print("Loading files...")
context_examples = read_files(PAPERS_PATH)
print("Files loaded!")

# List of JSON objects. One per paper
all_triplets = []

for i, ex in enumerate(context_examples):
    file_triplets = []

    # CALL 1: Find triplets
    # Result is a JSON *string* with all triplets from the current paper
    print("Extracting triplets...")
    raw_triplets = triplet_chain.invoke({"context": ex})
    # TODO: 
    print("\n\nRAW RES IS")
    print(raw_triplets)

    # CALL 2: Refactor triplets
    print("Refactoring triplets...")
    ref_triplets = refactor_chain.invoke({"triplets": raw_triplets})
    # TODO: 
    print("\nREFACTOR IS")
    print(ref_triplets)

    if "No triplets" not in ref_triplets:
        # Load string into a JSON object
        try:
            parsed_json = json.loads(ref_triplets)
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
