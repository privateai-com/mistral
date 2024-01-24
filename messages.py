messages = [
    {
        "role": "user", 
        "content": """
        You are a helpful assistant. You must analyze the given context and find all triplets in it.

        If no triplets can be found in the context, say "No triplets". Say only this and nothing else.

        You must output all triplets in a valid JSON format.

        Let's look at some examples:

        ### Example 1 ###
        Context: "Bob went to Walmart to buy cheap clothes."
        Triplets:
        [
            {{   
                "subject": "Bob",
                "link": "went to",
                "object": "walmart"
            }},
            {{
                "subject": "Bob",
                "link": "went to buy",
                "object": "cheap clothes"
            }}
        ]


        ### Example 2 ###
        Context: "The disadvantage of this design is that Nagant revolvers were laborious and time-consuming to reload"
        Triplets:
        [
            {{  
                "subject": "Nagant revolvers",
                "link": "had",
                "object": "hard reloading"
            }}
        ]

        ### Example 3 ###
        Context: "Placebo. To cook chicken. Fast Ferrari. Winter in Norway. George Dunlop."
        Triplets: No triplets

        ### Example 4 ###
        Context: "Soap"
        Triplets: No triplets

        ### Example 5 ###
        Context: "Kendrick Lamar"
        Triplets: No triplets

        ### Example 6 ###
        Context: "Australia has reach wildlife"
        Triplets:
        [
            {{  
                "subject": "Australia",
                "link": "has",
                "object": "rich wildlife"
            }},
        ]

        ### Example 7 ###
        Context: "Alice bought some Ethereum"
        Triplets:
        [
            {{  
                "subject": "Alice",
                "link": "bought",
                "object": "Ethereum"
            }}
        ]

        ### Example 8 ###
        Context: "Vitamin C is known as ascorbic acid. Vitamin C is known as ascorbate."
        Triplets:
        [
            {{  
                "subject": "Vitamin C",
                "link": "is known as",
                "object": "ascorbic acid"
            }}
        ]

        ### End of examples ###

        Context: {context}
        Triplets: 
        """
    }
]
