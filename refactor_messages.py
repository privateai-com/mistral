refactor_messages = [
    {
        "role": "user", 
        "content": """
            You are a computer program. You must analyze the given JSON object and refactor it.

            ### Example ###

            Context: No triplets.
            Your answer: No triplets.

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
                "object": "presence of excessive growth factors."
            }},
            {{
                "subject": "Various mechanisms",
                "link": "include",
                "object": "presence of cytokines"
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

            ### Example ###

            Context:
            {{
                "subject": "Recent approval of several RNA drugs and COVID-19 mRNA vaccines",
                "link": "suggests that this milestone is being realized"
            }}
            Your answer:
            {{
                "subject": "Recent approval of several RNA drugs",
                "link": "suggests that",
                "object": "this milestone is being realized"
            }},
            {{
                "subject": "Recent approval of several COVID-19 mRNA vaccines",
                "link": "suggests that",
                "object": "this milestone is being realized"
            }}

            ### End of examples ###

            Now refactor the following JSON

            Context:
            {triplets}

            Your answer:

        """
    }
]
