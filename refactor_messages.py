refactor_messages = [
    {
        "role": "user", 
        "content": """
            You are a helpful assistant. You must analyze the given context and refactor it.
            The context is in JSON format.

            If you see a "No triplets" string, just say "No triplets".

            Each JSON string a triplet. Each triplet has 3 parts: subject, link, object.
            Triplet is surrounded by curly braces like so:
            {{
                "subject": "some subject",
                "link": "some link",
                "object": "some object",
            }}

            For each triplet:
            - Make sure it's a valid JSON. It must contain correct number of curly braces, commas, quotes, colons
            - Make sure it has all 3 parts: subject, link, object. If no object is present, add it.

            For each part of the triplet:
            - Rephrase it to be as simple to understand as possible
            - Make it as short as possible
            - Get rid of synonyms
            - Divide it into several triplets if possible

            Let's look at some examples:

            ### Example ###
            Context: No triplets.
            Your answer: No triplets.

            ### Example ###
            Context: No triplets.
            Your answer: No triplets.

            ### Example ###
            Old version:
            [
                {{
                    "subject": "Fas-FasL interactions",
                    "link": "can be utilized as a method to",
                    "object": "decrease MDSC levels in vivo"
                }}
            ]
            Your answer:
            [
                {{
                    "subject": "Fas-FasL interactions",
                    "link": "can",
                    "object": "decrease MDSC levels"
                }}
            ]

            ### Example ###
            Old version:
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
                    "object": "presence of excessive growth factors."
                }},
                {{
                    "subject": "Various mechanisms",
                    "link": "include",
                    "object": "presence of cytokines, or inflammatory molecules"
                }},
                {{
                    "subject": "Various mechanisms",
                    "link": "include",
                    "object": "presence of inflammatory molecules"
                }},
                {{
                    "subject": "Presence of excessive growth",
                    "link": "provide",
                    "object": "continuous survival signals"
                }},
                {{
                    "subject": "Presence of cytokines",
                    "link": "provide",
                    "object": "continuous survival signals"
                }},
                {{
                    "subject": "Presence of inflammatory molecules",
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
             
            ### End of examples ###

            Now refactor the following JSON

            Old version:
            {triplets}

            Your answer:

        """
    }
]
