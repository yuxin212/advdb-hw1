import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Input file and output file')
parser.add_argument('-i', '--input', help='Input file name')
parser.add_argument('-o', '--output', help='Output file name')

def count(l, x):
    c = 0
    for i in l:
        if (i == x):
            c += 1
    return c

if __name__ == '__main__':

    args = parser.parse_args()

    input_f = args.input
    output_f = args.output

    with open(input_f, 'r') as f:
        text = f.read();

    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace("' ", ' ')
    text = text.replace('--', ' ')
    text = text.replace('- ', ' ')
    text = text.replace("'s ", ' ')
    text = text.replace("ly ", ' ')
    text = text.replace('ed ', ' ')
    text = text.replace('ing ', ' ')
    text = text.replace('ness ', ' ')
    text = text.replace(') ', ' ')
    text = text.replace('_ ', ' ')
    text = text.replace('; ', ' ')
    text = text.replace('? ', ' ')
    text = text.replace(', ', ' ')
    text = text.replace('! ', ' ')
    text = text.replace(': ', ' ')
    text = text.replace(' "', ' ')
    text = text.replace(" '", ' ')
    text = text.replace(' (', ' ')
    text = text.replace(' _', ' ')

    word_list = text.split()
    word_pair_list = []

    for i in range(1, len(word_list)):
        word_pair = {word_list[i - 1], word_list[i]}
        word_pair_list.append(word_pair)

    non_repeat = []

    for i in word_pair_list:
        if i not in non_repeat:
            non_repeat.append(i)

    df = pd.DataFrame(columns=['Word', 'Count'])

    for w in non_repeat:
        i = count(word_list, w)
        df = df.append({'Word': w, 'Count': i}, ignore_index=True)
        print('Progress {}/{}'.format(df.shape[0], len(non_repeat)))

    df.sort_values(by=['Count'], ascending=False)

    df.to_csv(output_f)
