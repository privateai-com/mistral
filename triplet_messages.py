triplet_messages = [
    {
        "role": "user", 
        "content": """
            You are a computer program. Your functionality is the following:
            1. Receive text as input
            2. Analyze it and find all relations (called triplets)
            3. Output a JSON object with all relations (triplets)

            The triplet is a pair of entities connected with a relation between them. 
            Entities are called a subject and an object.
            Relation is called a link.

            If no triplets can be found in the context, say "No triplets". Say only this two words and nothing else.
            For example, context "Guitar music" does not have enough information to form a triplet. Say "No triplets" in this case.
            Do not try to give any other comments like "The context does not provide enough information".

            For example in context "Bipolar disorder is known as manic depression" subject in "Bipolar disorder", 
            object is "manic depression" and relation is "is known as".
            This sentence may be represented as a triplet in JSON format:
            {{   
                "subject": "Bipolar disorder",
                "link": "is known as",
                "object": "manic depression"
            }}

            ### Example ###

            Context: CoolerMaster
            Your answer: No triplets.

            ### Example ###

            Context: Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop.
            Your answer: No triplets.

            ### Example ###

            Context: A mitochondrion (/ˌmaɪtəˈkɒndriən/;[1] pl.: mitochondria) is an organelle found in the cells 
            of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure 
            and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the 
            cell as a source of chemical energy.[2] They were discovered by Albert von Kölliker 
            in 1857[3] in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898
            Your answer: 
            [
                {{   
                    "subject": "Mitochondria",
                    "link": "is",
                    "object": "organelle"
                }},
                {{   
                    "subject": "Mitochondria",
                    "link": "was found in",
                    "object": "cells of most eukaryotes"
                }},
                {{
                    "subject": "Eukaryotes",
                    "link": "are",
                    "object": "animals, plants and fungi"
                }}
                {{   
                    "subject": "Mitochondria",
                    "link": "has",
                    "object": "double membrane structure"
                }},
                {{   
                    "subject": "Mitochondria",
                    "link": "uses",
                    "object": "aerobic respiration"
                }},
                {{   
                    "subject": "Mitochondria",
                    "link": "generates",
                    "object": "adenosine triphosphate (ATP)"
                }},
                {{   
                    "subject": "Adenosine triphosphate (ATP)",
                    "link": "is used as",
                    "object": "source of chemical energy"
                }},
                {{   
                    "subject": "Mitochondria",
                    "link": "was discovered by",
                    "object": "Albert von Kölliker"
                }},
                {{   
                    "subject": "Mitochondria",
                    "link": "was discovered in",
                    "object": "1853"
                }},
                {{   
                    "subject": "Mitochondria",
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

            Context: Obesity is a complex multifactorial condition with numerous possible biological, 
            behavioural and environmental determinants. Many children now grow up in an obesogenic 
            environment that promotes energy imbalance through the marketing, affordability and availability 
            of energy dense foods, coupled with decreases in physical activity and increases in screen‐based 
            sedentary pursuits. Therefore, behaviour‐changing interventions that aim to improve dietary intake, 
            increase physical activity levels and reduce sedentary behaviours are often prescribed, and were 
            recommended as a treatment option for childhood obesity. Behaviour‐changing interventions may target 
            just one behavioural component (e.g. diet, physical activity or sedentary behaviour) or combine several 
            components, and are often supported by theory‐based behaviour‐change techniques to help sustain positive 
            changes and prevent relapse.
            Your answer:
            [
                {{   
                    "subject": "Obesity",
                    "link": "is",
                    "object": "complex multifactorial condition"
                }},
                {{   
                    "subject": "Obesity",
                    "link": "implies",
                    "object": "biological, behavioural and environmental determinants"
                }},
                {{   
                    "subject": "Many children",
                    "link": "grow up in",
                    "object": "obesogenic environment"
                }},
                {{   
                    "subject": "Obesogenic environment",
                    "link": "promotes",
                    "object": "energy imbalance"
                }},
                {{   
                    "subject": "Energy imbalance",
                    "link": "is promoted by",
                    "object": "marketing, affordability and availability of energy dense foods"
                }},
                {{   
                    "subject": "Obesogenic environment",
                    "link": “promotes",
                    "object": "decreases in physical activity and increases in screen-based sedentary pursuits"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "aim to improve",
                    "object": "dietary intake"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "aim to increase",
                    "object": "physical activity levels"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "aim to reduce",
                    "object": "sedentary behaviours"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "were recommended as",
                    "object": "treatment option for childhood obesity"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "may target",
                    "object": "one behavioural component"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "may combine",
                    "object": "several behavioural components"
                }},
                {{   
                    "subject": "Behavioural components",
                    "link": "are",
                    "object": "diet, physical activity, sedentary behaviour"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "are supported by",
                    "object": "theory‐based behaviour‐change techniques"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "are supported to",
                    "object": "sustain positive changes and prevent relapse"
                }},
            ]

            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
