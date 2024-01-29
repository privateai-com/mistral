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

            Make sure each part of the triplet is as short as possible. The optimal 
            length of each part is up to 5 words. For example:
            "link": "could be exploited as a strategy to"
            should be replaced with
            "link": "is used to"
            Both options must have the same meaning, but the second one is much shorter.

            Let's look at some examples:

            ### Example ###

            If you see "No triplets" message, just say "No triplets".

            Context: No triplets.
            Your answer: No triplets.

            ### Example ###

            If you see "No triplets" message, just say "No triplets".

            Context: No triplets.
            Your answer: No triplets.

            ### Example ###

            This example shows the correct way to split very long object and subject into lists.
            Object "presence of excessive growth factors, cytokines, or inflammatory molecules" is very long.
            So you have form a list containing 3 objects: ["excessive growth factors", "cytokines", "inflammatory molecules"].
            Always place lists in square brackets.

            Subject "Presence of excessive growth factors, cytokines, or inflammatory molecules" is very long.
            So you have to form a list containing 3 subjects: ["excessive growth factors", "cytokines", "inflammatory molecules"]
            Always place lists in square brackets.

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

            This example shows the correct way of converting a long object into a list.
            Object "protein folding, stability, activity, and function" is very long.
            So you have to form a list containing 4 objects: ["protein folding", "protein stability",
            "protein activity", "protein function"].
            A list must be placed into square brackets.

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
            }},


            ### Example ###

            This example shows the correct way to form a list of subjects from one long subject.
            Subject "Recent approval of several RNA drugs and COVID-19 mRNA vaccines" is too long.
            You must form a list containing 2 subjects: ["RNA drugs", "COVID-19 mRNA vaccines"].
            A list must be placed in square brackets.

            Context:
            {{
                "subject": "Recent approval of several RNA drugs and COVID-19 mRNA vaccines",
                "link": "suggests that this milestone is being realized"
            }}
            Your answer:
            {{
                "subject": [
                    "Approval of RNA drugs",
                    "Approval of COVID-19 mRNA vaccines"
                ],
                "link": "suggests that this milestone is being realized"
            }}

            ### Example ###

            This example shows the correct way of forming a subject from a link.
            You should notice that the link has a verb that can be a link itself. 
            Link "consist of at least one long polypeptide" can be replaced with 
            {{
                "link": "consist of",
                "subject": "at least one long polypeptide"
            }}
            Also notice that in "at least one long polypeptide" all words are important. You should not
            omit any important words.

            Context:
            {{ 
                "subject": "Proteins", 
                "link": "consist of at least one long polypeptide"
            }}
            Your answer:
            {{ 
                "subject": "Proteins", 
                "link": "consist of",
                "subject": "at least one long polypeptide"
            }}
             

            ### Example ###

            This example shows the correct way to form an object from a link if object is not present.
            Link: "was a key innovation in the evolution of the nervous system" can form a new pair of link and object:
            {{
            "link": "was a key innovation in",
            "object": "evolution of the nervous system"
            }}

            Context:
            {{
                "subject": "Ability to generate electric signals", 
                "link": "was a key innovation in the evolution of the nervous system"
            }}
            Your answer:
            {{
                "subject": "Ability to generate electric signals", 
                "link": "was a key innovation in"
                "object": "evolution of the nervous system"
            }}

            ### Example ###

            This example shows correction of a link. In most cases the link contains a verb. So 
            "mediate" should be a link instead of "expressing FasL".

            Context:
            {{
                "subject": "Activated T cells",
                "link": "expressing FasL",
                "object": "mediate apoptosis of MDSCs in vivo"
            }}
            Your answer:
            {{
                "subject": "Activated T cells",
                "link": "mediate",
                "object": "apoptosis of MDSCs in vivo"
            }}


            ### End of examples ###

            Now refactor the following JSON

            Context:
            {triplets}

            Your answer:

        """
    }
]
