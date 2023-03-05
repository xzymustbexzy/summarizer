# summarizer
Summarize the content of PDF with power of GPT


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

## About
Summarizer is an open-source document summarization tool powered by GPT. With this tool, you can input any document, including PDF file, image, Word, Excel, HTML, and other type of files with any length. The program will automatically generate a concise summary of its contents. With the power of GPT, this tool is designed to make document summarization fast, accurate, and accessible to everyone. 

## Install
Download the github repo
```shell
git clone https://github.com/xzymustbexzy/summarizer.git
```

Install the required dependencies
```shell
pip install -r requirements.txt
```

## Usage
Set your openai key
```shell
export OPENAI_API_KEY=xxxxxxxxxxxx
```
Run the script
```shell
cd src
python run.py --file example.pdf
```

## Todo
- [] multiple pages support
- [] extremely long content support
- [] Multi-language support
- [] url input
- [] multi-modal support(image)
- [] multiple file types support(Word, Excel, image, html etc.)
- [] more generation controllability
