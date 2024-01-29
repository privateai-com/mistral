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

            For example in context "Bipolar disorder is known as manic depression" subject in "Bipolar disorder", 
            object is "manic depression" and relation is "is known as".
            This sentence may be represented as a triplet in JSON format:
            {{   
                "subject": "Bipolar disorder",
                "link": "is known as",
                "object": "manic depression"
            }}

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

            ### Example ### 

            In this example you are shown a correct way to form multiple triplets from a single sentence with 
            homogeneous members. For example "Obesity is a complex multifactorial condition with numerous possible biological, 
            behavioural and environmental determinants" has homogeneous members: "biological determinants", "behavioural determinants"
            and "environmental determinants". So a total of 3 triplets should be formed from this sentence.
            The same goes for sentece "promotes energy imbalance through the marketing, affordability and availability 
            of energy dense foods". It has 3 homogeneous members: "marketing", "affordability of dense foods",
            and "availability of dense foods". So a total of 3 triplets should be formed from this sentence.

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
                    "object": "biological determinants"
                }},
                {{   
                    "subject": "Obesity",
                    "link": "implies",
                    "object": "behavioural determinants"
                }},
                {{   
                    "subject": "Obesity",
                    "link": "implies",
                    "object": "environmental determinants"
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
                    "object": "marketing"
                }},
                {{   
                    "subject": "Energy imbalance",
                    "link": "is promoted by",
                    "object": "affordability of energy dense foods"
                }},
                {{   
                    "subject": "Energy imbalance",
                    "link": "is promoted by",
                    "object": "availability of energy dense foods"
                }},
                {{   
                    "subject": "Obesogenic environment",
                    "link": “promotes",
                    "object": "decreases in physical activity"
                }},
                {{   
                    "subject": "Obesogenic environment",
                    "link": “promotes",
                    "object": "increases in screen‐based sedentary pursuits"
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
                    "link": "are",
                    "object": "prescribed"
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
                    "object": "diet"
                }},
                {{   
                    "subject": "Behavioural components",
                    "link": "are",
                    "object": "physical activity"
                }},
                {{   
                    "subject": "Behavioural components",
                    "link": "are",
                    "object": "sedentary behaviour"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "are supported by",
                    "object": "theory‐based behaviour‐change techniques"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "are supported to help sustain",
                    "object": "positive changes"
                }},
                {{   
                    "subject": "Behaviour‐changing interventions",
                    "link": "are supported to prevent",
                    "object": "relapse"
                }}
            ]


            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
