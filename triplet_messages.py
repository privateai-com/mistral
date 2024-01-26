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

            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
