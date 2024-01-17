from transformers import AutoTokenizer
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import find_dotenv, load_dotenv
from text_reader import read_files, write_triplets
from pathlib import Path
import json

# Load OpenAI API token
load_dotenv(find_dotenv())


PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")

llm = OpenAI(
    model_name="gpt-3.5-turbo-instruct", 
    temperature=0.1, 
    max_tokens=1024 # Needs to be enough for all output triplets
)

prompt = PromptTemplate.from_template(
    """
    [INST] 
    You are a helpful assistant. You must analyze the given context and find all triplets in it.

    A triplet is a collection of 3 parts: a subject, a link, an object.
    A subject is connected with an object via a link.
    In most cases, a subject and an object contain nouns and adjectives and links contain verbs.

    Extracted triplets will be used by other people to quickly understand the context without reading it whole. Thus, extract
    only meaningful triplets that might be helpful to understand the context.

    Connecting a subject, a link and an object from one triplet must result in meaningful sentence. 
    If connecting a subject, a link and an object from the triplet does not result in a sentence, ignore this triplet.

    Extracted triplets will be parsed into a JSON object and then used to draw a knowledge graph based on that object.
    That means you may be given the same context multiple times and you must extract exactly the same triplets each time. 
    Because subject and object of the triplet will be used as nodes of the graph. And link of the triplet will be 
    used as an edge between these two nodes.

    Maximum length of subject string is 25 characters. If it's longer, rephrase it to fit into 25 characters.
    Maximum length of link string is 25 characters. If it's longer, rephrase it to fit into 25 characters.
    Maximum length of object string is 25 characters. If it's longer, rephrase it to fit into 25 characters.
    Each of 3 parts of triplet must be maximum of 25 characters long.

    If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

    Output only the triplets and nothing else. Do not make up any new triplets, stick strictly to the context.

    You must output all triplets in a valid JSON format. Use only this format for all triplets and nothing else:
    
    [ 
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
    ]


    Let's look at some examples:

    ### Good Example 1 ###
    Context: "Bob went to Walmart to buy cheap clothes."
    Triplets:
    [
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
            "subject": "Cheap clothes",
            "link": "Are sold in",
            "object": "Walmart"
        }}
    ]


    ### Good Example 2 ###
    Context: "The disadvantage of this design is that Nagant revolvers were laborious and time-consuming to reload"
    Triplets:
    [
        {{  
            "subject": "Nagant revolvers",
            "link": "Were",
            "object": "Hard to reload"
        }}
    ]

    ### Good Example 3 ###
    Context: "Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop."
    Triplets:
    [
        {{  
            "subject": "Chicken",
            "link": "Is",
            "object": "Cooked"
        }},
        {{
            "subject": "Ferrari",
            "link": "Is",
            "object": "Fast"
        }},
        {{
            "subject": "Winter",
            "link": "Is",
            "object": "In Norway"
        }}
    ]
    Please note, that there are no triplets in the "Placebo" and "George Dunlop" sentences.


    ### Good Example 4 ###
    Context: "Soap"
    Triplets: No triplets

    ### Good Example 5 ###
    Context: "Kendrick Lamar"
    Triplets: No triplets

    ### Bad Example 1 ###
    Context: "Australia has reach wildlife"
    Wrong triplets:
    [
        {{  
            "subject": "Australia",
            "link": "Is",
            "object": "Rich wildlife"
        }},
    ]
    Correct triplets:
    [
        {{  
            "subject": "Australia",
            "link": "Has",
            "object": "Rich wildlife"
        }},
    ]
    So pay attention to the verb in the link


    ### End of examples ###

    Now analyze the following context and find all triplets.
    
    Context: {context}

    Triplets: 
    [/INST]
    """
)

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
    if "No triplets" not in res:
        # Load string into a JSON object
        parsed_json = json.loads(res)
        for triplet in parsed_json:
            file_triplets.append(triplet)
    # TODO: Maybe append "None" to triplets in this case?
    # If no triplets were found, an empty list will be returned
    all_triplets.append(file_triplets)
print("Triplets extracted!")


print("Writing triplets into files...")
# Write triplets in corresponding files
write_triplets(PAPERS_PATH, all_triplets)
print("Triplets written into files!")
