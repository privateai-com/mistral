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

            Context: The most prevalent transmitter is glutamate, which is excitatory at well over 90% of the synapses in 
            the human brain. The next most prevalent is gamma-Aminobutyric Acid, or GABA, which is inhibitory at more 
            than 90% of the synapses that do not use glutamate. Although other transmitters are used in fewer synapses, they may 
            have very important functionally. The great majority of psychoactive drugs exert their effects by altering the 
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
                    "link": "have",
                    "object": "very important functionally"
                }},
                {{   
                    "subject": "Psychoactive drugs",
                    "link": "exert their effect by",
                    "object": "altering the actions of neurotransmitter systems"
                }},
                {{   
                    "subject": "Addictive drugs",
                    "link": "exert their effects on",
                    "object": "dopamine system"
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


            ### Example ###

            This example shows the usage of scientific notations (abbreviations) from text in triplets.
            The abbreviations here are: "FDP", "HERC2-OCA2 locus", "SNP", "rs12913832". You should
            use them in triplets without changing.

            Context: In recent decades, the use of genetic polymorphisms related to specific phenotypes, such as eye color, 
            has greatly contributed to the development of the research field called forensic DNA phenotyping (FDP), 
            enabling the investigators of crime cases to reduce the number of suspects, making their work 
            faster and more precise. Eye color is a polygenic phenotype, and many genetic variants have been highlighted, 
            with the major contributor being the HERC2-OCA2 locus, where many single nucleotide variations (SNPs) were identified. 
            Interestingly, the HERC2-OCA2 locus, containing the intronic SNP rs12913832, the major eye color determinant, 
            shows a high level of evolutionary conservation across many species of vertebrates. Currently, there are some genetic 
            panels to predict eye color by genomic DNA analysis, even if the exact role of the SNP variants in 
            the formation of eye color is still poorly understood, with a low level of predictivity in the so-called intermediate eye color.
            Your answer:
            [
                {{   
                    "subject": "Genetic polymorphisms",
                    "link": "is related to",
                    "object": "specific phenotypes"
                }},
                {{   
                    "subject": "Example of specific phenotypes”,
                    "link": "is",
                    "object": "eye color"
                }},
                {{   
                    "subject": "Use of genetic polymorphisms",
                    "link": "has greatly contributed to",
                    "object": "development of forensic DNA phenotyping (FDP)"
                }},
                {{   
                    "subject": "Forensic DNA phenotyping development”,
                    "link": "enables",
                    "object": "investigators of crime cases to reduce the number of suspects"
                }},
                {{   
                    "subject": "Eye color",
                    "link": “is",
                    "object": "polygenic phenotype"
                }},
                {{   
                    "subject": "Many genetic variants of eye color",
                    "link": “have been",
                    "object": "highlighted"
                }},
                {{   
                    "subject": "Major contributor in genetic variants",
                    "link": "is",
                    "object": "HERC2-OCA2 locus"
                }},
                {{   
                    "subject": "Many single nucleotide variations (SNPs)",
                    "link": "were identified in",
                    "object": "HERC2-OCA2 locus"
                }},
                {{   
                    "subject": "HERC2-OCA2 locus",
                    "link": "contains",
                    "object": "intronic SNP rs12913832"
                }},
                {{   
                    "subject": "Intronic SNP rs12913832",
                    "link": "is",
                    "object": "major eye color determinant"
                }},
                {{   
                    "subject": "HERC2-OCA2 locus",
                    "link": "shows",
                    "object": "high level of evolutionary conservation"
                }},
                {{   
                    "subject": "Genetic panels",
                    "link": "predict",
                    "object": "eye color"
                }},
                {{   
                    "subject": "Eye color",
                    "link": "is predicted by",
                    "object": "genomic DNA analysis"
                }},
                {{   
                    "subject": "SNP variants",
                    "link": "are not understood in terms of",
                    "object": "formation of eye color"
                }},
                {{   
                    "subject": "Intermediate eye color",
                    "link": "have",
                    "object": "low level of predictivity"
                }}
            ]

            ### Example ###

            This example shows how to form triplets from long sentences. Last two sentences of the context
            are quite long. You should analyze each part of these sentences.

            Context: Anemia and iron deficiency (ID) are frequently encountered in patients with chronic heart failure (CHF). 
            They affect the quality of life and reduce the exercise capacity of patients by limiting their physical efficiency. 
            The presence of anemia and/or ID is associated with a poor outcome in patients with CHF and linked 
            to an increased mortality. ID can be caused by insufficient iron absorption or chronic blood losses resulting 
            in low iron storage, termed as absolute or true ID being reflected by low circulating concentrations of iron 
            and of the iron storage protein ferritin. ID can also originate from inflammation‐driven alterations of iron 
            homeostasis leading to defective iron utilization and transport, termed as functional ID being reflected by low 
            circulating iron but normal or increased ferritin concentrations.
            Your answer:
            [
                {{   
                    "subject": "Anemia and iron deficiency (ID)",
                    "link": "are frequently encountered in",
                    "object": "patients with chronic heart failure (CHF)"
                }},
                {{   
                    "subject": "Anemia and iron deficiency (ID)”,
                    "link": "affect",
                    "object": "quality of life"
                }},
                {{   
                    "subject": "Anemia and iron deficiency (ID)”,
                    "link": "reduce",
                    "object": "exercise capacity of patients"
                }},
                {{   
                    "subject": "Exercise capacity of patients”,
                    "link": "is being reduced by",
                    "object": "limiting physical efficiency"
                }},
                {{   
                    "subject": "Presence of anemia and/or ID",
                    "link": "is associated with",
                    "object": "poor outcome in patients with CHF"
                }},
                {{   
                    "subject": "Presence of anemia and/or ID",
                    "link": "is linked to",
                    "object": "increased mortality"
                }},
                {{   
                    "subject": "ID",
                    "link": “can be caused by",
                    "object": "insufficient iron absorption"
                }},
                {{   
                    "subject": "ID",
                    "link": “can be caused by",
                    "object": "chronic blood losses"
                }},
                {{   
                    "subject": "Insufficient iron absorption",
                    "link": “results in",
                    "object": "low iron storage"
                }},
                {{   
                    "subject": "Chronic blood losses",
                    "link": “results in",
                    "object": "low iron storage"
                }},
                {{   
                    "subject": "ID",
                    "link": "is reflected by",
                    "object": "low circulating concentrations of iron"
                }},
                {{   
                    "subject": "ID",
                    "link": "is reflected by",
                    "object": "low circulating concentrations of iron storage protein ferritin"
                }},
                {{   
                    "subject": "ID",
                    "link": "can originate from",
                    "object": "inflammation‐driven alterations of iron homeostasis"
                }},
                {{   
                    "subject": "Inflammation‐driven alterations of iron homeostasis",
                    "link": "leads to",
                    "object": "defective iron utilization and transport"
                }},
                {{   
                    "subject": "Defective iron utilization and transport",
                    "link": "is termed as",
                    "object": "functional ID"
                }},
                {{   
                    "subject": "Functional ID",
                    "link": "is reflected by",
                    "object": "low circulating iron"
                }},
                {{   
                    "subject": "Functional ID",
                    "link": "is reflected by",
                    "object": "normal or increased ferritin concentrations"
                }}
            ]



            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
