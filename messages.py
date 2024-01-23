messages = [
    {
        "role": "user", 
        "content": """
        You are a helpful assistant. You must analyze the given context and find all triplets in it.
        Study the following instructions. Strictly follow each of them. 
        Each instruction has a header in square brackets.

        [Nature of triplet]
        A triplet is a collection of 3 parts: a subject, a link, an object.
        A subject is connected with an object via a link.
        In most cases, a subject and an object contain nouns and adjectives and links contain verbs.

        [Usage of triplets in real life]
        Extracted triplets will be used by other people to quickly understand the context without reading it whole. Thus, extract
        only meaningful triplets that might be helpful to understand the context.

        [Length of parts of tripleets]
        Maximum length of each part of triplet must be 50 characters. Only 50 charactes are allowed for each found part of triplet.
        Each of 3 parts of triplet must not be empty.

        [Insufficient context]
        Do not make up any new triplets, stick strictly to the context.
        If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

        [Output format]
        You must output all triplets in a valid JSON format. That means the output must contain correct amount of curly braces and square brackets.
        Each openening curly brace must have a closing curly brace.
        Each opening square bracket must have a closing square bracket.

        [Additional commets]
        You should not make any comments about the context.
        There are only two options of what your output must look like:
        Option 1: A valid JSON object like in the Examples below
        Option 2: "No triplets"

        [Examples]
        Let's look at some examples:

        ### Example 1 ###
        Context: "Bob went to Walmart to buy cheap clothes."
        Triplets:
        [
            {{   
                "subject": "Bob",
                "link": "went to",
                "object": "walmart"
            }},
            {{
                "subject": "Bob",
                "link": "went to buy",
                "object": "cheap clothes"
            }}
        ]


        ### Example 2 ###
        Context: "The disadvantage of this design is that Nagant revolvers were laborious and time-consuming to reload"
        Triplets:
        [
            {{  
                "subject": "Nagant revolvers",
                "link": "had",
                "object": "hard reloading"
            }}
        ]

        Note that is Example 2 you have to rephrase "laborious and time-consuming to reload" into "hard reloading"

        ### Example 3 ###
        Context: "Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop."
        Triplets: No triplets

        Note that in Example 3 such short sentences should form no triplets.

        ### Example 4 ###
        Context: "Soap"
        Triplets: No triplets

        ### Example 5 ###
        Context: "Kendrick Lamar"
        Triplets: No triplets

        ### Example 6 ###
        Context: "Australia has reach wildlife"
        Wrong triplets:
        [
            {{  
                "subject": "Australia",
                "link": "is",
                "object": "rich wildlife"
            }},
        ]
        Correct triplets:
        [
            {{  
                "subject": "Australia",
                "link": "has",
                "object": "rich wildlife"
            }},
        ]
        So pay attention to grammatical form of all words in the triplet. Especially verbs.

        ### Example 7 ###
        Context: "Alice bought some Ethereum"
        Wrong format:
        [
            {{  
                "subject": "Alice",
                "link": "bought",
                "object": "Ethereum"
        ]
        Correct format:
        [
            {{  
                "subject": "Alice",
                "link": "bought",
                "object": "Ethereum"
            }}
        ]
        Note that it is VERY important for you to follow the JSON format and close all curly braces and square brackets as in Example 7.

        ### Example 8 ###
        Context: "Vitamin C is known as ascorbic acid. Vitamin C is known as ascorbate."
        Wrong triplets:
        [
            {{  
                "subject": "Vitamin C",
                "link": "is known as",
                "object": "ascorbic acid" 
            }},
            {{  
                "subject": "Vitamin C",
                "link": "is known as",
                "object": "ascorbate"
            }}
        ]
        Correct triplets:
        [
            {{  
                "subject": "Vitamin C",
                "link": "is known as",
                "object": "ascorbic acid"
            }}
        ]

        Note that in Example 8 objects in both Wrong triplets ("Ascobric acid" and "Ascorbate") mean the same thing. They are synonymous.
        So you must combine them into one object and use it in one triplet as shown in Correct triplets above.

        ### End of examples ###

        Now analyze the following context and find all triplets.

        Context: {context}

        Triplets: 
        """
    }
]
