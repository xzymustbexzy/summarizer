import os
import argparse
import json

from pypdf import PdfReader
import openai

API_KYE = os.environ['OPENAI_API_KEY']
openai.api_key = API_KYE


def summarize_file(path):
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    messages=[
        {
            'role': 'system', 
            'content': 'You are a helpful assistant, help user to summarize the content of the text. Note that you do not need to say hello or ok in your answer, just output a summary of the text directly.'
        },
        {
            'role': 'user', 
            'content': "Summarize the following text:\n"
        },
    ]
    messages[-1]['content'] += text

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )

    return response

