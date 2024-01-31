refactor_messages = [
    {
        "role": "user",
        "content": """
            You are a computer program. Your functionality is the following:
            1. Get a JSON string as input
            2. Modify/Enhance it
            3. Return a new JSON string
            Your actions must strictly follow the examples provided below.

            Each JSON string contains a triplet. Each triplet has 3 parts: subject, link, object.
            Triplet is surrounded by curly braces like so:
            {{   
                "subject": "Bipolar disorder",
                "link": "is known as",
                "object": "manic depression"
            }}

            You have to make the following:

            Your whole answer must be a valid JSON. Pay attention to how you use curly braces and square brackets. 

            Each triplet must contain exactly 3 parts: subject, link, object.
            So if object is not present, you must create it only using the context. For example:

            "subject": "Ability to generate electric signals",
            "link": "represented a significant innovation in the development of the nervous system"

            should be replaced with

            "subject": "Ability to generate electric signals",
            "link": "represented",
            "object": "a significant innovation in the development of the nervous system"

            If no triplets can be found in the context, say "No triplets". Say only this two words and nothing else.
            Do not try to give any other comments like "The context does not provide enough information".

            Make sure each part of the triplet is as short as possible. The optimal 
            length of each part is up to 5 words. For example:

            "link": "could be exploited as a strategy to"

            should be replaced with

            "link": "is used to"

            Both options must have the same meaning, but the second one is much shorter.

            Let's look at some examples:

            ### Example ###

            Context: No triplets.
            Your answer: No triplets.

            ### Example ###

            Context:
            [
                {{
                    "subject": "Accumulation of MDSCs associated with tumor growth",
                    "link": "could be because of",
                    "object": "various mechanisms"
                }},
                {{
                    "subject": "Various mechanisms",
                    "link": "include",
                    "object": "presence of excessive growth factors, cytokines, or inflammatory molecules"
                }},
                {{
                    "subject": "Presence of excessive growth factors, cytokines, or inflammatory molecules",
                    "link": "provide",
                    "object": "continuous survival signals"
                }},
                {{
                    "subject": "MDSCs",
                    "link": "express",
                    "object": "death receptor Fas"
                }},
                {{
                    "subject": "Fas",
                    "link": "is engaged by",
                    "object": "FasL"
                }},
                {{
                    "subject": "Activated T cells expressing FasL",
                    "link": "mediate apoptosis of MDSCs in vivo"
                }},
                {{
                    "subject": "Fas-FasL interactions",
                    "link": "could be exploited as a strategy to",
                    "object": "reduce MDSC levels in vivo"
                }}
            ]
            Your answer:
            [
                {{
                    "subject": "Accumulation of MDSCs",
                    "link": "could be because of",
                    "object": "various mechanisms"
                }},
                {{
                    "subject": "Various mechanisms",
                    "link": "include",
                    "object": [ 
                        "presence of excessive growth factors",
                        "presence of cytokines",
                        "presence of inflammatory molecules"
                    ]
                }},
                {{
                    "subject": [
                        "Presence of excessive growth factors",
                        "Presence of cytokines",
                        "Presence of inflammatory molecules"
                    ],
                    "link": "provides",
                    "object": "continuous survival signals"
                }},
                {{
                    "subject": "MDSCs",
                    "link": "express",
                    "object": "death receptor Fas"
                }},
                {{
                    "subject": "Fas",
                    "link": "is engaged by",
                    "object": "FasL"
                }},
                {{
                    "subject": "Activated T cells",
                    "link": "mediate apoptosis of"
                    "object": "MDSCs in vivo"
                }},
                {{
                    "subject": "Fas-FasL interactions",
                    "link": "are a strategy to",
                    "object": "reduce MDSC levels in vivo"
                }}
            ]

            ### Example ###

            Context:
            [
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "is", 
                    "object": "one of the most common life-limiting recessive genetic disorders in Caucasians"
                }},
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "is caused by", 
                    "object": "mutations in the cystic fibrosis transmembrane conductance regulator (CFTR)" 
                }},
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "is a multi-organ disease that involves", 
                    "object": "lungs, pancreas, sweat glands, digestive and reproductive systems and several other tissues" 
                }},
                {{ 
                    "subject": "CFTR", 
                    "link": "is", 
                    "object": "cystic fibrosis transmembrane conductance regulator" 
                }},
                {{ 
                    "subject": "CFTR", 
                    "link": "is affected by", 
                    "object": "mutations in patients with CF" 
                }},
                {{ 
                    "subject": "CFTR mutations", 
                    "link": "lead to", 
                    "object": "dysregulation of several cellular signalling pathways" 
                }},
                {{ 
                    "subject": "Airway epithelial cells", 
                    "link": "contribute to", 
                    "object": "pathogenesis of CF" 
                }},
                {{ 
                    "subject": "Neutrophils", 
                    "link": "contribute to", 
                    "object": "pathogenesis of CF" 
                }},
                {{ 
                    "subject": "Monocytes", 
                    "link": "contribute to", 
                    "object": "pathogenesis of CF" 
                }},
                {{ 
                    "subject": "Macrophages", 
                    "link": "contribute to", 
                    "object": "pathogenesis of CF"
                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "are affected by", 
                    "object": "CFTR mutations in patients with CF" 
                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "play a crucial role in", 
                    "object": "protecting the organs against opportunistic infections and also in the regulation of tissue homeostasis" 
                }},
                {{ 
                    "subject": "Immune cells", 
                    "link": "are involved in", 
                    "object": "regulation of tissue homeostasis" 
                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "are in continuous use by these cells to elicit a proper immune response", 
                    "object": "several signalling pathways" 
                }},
                {{ 
                    "subject": "Several signalling pathways", 
                    "link": "may be dysregulated in", 
                    "object": "cells with CFTR mutations" 
                }}
            ]
            Your answer:
            [
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "is", 
                    "object": "life-limiting recessive genetic disorder in Caucasians"
                }},
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "is caused by", 
                    "object": "mutations in the cystic fibrosis transmembrane conductance regulator (CFTR)" 
                }},
                {{ 
                    "subject": "Cystic fibrosis (CF)", 
                    "link": "involves", 
                    "object": [
                        "lungs", 
                        "pancreas", 
                        "sweat glands", 
                        "digestive system",
                        "reproductive system",
                        "other tissues" 
                    ]
                }},
                {{ 
                    "subject": "CFTR", 
                    "link": "is", 
                    "object": "cystic fibrosis transmembrane conductance regulator" 
                }},
                {{ 
                    "subject": "CFTR", 
                    "link": "is affected by", 
                    "object": "mutations in patients with CF" 
                }},
                {{ 
                    "subject": "CFTR mutations", 
                    "link": "lead to", 
                    "object": "dysregulation of cellular signalling pathways" 
                }},
                {{
                    "subject": [
                        "Airway epithelial cells",
                        "Neutrophils",
                        "Monocytes", 
                        "Macrophages"
                    ],
                    "link": "contribute to", 
                    "object": "pathogenesis of CF" 

                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "are affected by", 
                    "object": "CFTR mutations in patients with CF" 
                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "play a crucial role in", 
                    "object": [
                        "protecting the organs against opportunistic infections",
                        "regulation of tissue homeostasis"
                    ]
                }},
                {{ 
                    "subject": "Innate immune cells", 
                    "link": "are used by cells",
                    "object": "to elicit a proper immune response"
                }},
                {{ 
                    "subject": "Several signalling pathways", 
                    "link": "may be dysregulated in", 
                    "object": "cells with CFTR mutations" 
                }}
            ]

            ### End of examples ###

            Now refactor the following JSON

            Context:
            {triplets}

            Your answer:

        """
    }
]
