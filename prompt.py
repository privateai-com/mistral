messages = [
    {
        "role": "user", 
        "content": """
            You are a strict, laconic and concise assistant. You must analyze the given context and find all triplets in it.

            A triplet is a collection of 3 parts: a subject, a link, an object.

            Maximum length of each part of triplet must be 50 characters. 
            Each of 3 parts of triplet must not be empty.

            Do not make up any new triplets, stick strictly to the context.
            If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

            You must output all triplets in a valid JSON format. 

            There are only two options of what your output must look like:
            Option 1: A valid JSON object
            Option 2: "No triplets"
            Do not make any other comments except the two options above!

            Bob went to Walmart to buy cheap clothes.

            Triplets:
        """
    },
    {
        "role": "assistant", 
        "content": """
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
        """
    },
    {
        "role": "user", 
        "content": """
            The disadvantage of this design is that Nagant revolvers were laborious and time-consuming to reload
        """
    },
    {
        "role": "assistant", 
        "content": """
            [
                {{  
                    "subject": "Nagant revolvers",
                    "link": "had",
                    "object": "hard reloading"
                }}
            ]
        """
    },
    {
        "role": "user", 
        "content": """
            Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop.
        """
    },
    {
        "role": "assistant",
        "content": """
            No triplets
        """
    },
    {
        "role": "user",
        "content": """
            Soap
        """
    },
    {
        "role": "assistant",
        "content": """
            No triplets
        """
    },
    {
        "role": "user",
        "content": """
            Kendrick Lamar
        """
    },
    {
        "role": "assistant",
        "content": """
            No triplets
        """
    },
    {
        "role": "user",
        "content": """
            Australia has reach wildlife
        """
    },
    {
        "role": "assistant",
        "content": """
            [
                {{  
                    "subject": "Australia",
                    "link": "has",
                    "object": "rich wildlife"
                }}
            ]
        """
    },
    {
        "role": "user",
        "content": """
            Alice bought some Ethereum
        """
    },
    {
        "role": "assistant",
        "content": """
            [
                {{  
                    "subject": "Alice",
                    "link": "bought",
                    "object": "Ethereum"
                }}
            ]
        """
    },
    {
        "role": "user",
        "content": """
            Vitamin C is known as ascorbic acid. Vitamin C is known as ascorbate.
        """
    },
    {
        "role": "assistant",
        "content": """
            [
                {{  
                    "subject": "Vitamin C",
                    "link": "is known as",
                    "object": "ascorbic acid"
                }}
            ]
        """
    },
    {
        "role": "user",
        "content": """
            Vitamin C is sold as a topical `serum` ingredient to treat melasma (dark pigment spots) and wrinkles on the face
        """
    },
    {
        "role": "assistant",
        "content": """
            [
                {{  
                    "subject": "Vitamin C",
                    "link": "is sold to treat",
                    "object": "melasma and face wrinkles" 
                }}
            ]
        """
    },
    {
        "role": "user",
        "content": """
            Bipolar disorder, previously known as manic depression, is a mental disorder characterized by 
            periods of depression and periods of abnormally elevated mood that each last from days to weeks.
            If the elevated mood is severe or associated with psychosis, it is called mania; if it is less severe, 
            it is called hypomania. During mania, an individual behaves or feels abnormally energetic, happy or irritable,
            and they often make impulsive decisions with little regard for the consequences.
            There is usually also a reduced need for sleep during manic phases.
            During periods of depression, the individual may experience crying and have a negative outlook on 
            life and poor eye contact with others
        """
    },
    {
        "role": "assistant",
        "content": """
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
        """
    },
    {
        "role": "user",
        "content": """
            A mitochondrion (/ˌmaɪtəˈkɒndriən/;[1] pl.: mitochondria) is an organelle found in the cells 
            of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure 
            and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the 
            cell as a source of chemical energy.[2] They were discovered by Albert von Kölliker 
            in 1857[3] in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898"
        """
    },
    {
        "role": "assistant",
        "content": """
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
        """
    },
    {
        "role": "user",
        "content": """
            The most prevalent transmitter is glutamate, which is excitatory at well over 90% of the synapses in 
            the human brain.[28] The next most prevalent is gamma-Aminobutyric Acid, or GABA, which is inhibitory at more 
            than 90% of the synapses that do not use glutamate. Although other transmitters are used in fewer synapses, they may 
            be very important functionally. The great majority of psychoactive drugs exert their effects by altering the 
            actions of some neurotransmitter systems. Addictive drugs such as cocaine and amphetamines exert their effects 
            primarily on the dopamine system.
        """
    },
    {
        "role": "assistant",
        "content": """
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
        """
    },
    {
        "role": "user",
        "content": """
            {context}
        """
    }
]
