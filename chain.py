import os

os.environ["TRANSFORMERS_CACHE"] = "/home/ubuntu/big-dir/"

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from text_reader import read_files, write_triplets
from pathlib import Path
from triplet_messages import triplet_messages
from refactor_messages import refactor_messages
import json
import torch
import sys

def create_tokenizer(model_name):
    """
    Creates a tokenizer for the model.

    Args:
        model_name (str): The name of the model
    Returns:
        The tokenizer
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return tokenizer

def create_llm(model_name, tokenizer, _top_k, _top_p, _tempterature):
    """
    Creates a HuggingFace pipeline to be used as LLM.

    Args:
        model_name (str): The name of the model
        tokenizer: The tokenizer for the model
        _top_k (float): 'top_k' parameter of the model
        _top_p (float): 'top_p' parameter of the model
        _tempterature (float): 'temperature' parameter of the model

    Returns:
        HuggingFace pipeline based on the model
    """
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        do_sample=True,
        top_k=_top_k,  # defaults to 50
        top_p=_top_p,  # defaults to 1
        temperature=_tempterature,  # defaults to 1
        device_map="auto",
        torch_dtype=torch.float16,
    )
    pipe = pipeline(
        "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=1024
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    return llm


def create_chain(messages, llm, tokenizer):
    """
    Creates a chain from a prompt and a LLM.

    Args:
        messages (list): List of JSON objects with 'role' and 'content' fields
                         The messages form the prompt for LLM.
                         There are 2 kinds of messages:
                            - For triplet extraction
                            - For triplet refactoring
        llm: The LLM to be used in the chain
        tokenizer: The tokenizer for the LLM
    Returns:
        Chain of prompt and LLM
    """

    # Tokenize previous messages
    prompt_tokens = tokenizer.apply_chat_template(messages, return_tensors="pt")
    # Turn tokens into list of strings
    prompt_text_parts = tokenizer.batch_decode(prompt_tokens)
    # Place all strings into one
    prompt_text = ""
    for part in prompt_text_parts:
        prompt_text += part
    # Form a prompt from that string
    prompt = PromptTemplate.from_template(prompt_text)
    chain = prompt | llm

    return chain

def extract_triplets(chain, file):
    """
    Invokes a chain to extract triplets from the file text.

    Args:
        chain: Chain to be used for triplet extraction
        file (str): Text to extract triplets from
    Returns:
        Long string with all triplets from the text
    """
    print("Extracting triplets...")
    raw_triplets = chain.invoke({"context": file})
    # TODO:
    print("\n\nRAW RES IS")
    print(raw_triplets)
    return raw_triplets

def refactor_triplets(chain, raw_triplets):
    """
    Invokes a chain to reformat extracted triplets.

    Args:
        chain: Chain to be used for triplet refactoring
        raw_triplets (str): Previously extracted triplets
    Returns:
        Long string with all refactored triplets
    """
    print("Refactoring triplets...")
    ref_triplets = chain.invoke({"triplets": raw_triplets})
    # TODO:
    print("\nREFACTOR IS")
    print(ref_triplets)
    return ref_triplets
