refactor_messages = [
    {
        "role": "user", 
        "content": """
            You are a computer program. You must analyze the given JSON object and refactor it.

            ### Example ###

            If you see "No triplets" message, just say "No triplets".

            Context: No triplets.
            Your answer: No triplets.

            ### Example ###

            If you see "No triplets" message, just say "No triplets".

            Context: No triplets.
            Your answer: No triplets.


            ### Example ###

            This example shows the correct way to split very long object and subject into separate triplets.
            Object "presence of excessive growth factors, cytokines, or inflammatory molecules" is very long.
            So you have to split it into different triplets. One for "growth factors", one for "cytokines", one for "inflammatory molecules".
            Subject and link in all these new triplets are the same.

            Subject "Presence of excessive growth factors, cytokines, or inflammatory molecules" is very long.
            So you have to split it into different triplets. One for "growth factors", one for "cytokines", one for "inflammatory molecules".
            Object and link in all these new triplets are the same.

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

            This example shows the correct way to form 2 triplets from 1 original.
            In subject of original triplet you can see 2 objects (RNA drugs, COVID-19 mRNA vaccines) that
            can act as subjects in new triplets.
            Link and object in these new triplets stay the same.

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
