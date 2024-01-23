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
            <- No curly brace here
        ]
        Correct format:
        [
            {{  
                "subject": "Alice",
                "link": "bought",
                "object": "Ethereum"
            }} <- This curly brace must be here
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

        ### Example 9 ###
        Context: "Vitamin C is sold as a topical `serum` ingredient to treat melasma (dark pigment spots) and wrinkles on the face"
        Wrong triplets:
        [
            {{  
                "subject": "Vitamin C",
                "link": "is sold as topical 'serum' ingredient to treat",
                "object": "melasma (dark pigment spots)" 
            }},
            {{  
                "subject": "Vitamin C",
                "link": "is sold as topical 'serum' ingredient to treat",
                "object": "wrinkles on the face" 
            }}
        ]
        Correct triplets:
        [
            {{  
                "subject": "Vitamin C",
                "link": "is sold to treat",
                "object": "melasma and face wrinkles" 
            }}
        ]

        Note that in Example 9 links and objects of both Wrong triplets must be rephrased and connected into one triplet.

        ### Example 10 ###
        Context: "Bipolar disorder, previously known as manic depression, is a mental disorder characterized by 
        periods of depression and periods of abnormally elevated mood that each last from days to weeks.
        If the elevated mood is severe or associated with psychosis, it is called mania; if it is less severe, 
        it is called hypomania. During mania, an individual behaves or feels abnormally energetic, happy or irritable,
        and they often make impulsive decisions with little regard for the consequences.
        There is usually also a reduced need for sleep during manic phases.
        During periods of depression, the individual may experience crying and have a negative outlook on 
        life and poor eye contact with others"
        Triplets: 
        [
            {{   
                "subject": "Bipolar disorder",
                "link": "is known as",
                "object": "manic depression"
            }},
            {{   
                "subject": "Bipolar disorder",
                "link": "is",
                "object": "mental disorder"
            }},
            {{   
                "subject": "Bipolar disorder",
                "link": "is characterized by",
                "object": "periods of depression and periods of abnormally elevated mood"
            }},
            {{   
                "subject": "periods of depression and periods of abnormally elevated mood",
                "link": "last",
                "object": "from days to weeks"
            }},
            {{   
                "subject": "abnormally elevated mood associated with psychosis",
                "link": "is called",
                "object": "mania"
            }},
            {{   
                "subject": "less severe abnormally elevated mood",
                "link": "is called",
                "object": "hypomania"
            }},
            {{   
                "subject": "Individuals during mania period",
                "link": "feels",
                "object": "abnormally energetic, happy or irritable"
            }},
            {{   
                "subject": "Individuals during mania period",
                "link": "often makes",
                "object": "impulsive decisions"
            }},
            {{   
                "subject": "Individuals during mania period",
                "link": "often needs",
                "object": "less sleep"
            }},
            {{   
                "subject": "Individuals during depression period",
                "link": "may experience",
                "object": "crying"
            }},
            {{   
                "subject": "Individuals during depression period",
                "link": "have",
                "object": "negative outlook on life"
            }},
            {{   
                "subject": "Individuals during depression period",
                "link": "avoid",
                "object": "eye contact"
            }}
        ]

        ### Example 11 ###
        Context: "A mitochondrion (/ˌmaɪtəˈkɒndriən/;[1] pl.: mitochondria) is an organelle found in the cells 
        of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure 
        and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the 
        cell as a source of chemical energy.[2] They were discovered by Albert von Kölliker 
        in 1857[3] in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898"
        Triplets: 
        [
            {{   
                "subject": "Mitochondrion",
                "link": "is",
                "object": "organelle"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "was found in",
                "object": "cells of most eukaryotes"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "has",
                "object": "double membrane structure"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "uses",
                "object": "aerobic respiration"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "generates",
                "object": "adenosine triphosphate (ATP)"
            }},
            {{   
                "subject": "Adenosine triphosphate (ATP)",
                "link": " is used by cell as",
                "object": "source of chemical energy"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "was discovered by",
                "object": "Albert von Kölliker"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "was discovered in",
                "object": "1853"
            }},
            {{   
                "subject": "Mitochondrion",
                "link": "was discovered in",
                "object": "voluntary muscles of insects"
            }},
            {{   
                "subject": "Term mitochondrion",
                "link": "was coined by",
                "object": "Carl Benda"
            }},
            {{   
                "subject": "Term mitochondrion",
                "link": "was coined in",
                "object": "1898"
            }}
        ]

        ### Example 12 ###
        Context: "The most prevalent transmitter is glutamate, which is excitatory at well over 90% of the synapses in 
        the human brain.[28] The next most prevalent is gamma-Aminobutyric Acid, or GABA, which is inhibitory at more 
        than 90% of the synapses that do not use glutamate. Although other transmitters are used in fewer synapses, they may 
        be very important functionally. The great majority of psychoactive drugs exert their effects by altering the 
        actions of some neurotransmitter systems. Addictive drugs such as cocaine and amphetamines exert their effects 
        primarily on the dopamine system.""
        Triplets:
        [
            {{   
                "subject": "Most prevalent transmitter",
                "link": "is",
                "object": "glutamate"
            }},
            {{   
                "subject": "Glutamate",
                "link": "is excitatory at",
                "object": "over 90% of the synapses in the human brain"
            }},
            {{   
                "subject": "Second most prevalent transmitter",
                "link": "is",
                "object": "gamma-Aminobutyric Acid (GABA)"
            }},
            {{   
                "subject": "Gamma-Aminobutyric Acid ",
                "link": "is excitatory at",
                "object": "over 90% of the synapses that do not use glutamate"
            }},
            {{   
                "subject": "Other transmitters",
                "link": "are used in",
                "object": "fewer synapses"
            }},
            {{   
                "subject": "Other transmitters",
                "link": are still",
                "object": "very important functionally"
            }},
            {{   
                "subject": "Psychoactive drugs",
                "link": "exert their effects by",
                "object": "altering the actions of neurotransmitter systems"
            }},
            {{   
                "subject": "Addictive drugs",
                "link": " exert their effects on",
                "object": "dopamine system"
            }}
        ]

        ### End of examples ###

        Now analyze the following context and find all triplets.

        Context: {context}

        Triplets: 
        """
    }
]
