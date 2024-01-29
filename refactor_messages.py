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

            This example shows the correct way to decrease length of link and object
            without loosing information. So "can be utilized as a method to" can be replaced with just
            "can". All other words can be omitted. 
            Note that in"decrease MDSC levels in vivo" all words are important. You should not omit any of them 
            because otherwise, information will be lost.

            Context:
            {{
                "subject": "Fas-FasL interactions",
                "link": "can be utilized as a method to",
                "object": "decrease MDSC levels in vivo"
            }}
            Your answer:
            {{
                "subject": "Fas-FasL interactions",
                "link": "can",
                "object": "decrease MDSC levels in vivo"
            }}

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

            This example shows the correct way to make parts of triplets shorter.
            So "containing fewer" can be replaced with "with less". And "are typically not considered" can 
            be replaced with "are not".

            Context:
            {{                                                                                                                                                                                     
                "subject": "Short polypeptides", 
                "link": "containing fewer than 20–30 residues"
                "object": "are typically not considered proteins"
            }}
            Your answer:
            {{                                                                                                                                                                                     
                "subject": "Short polypeptides", 
                "link": "with less than 20-30 residues", 
                "object": "are not proteins"
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

            This example shows the correct way to form a list on objects from one long object.
            Object "such as catalysis, DNA replication, response to stimuli, providing structure, and transport" is very long 
            and you must form a list containin 5 objects: ["catalysis", "DNA replication", 
            "response to stimuli", "providing structure", "transport"].
            A list must be placed into square brackets.

            Context:
            {{ 
                "subject": "Proteins", 
                "link": "have various functions", 
                "object": "such as catalysis, DNA replication, response to stimuli, providing structure, and transport"
            }}
            Your answer:
            {{ 
                "subject": "Proteins", 
                "link": "have function of", 
                "object": [
                    "catalysis",
                    "DNA replication",
                    "response to stimuli",
                    "providing structure",
                    "transport"
                ]
            }}
             
            ### Example ###

            This example shows the correct way to form an object if it's not present.
            You can see that "was a significant innovation in the development of the nervous system" has a verb
            that can be a link itself. So the new link is "was a significant innovation in" and the new object is
            "development of nervous system".

            Context:
            {{
                "subject": "Generation of electric signals", 
                "link": "was a significant innovation in the development of the nervous system"
            }}
            Your answer:
            {{
                "subject": "Generation of electric signals", 
                "link": "was a significant innovation in",
                "object": "development of nervous system"
            }}

            ### Example ###

            This example shows the correct way to form 2 new triplets from original 1 triplet.
            The pair:
            {{
                "link": "indicates that the capacity to generate electric signals emerged",
                "object": "during the Tonian period"
            }}
            can form a new triplet:
            {{ 
                "subject": "Capacity to generate electric signals", 
                "link": "emerged", 
                "object": "during the Tonian period" 
            }}

            Context:
            {{ 
                "subject": "Evidence from molecules", 
                "link": "indicates that the capacity to generate electric signals emerged", 
                "object": "during the Tonian period" 
            }}
            Your answer:
            {{ 
                "subject": "Evidence from molecules", 
                "link": "indicates that", 
                "object": "capacity to generate electric signals emerged" 
            }},
            {{ 
                "subject": "Capacity to generate electric signals", 
                "link": "emerged", 
                "object": "during the Tonian period" 
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

            This example shows the correct way to form 2 new triplets from original 1 triplet.
            An object "FasL, which triggers apoptosis in MDSCs" can form a new triplet:
            {{
                "subject": "FasL",
                "link": "triggers",
                "object": "apoptosis in MDSC's"
            }}

            Context:
            {{
                "subject": "Activated T cells",
                "link": "produce",
                "object": "FasL, which triggers apoptosis in MDSCs"
            }}
            Your answer:
            {{
                "subject": "Activated T cells",
                "link": "produce",
                "object": "FasL"
            }},
            {{
                "subject": "FasL",
                "link": "triggers",
                "object": "apoptosis in MDSC's"
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

            ### End of examples ###

            Now refactor the following JSON

            Context:
            {triplets}

            Your answer:

        """
    }
]
