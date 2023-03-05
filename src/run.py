import argparse

from main import summarize_file


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, required=True, help='Path to the pdf file')
args = parser.parse_args()


def run():
    result = summarize_file(args.file)
    text = result['choices'][0]['message']['content']
    print(text)


if __name__ == '__main__':
    run()
