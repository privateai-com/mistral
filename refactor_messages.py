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
            Make sure each triplet is a valid JSON. If it's not, reformat it to be a valid JSON.
            Each triplet must contain exactly 3 parts: subject, link, object. This is the most important requirement!
            So if object is not present, you must create it from the link. For example:
            {{
                "subject": "People of Uganda",
                "link": "demand their freedom"
                <no object here>
            }}
            should be replaced with
            {{
                "subject": "People of Uganda",
                "link": "demand",
                "object": "their freedom"
            }}

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
            Your answer:
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

            ### Example ###

            Context:
            {{
                "subject": "Post-translational modifications",
                "link": "affect",
                "object": "protein folding, stability, activity, and function"
            }}
            Your answer:
            {{
                "subject": "Post-translational modifications",
                "link": "affect",
                "object": [
                    "protein folding",
                    "protein stability",
                    "protein activity",
                    "protein function"
                ]
            }}

            ### End of examples ###

            Now refactor the following JSON

            Context:
            {triplets}

            Your answer:

        """
    }
]
