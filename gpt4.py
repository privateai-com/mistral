from transformers import AutoTokenizer
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import find_dotenv, load_dotenv

# Load OpenAI API token
load_dotenv(find_dotenv())

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.1)

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

context_examples = [
    """Bob went to Australia to see rich wildlife""",
    """Bananas are yellow""",
    """Conputer""",
    """After purchasing rights to Steig's book in 1991,
    Steven Spielberg sought to produce a traditionally-animated film adaptation, but John H. Williams
    convinced him to bring the project to the newly founded DreamWorks in 1994. Jeffrey Katzenberg, along with
    Williams and Aron Warner, began development on Shrek in 1995, immediately following the studio's purchase of the rights
    from Spielberg. Chris Farley was cast as the voice for the title character, recording most of the required dialogue,
    but died in 1997 before his work on the film was finished; Myers was hired to replace him, and gave Shrek
    his Scottish accent. The film was initially intended to be created using motion capture, but after poor test
    results, the studio hired Pacific Data Images to complete the final computer animation. Shrek parodies
    other fairy tale adaptations, primarily animated Disney films.""",
    """
    Macromolecule blotting is a process performed after gel electrophoresis. An alkaline solution is prepared in a container. 
    A sponge is placed into the solution and an agarose gel is placed on top of the sponge. Next, nitrocellulose paper 
    is placed on top of the agarose gel and a paper towels are added on top of the nitrocellulose paper to apply pressure. 
    The alkaline solution is drawn upwards towards the paper towel. During this process, the DNA denatures in 
    the alkaline solution and is carried upwards to the nitrocellulose paper. The paper is then placed into a plastic bag 
    and filled with a solution full of the DNA fragments, called the probe, found in the desired sample of DNA. The 
    probes anneal to the complementary DNA of the bands already found on the nitrocellulose sample. Afterwards, 
    probes are washed off and the only ones present are the ones that have annealed to complementary DNA on the paper. 
    Next the paper is stuck onto an x ray film. The radioactivity of the probes creates black bands on the film, called 
    an autoradiograph. As a result, only similar patterns of DNA to that of the probe are present on the film. 
    This allows us the compare similar DNA sequences of multiple DNA samples. The overall process results in a precise 
    reading of similarities in both similar and different DNA sample
    """
]


for ex in context_examples:
    res = chain.invoke({"context": ex})
    print(res)
