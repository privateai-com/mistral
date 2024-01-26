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

            This example shows the correct way to decrease length of link and object
            without loosing information. So "can be utilized as a method to" can be replaced with just
            "can". All other words can be omitted. But in "decrease MDSC levels in vivo" all words are
            important. So you should not omit any of them because otherwise, information will be lost.

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

            This example shows the correct way of splitting a very long object into separate triplets.
            Object "protein folding, stability, activity, and function" is very long.
            So you have to split it into different triplets. One for "protein folding", one for "protein stability", 
            one for "protein activity", one for "protein function".
            Subject and link in these new triplets stay the same.

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
                "object": "protein folding"
            }},
            {{
                "subject": "Post-translational modifications",
                "link": "affect",
                "object": "protein stability"
            }},
            {{
                "subject": "Post-translational modifications",
                "link": "affect",
                "object": "protein activity"
            }},
            {{
                "subject": "Post-translational modifications",
                "link": "affect",
                "object": "protein function"
            }}

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
            You should notice that the link has a verb that can be a link itself. So:
            "link": "consist of at least one long polypeptide"
            can be replaced with 
            "link": "consist of",
            "subject": "at least one long polypeptide"
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

            This example shows the correct way to split long object into separate triplets.
            Object "such as catalysis, DNA replication, response to stimuli, providing structure, and transport" is very long 
            and must be separated into different triplets. One for "catalysis", one for "DNA replication", one for "responce to stimuli",
            one for "providing structure", one for "transport".
            Subject and link in these new triplets stay the same.

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
                "object": "catalysis"
            }},
            {{ 
                "subject": "Proteins", 
                "link": "have function of", 
                "object": "DNA replication"
            }},
            {{ 
                "subject": "Proteins", 
                "link": "have function of", 
                "object": "response to stimuli"
            }},
            {{ 
                "subject": "Proteins", 
                "link": "have function of", 
                "object": "providing structure"
            }},
            {{ 
                "subject": "Proteins", 
                "link": "have function of", 
                "object": "transport"
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
            The pair of link "indicates that the capacity to generate electric signals emerged" and 
            object "during the Tonian period" can form a new triplet:
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
            A link "was a key innovation in the evolution of the nervous system" can form a new pair of link and object:
            "link": "was a key innovation in"
            "object": "evolution of the nervous system"

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
