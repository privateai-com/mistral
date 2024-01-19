from transformers import AutoTokenizer
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate

# This will wrap prompt into <s> tokens
# TODO: not sure it's needed
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

# Create pipeline based on Mistral-7B-Instruct model
llm = HuggingFacePipeline.from_model_id(
    task="text-generation",
    model_id="mistralai/Mistral-7B-Instruct-v0.2",
    device_map="auto", # Use 'accelerate' library to load model to VRAM and RAM
    model_kwargs={
        "do_sample": True, 
        "temperature": 0.1,
        "max_new_tokens": 1028,  
    },
)

# Create a prompt. Use few-shot for better perfomance.
# Place [INST] and [/INST] tags explicitly as tokenizer only adds <s> and </s> tags
# TODO: Make sure that all triplets are present in examples
prompt = PromptTemplate.from_template(
    """
    [INST] 
    You are a helpful assistant. You must analyze the given context and find all triplets in it.
    A triplet is a collection of 3 parts: a subject, a link, an object.
    A subject is connected with an object via a link.
    In most cases, a subject and an object contain nouns and adjectives and links contain verbs.
    If no triplets can be found in the context, the output must be a string: "None". Return only this one word if no triplets were found.
    Output only the triplets and nothing else. Do not make up any new triplets, stick strictly to the context.
    You must output all triplets in a valid JSON format. Use only this format for all triplets and nothing else:
    
    {{ 
        {{
            "subject1": "<subject1 here>",
            "link1": "<link1 here>",
            "object1": "<object1 here>"
        }},
        {{
            "subject2": "<subject2 here>",
            "link2": "<link2 here>",
            "object2": "<object2 here>"
        }},
        {{
            "subject3": "<subject3 here>",
            "link3": "<link3 here>",
            "object3": <object3 here>
        }}
    }}


    Let's look at some examples:

    ### Example 1 ###
    Context: "Bob went to Walmart to buy cheap clothes."
    Triplets:
    {{
        {{   
            "subject": "Bob",
            "link": "Went to",
            "object": "Walmart"
        }},
        {{
            "subject": "Bob",
            "link": "Buy",
            "object": "Cheap clothes"
        }},
        {{
            "subject": "Clothes",
            "link": "Are",
            "object": "Cheap"
        }},
        {{
            "subject": "Cheap clothes",
            "link": "Are sold in",
            "object": "Walmart"
        }}
    }}


    ### Example 2 ###
    Context: "The disadvantage of this design is that Nagant revolvers were laborious and time-consuming to reload"
    Triplets:
    {{
        {{  
            "subject": "Nagant revolvers",
            "link": "Were",
            "object": "Laborious and time-consuming to reload"
        }},
        {{
            "subject": "Disadvantage of design",
            "link": "Is",
            "object": "Laborious and time-consuming to reload"
        }},
        {{
            "subject": "Reload",
            "link": "Is",
            "object": "Laborious and time-consuming"
        }}
    }}

    ### Example 3 ###
    Context: "Soap"
    Triplets: "None"

    ### Example 4 ###
    Context: "Kendrick Lamar"
    Triplets: "None"

    ### End of examples ###

    Now analyze the following context and find all triplets.
    
    Context: {context}

    Triplets: 
    [/INST]
    """
)

chain = prompt | llm

context = "Bob went to Australia to see rich wildlife"

res = chain.invoke({"context": context})

print(res)
