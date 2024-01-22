from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from text_reader import read_files, write_triplets
from pathlib import Path
import json
import torch


PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")
PROMPT_PATH = (Path(__file__).parent).joinpath("prompt.txt")

# Create pipeline based on Mistral-7B-Instruct model
model_name = "mistralai/Mistral-7B-Instruct-v0.2"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=2056)

llm = HuggingFacePipeline(pipeline=pipe)

prompt_text = None
with open(PROMPT_PATH, "r") as file:
    prompt_text = file.read()

if prompt_text is not None:
    print(prompt_text)
    prompt = PromptTemplate.from_template(
        prompt_text
    )
else:
    raise Exception("Invalid prompt!")

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
    # TODO: Maybe append "None" to triplets in this case?
    # If no triplets were found, an empty list will be returned
    all_triplets.append(file_triplets)
print("Triplets extracted!")


print("Writing triplets into files...")
# Write triplets in corresponding files
write_triplets(PAPERS_PATH, all_triplets)
print("Triplets written into files!")
