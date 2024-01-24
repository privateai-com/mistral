messages = [
    {
        "role": "user", 
        "content": """
            You are a helpful assistant. You must analyze the given context and find all triplets in it.
            Study the following instructions. Strictly follow each of them. 
            Each instruction has a header in square brackets.

            [Nature of triplet]
            A triplet is a collection of 3 parts: a subject, a link, an object.
            Each part of triplet is essential. Each triplet must contain all parts: subject, link, object.
            Triplets with less then 3 parts are unacceptable.
            Subject and object contain nouns and adjectives and links contain verbs.

            [Usage of triplets in real life]
            Extracted triplets will be used by other people to quickly understand the context without 
            reading it whole. Thus, extract all possible triplets. Do not pass any triplets even if they
            are not as important as others. Analyze each sentence. Do not skip any senrences.

            [Length of parts of triplets]
            Each part of triplet must contain maximum of 4 words. For example, if object is:
            "Strong relationships full of trust and love", rephrase it to "Strong relationships".
            If any part of triplet can be divided into new triplets - do it. For example if object is
            "Mike went out to see Bob, Alice and dad", divide it into three triplets each containing
            "Bob", "Alice" and "dad" respectively.
            Each part of triplets must contain something. Empty objects, links or subjects are unacceptable. 

            [Insufficient context]
            If no triplets can be found in the context, say "No triplets". Say only this and nothing else.
            If context in not enough to form any triplets, say "No triplets". Exactly that.


            [Output format]
            You must output all triplets in a valid JSON format. 
            Each openening curly brace must have a closing curly brace.
            Each opening square bracket must have a closing square bracket.

            [Additional commets]
            You should not make any comments about the context.
            There are only two options of what your output must look like:
            Option 1: A valid JSON object like in the Examples below
            Option 2: "No triplets"

            Let's look at some examples:

            ### Example ###
            Context: "Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop."
            Your answer: "No triplets"

            ### Example ###
            Context: "Soap"
            Your answer: "No triplets"

            ### Example ###
            Context: "Kendrick Lamar"
            Your answer: "No triplets"

            ### Example ###
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

            ### Example ###
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

            ### Example ###
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
