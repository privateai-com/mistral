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

            ### Example ###

            This example shows extraction of triplets that contain scientific designations such as
            "HERC2-OCA2 locus", "SNP rs12913832". You must use this designations without any changes.
            It also shows you the way to use abbreviations that you have already seen in the context. For example
            in phrase "research field called forensic DNA phenotyping (FDP)" you can see that "FDP" stands for 
            "forensic DNA phenotyping" so you should use "FDP" instead of "forensic DNA phenotyping" in all
            triplets after this phrase.

            Context: In recent decades, the use of genetic polymorphisms related to specific phenotypes, 
            such as eye color, has greatly contributed to the development of the research field called 
            forensic DNA phenotyping (FDP), enabling the investigators of crime cases to 
            reduce the number of suspects, making their work faster and more precise. Eye color 
            is a polygenic phenotype, and many genetic variants have been highlighted, with the major contributor 
            being the HERC2-OCA2 locus, where many single nucleotide variations (SNPs) were identified. 
            Interestingly, the HERC2-OCA2 locus, containing the intronic SNP rs12913832, the major eye 
            color determinant, shows a high level of evolutionary conservation across many species of vertebrates. 
            Currently, there are some genetic panels to predict eye color by genomic DNA analysis, even if the 
            exact role of the SNP variants in the formation of eye color is still poorly understood, with a 
            low level of predictivity in the so-called intermediate eye color.
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
                    "link": "contributed to",
                    "object": "development of forensic DNA phenotyping (FDP)"
                }},
                {{   
                    "subject": "FDP development",
                    "link": "enables",
                    "object": "investigators of crime cases"
                }},
                {{   
                    "subject": "FDP development",
                    "link": "reduces",
                    "object": "number of suspects"
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
        
            This is another important example of rephrasing. For example
            phrase "Previous publications regarding possible factors contributing to pulmonary function impairment" 
            should be reduced to triplet
            {{
                "subject": "Previous publications",
                "link": "described",
                "object": "possible factors of pulmonary function impairment"
            }}
            You can see that "regarding" was replaced with "described". That's done in order for 
            a link to contain a verb.
            The same goes for phrase "idiopathic scoliosis, which can be considered another factor which may impact pulmonary testing results".
            It can be replaced with "idiopathic scoliosis, impacts pulmonary testing results". And the following triplet should be formed:
            {{   
                "subject": "Idiopathic scoliosis",
                "link": "may impact",
                "object": "pulmonary testing results"
            }}

            Context: Spine and trunk alignment can be altered due to idiopathic scoliosis (IS), 
            and this can impair pulmonary function in the case of spinal curvatures developing in the thoracic region. 
            Previous publications regarding possible factors contributing to pulmonary function impairment 
            revealed that radiological parameters such as thoracic Cobb angle, thoracic kyphosis angle, the number 
            of vertebrae involved and the limitation of rib cage mobility might correlate with the pulmonary parameters. 
            Due to spine deformity, a loss of body height is observed in patients with idiopathic scoliosis, which 
            can be considered another factor which may impact pulmonary testing results.
            Your answer:
            [
                {{   
                    "subject": "Spine and trunk alignment",
                    "link": "can be altered due to",
                    "object": "idiopathic scoliosis (IS)"
                }},
                {{   
                    "subject": "Spine and trunk alignment alteration”,
                    "link": "can impair",
                    "object": "pulmonary function"
                }},
                {{   
                    "subject": "Pulmonary function",
                    "link": "can be impaired in case of",
                    "object": "spinal curvatures"
                }},
                {{   
                    "subject": "Spinal curvatures”,
                    "link": "are developing in",
                    "object": "thoracic region"
                }},
                {{   
                    "subject": "Previous publications",
                    "link": "described",
                    "object": "possible factors of pulmonary function impairment"
                }},
                {{   
                    "subject": "Radiological parameters",
                    "link": “include",
                    "object": "thoracic Cobb angle"
                }},
                {{   
                    "subject": "Radiological parameters",
                    "link": “include",
                    "object": "thoracic kyphosis angle"
                }},
                {{   
                    "subject": "Radiological parameters",
                    "link": “include",
                    "object": "number of vertebrae involved"
                }},
                {{   
                    "subject": "Radiological parameters",
                    "link": “include",
                    "object": "limitation of rib cage mobility"
                }},
                {{   
                    "subject": "Loss of body height",
                    "link": "is observed in",
                    "object": "patients with idiopathic scoliosis"
                }},
                {{   
                    "subject": "Idiopathic scoliosis",
                    "link": "may impact",
                    "object": "pulmonary testing results"
                }}
            ]


            ### Example ###

            This example also shows the way to use short scientific designations (abbreviations) instead 
            of full words.
            For example, in the context it's clear that "ID" stands for "iron deficiency". So you should use ID instead of "iron deficiency"
            in triplets as well.

            Context: Anemia and iron deficiency (ID) are frequently encountered in patients with chronic heart failure (CHF). 
            They affect the quality of life and reduce the exercise capacity of patients by limiting their physical efficiency. 
            The presence of anemia and/or ID is associated with a poor outcome in patients with CHF and linked to an 
            increased mortality. ID can be caused by insufficient iron absorption or chronic blood losses resulting in 
            low iron storage, termed as absolute or true ID being reflected by low circulating concentrations of iron 
            and of the iron storage protein ferritin. ID can also originate from inflammation‐driven alterations of 
            iron homeostasis leading to defective iron utilization and transport, termed as functional ID being reflected 
            by low circulating iron but normal or increased ferritin concentrations.
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
                }},
            ]

            ### Example ###
            
            This examples shows that sometimes objects in triplets could contain many words and cannot be any shorter.
            For example phrase "cardiac arrest refractory to conventional cardiopulmonary resuscitation (CPR)" should be put
            into the object as it is, without any rephrasing.
            This example also shows the way to include abbreviations in the same part of triplet as the full term. For example,
            "Extracorporeal membrane oxygenation" in short is "ECMO" so they should be both placed in the same subject like so:
            "subject": "Extracorporeal membrane oxygenation (ECMO)".

            Context: Extracorporeal membrane oxygenation (ECMO) is a rescue therapy used to stabilize 
            patients with hemodynamic compromise such as refractory cardiogenic shock or cardiac arrest. 
            When used for cardiac arrest, ECMO is also known as extracorporeal cardiopulmonary resuscitation (ECPR). 
            We conducted a health technology assessment of venoarterial ECMO for adults (aged ≥ 18 years) 
            with cardiac arrest refractory to conventional cardiopulmonary resuscitation (CPR) or with 
            cardiogenic shock refractory to conventional medical management (i.e., drugs, mechanical support 
            such as intra-aortic balloon pump and temporary ventricular assist devices).
            Your answer:
            [
                {{   
                    "subject": "Extracorporeal membrane oxygenation (ECMO)",
                    "link": "is",
                    "object": "rescue therapy"
                }},
                {{   
                    "subject": "Extracorporeal membrane oxygenation (ECMO)”,
                    "link": "is used to stabilize",
                    "object": "patients with hemodynamic compromise"
                }},
                {{   
                    "subject": "Hemodynamic compromise”,
                    "link": "includes",
                    "object": "refractory cardiogenic shock or cardiac arrest"
                }},
                {{   
                    "subject": "ECMO used for cardiac arrest”,
                    "link": "is known as",
                    "object": "extracorporeal cardiopulmonary resuscitation (ECPR)"
                }},
                {{   
                    "subject": "We",
                    "link": "conducted",
                    "object": "health technology assessment"
                }},
                {{   
                    "subject": "Health technology assessment",
                    "link": “is used for",
                    "object": "venoarterial ECMO for adults"
                }},
                {{   
                    "subject": "Adults",
                    "link": “have",
                    "object": "cardiac arrest refractory to conventional cardiopulmonary resuscitation (CPR)"
                }},
                {{   
                    "subject": "Adults",
                    "link": “have",
                    "object": “cardiogenic shock refractory to conventional medical management” 
                }},
                {{   
                    "subject": "Conventional medical management",
                    "link": “includes",
                    "object": "drugs and mechanical support"
                }},
                {{   
                    "subject": "Mechanical support",
                    "link": “includes",
                    "object": "intra-aortic balloon pump and temporary ventricular assist devices"
                }}
            ]

            ### Example ###

            This example shows the correct way to form multiple triplets with the same subject.
            For example, "Hepatocellular carcinoma (HCC)" is present as subject in 2 triplets, 
            "Rist factors" is present as subject in 3 triplets, "Available treatment options"
            is present as subject in 3 triplets, "Optimal treatment options" is present as subject
            in 5 triplets.

            Context: Liver neoplasms are a global health challenge worldwide, with high incidence and mortality rates. 
            Hepatocellular carcinoma (HCC) is the most common type of primary liver cancer, originating from the hepatocytes, 
            which are the main functional cells of the liver. It is a malignant tumor that often occurs in the context of 
            chronic liver disease, such as cirrhosis or chronic hepatitis B or C infections. Other risk factors include 
            alcohol abuse, non‐alcoholic fatty liver disease, and exposure to certain toxins like aflatoxin. Available 
            treatment options include surgery, ablation therapies, embolization therapies. The appropriate treatment option 
            for an individual patient is a complex process that takes into consideration several factors such as staging 
            of the cancer, liver function, tumor size, and location, as well as the patient's overall health.
            Your answer:
            [
                {{   
                    "subject": "Liver neoplasms",
                    "link": "are",
                    "object": "global health challenge worldwide"
                }},
                {{   
                    "subject": "Liver neoplasms”,
                    "link": "have",
                    "object": "high incidence and mortality rates"
                }},
                {{   
                    "subject": "Hepatocellular carcinoma (HCC)”,
                    "link": "is",
                    "object": "most common type of primary liver cancer"
                }},
                {{   
                    "subject": "Hepatocellular carcinoma (HCC)”,
                    "link": "originates from",
                    "object": "hepatocytes"
                }},
                {{   
                    "subject": "Hepatocytes",
                    "link": "are",
                    "object": "main functional cells of the liver"
                }},
                {{   
                    "subject": "Malignant tumor",
                    "link": “often occurs in the context of",
                    "object": "chronic liver disease"
                }},
                {{   
                    "subject": Chronic liver disease",
                    "link": “includes",
                    "object": "cirrhosis or chronic hepatitis B or C infections"
                }},
                {{   
                    "subject": "Risk factors",
                    "link": “include",
                    "object": “alcohol abuse” 
                }},
                {{   
                    "subject": "Risk factors",
                    "link": “include",
                    "object": “non‐alcoholic fatty liver disease” 
                }},
                {{   
                    "subject": "Risk factors",
                    "link": “include",
                    "object": “exposure to certain toxins like aflatoxin” 
                }},
                {{   
                    "subject": "Available treatment options",
                    "link": “include",
                    "object": “surgery” 
                }},
                {{   
                    "subject": "Available treatment options",
                    "link": “include",
                    "object": “ablation therapies” 
                }},
                {{   
                    "subject": "Available treatment options",
                    "link": “include",
                    "object": “embolization therapies” 
                }},
                {{   
                    "subject": "Optimal treatment options",
                    "link": “is",
                    "object": “complex process” 
                }},
                {{   
                    "subject": "Optimal treatment options",
                    "link": “takes into account",
                    "object": “staging of the cancer” 
                }},
                {{   
                    "subject": "Optimal treatment options",
                    "link": “takes into account",
                    "object": “liver function” 
                }},
                {{   
                    "subject": "Optimal treatment options",
                    "link": “takes into account",
                    "object": “tumor size and location” 
                }},
                {{   
                    "subject": "Optimal treatment options",
                    "link": “takes into account",
                    "object": “patient’s overall health” 
                }}
            ]


            ### End of examples ###

            Now analyze the following context and find all triplets.

            Context: {context}

            Your answer: 
        """
    }
]
