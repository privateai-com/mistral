triplet_messages = [
    {
        "role": "user", 
        "content": """
            You are a computer program. You must analyze the text and find all triplets in it.

            ### Example ###

            If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

            Context: Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop.
            Your answer: No triplets.

            ### Example ###

            If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

            Context: Soap
            Your answer: No triplets.

            ### Example ###

            In this example you are given a large text. In this case you must analyze it whole. Find triplets in each sentence, 
            between sentences and different parts of the text.
            In most cases links contain verbs in different forms. So pay attention to it.
            Long sentences like "Periods of depression and periods of abnormally elevated mood" are separated into 
            2 different triplets. All complex sentences must be separated into 2 or more triplets.

            Context: Bipolar disorder, previously known as manic depression, is a mental disorder characterized by 
            periods of depression and periods of abnormally elevated mood that each last from days to weeks.
            If the elevated mood is severe or associated with psychosis, it is called mania; if it is less severe, 
            it is called hypomania. During mania, an individual behaves or feels abnormally energetic, happy or irritable,
            and they often make impulsive decisions with little regard for the consequences.
            There is usually also a reduced need for sleep during manic phases.
            During periods of depression, the individual may experience crying and have a negative outlook on 
            life and poor eye contact with others
            Your answer: 
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
                    "object": "periods of depression"
                }},
                {{   
                    "subject": "Bipolar disorder",
                    "link": "is characterized by",
                    "object": "periods of abnormally elevated mood"
                }},
                {{   
                    "subject": "Periods of depression",
                    "link": "last",
                    "object": "from days to weeks"
                }},
                {{   
                    "subject": "Periods of abnormally elevated mood",
                    "link": "last",
                    "object": "from days to weeks"
                }},
                {{   
                    "subject": "Abnormally elevated mood",
                    "link": "is called",
                    "object": "mania"
                }},
                {{   
                    "subject": "Less severe abnormally elevated mood",
                    "link": "is called",
                    "object": "hypomania"
                }},
                {{   
                    "subject": "Individuals during mania period",
                    "link": "feel",
                    "object": "abnormally energetic, happy or irritable"
                }},
                {{   
                    "subject": "Individuals during mania period",
                    "link": "feel",
                    "object": "happy"
                }},
                {{   
                    "subject": "Individuals during mania period",
                    "link": "feel",
                    "object": "irritable"
                }},
                {{   
                    "subject": "Individuals during mania period",
                    "link": "often make",
                    "object": "impulsive decisions"
                }},
                {{   
                    "subject": "Individuals during mania period",
                    "link": "often need",
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

            In this example context contains special footnotes notations lile [1], [2]. They must be ignored.
            It also shows a perfect example of triplets. Each part of triplet it neither long, nor short and 
            all links contain verbs. You should try to find triplets like this in other contexts.

            Context: A mitochondrion (/ˌmaɪtəˈkɒndriən/;[1] pl.: mitochondria) is an organelle found in the cells 
            of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure 
            and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the 
            cell as a source of chemical energy.[2] They were discovered by Albert von Kölliker 
            in 1857[3] in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898
            Your answer: 
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
                    "link": "is used as",
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

            In this example your are shown how to rephrase long sentences. For example, in the sentence "The great majority of psychoactive 
            drugs exert their effects by altering the actions of some neurotransmitter systems" the subject is "Psychoactive drugs",
            the object is "altering the actions of some neurotransmitter systems" and the link is "exert their effects by". But 
            object can be replaced with just "actions of neurotransmitter systems", and link can be replaced with "alter".
            The same goes for "Addictive drugs such as cocaine and amphetamines exert their effects primarily on the dopamine system." The 
            subject is "Addictive drugs such as cocaine and amphetamines", the object is "dopamine system" and the link is "exert their effects".
            But subject can be replaced with "Addictive drugs" and link can be replaced with "affect".
            You must apply similar patterns of replacing long phrases to all other context parts.

            Context: The most prevalent transmitter is glutamate, which is excitatory at well over 90% of the synapses in 
            the human brain. The next most prevalent is gamma-Aminobutyric Acid, or GABA, which is inhibitory at more 
            than 90% of the synapses that do not use glutamate. Although other transmitters are used in fewer synapses, they may 
            be very important functionally. The great majority of psychoactive drugs exert their effects by altering the 
            actions of some neurotransmitter systems. Addictive drugs such as cocaine and amphetamines exert their effects 
            primarily on the dopamine system.
            Your answer:
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
                    "subject": "The next most prevalent transmitter",
                    "link": "is",
                    "object": "gamma-Aminobutyric Acid (GABA)"
                }},
                {{   
                    "subject": "Gamma-Aminobutyric Acid ",
                    "link": "is inhibitory at",
                    "object": "over 90% of the synapses that do not use glutamate"
                }},
                {{   
                    "subject": "Other transmitters",
                    "link": "are used in",
                    "object": "fewer synapses"
                }},
                {{   
                    "subject": "Other transmitters",
                    "link": are",
                    "object": "very important functionally"
                }},
                {{   
                    "subject": "Psychoactive drugs",
                    "link": "alter",
                    "object": "the actions of neurotransmitter systems"
                }},
                {{   
                    "subject": "Addictive drugs",
                    "link": "affect",
                    "object": "dopamine system"
                }}
            ]

            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
