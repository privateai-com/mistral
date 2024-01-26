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
