lib = ['Á', 'á', 'Ä', 'ä', 'Ã', 'ã', 'Č', 'č', 'Ď', 'ď', 'Ě', 'ě', 'Í', 'í',
       'Ň', 'ň', 'Ó', 'ó', 'Ò', 'ò', 'Ö', 'ö', 'Õ', 'õ', 'Ř', 'ř', 'Š', 'š',
       'Ť', 'ť', 'Ú', 'ú', 'Ů', 'ů', 'Ý', 'ý', 'Ž', 'ž']

def create_not_french_dictionary(input_file):
    with open(input_file) as f:
        line_count = 0
        container = {}

        for line in f:
            line_count += 1
            not_french, french_percent = check_if_not_french(line)
            if french_percent == 0:
                pass
            else:
                if french_percent in container.keys():
                    container[french_percent].append((not_french, line_count))
                else:
                    container[french_percent] = []
                    container[french_percent].append((not_french, line_count))
    return container

def check_if_not_french(line):
    processed_line = line.strip().split()
    not_french = []
    for i in processed_line:
        for alphabet in lib:
            if alphabet in i:
                not_french.append(i)
                break
    if len(processed_line) > 0:
        french_percent = round(len(not_french)*100 / len(processed_line))
    else:
        french_percent = 0
    return (not_french, french_percent)

def write_result_to_file(container, output_file):
    descending = sorted(container.keys(), reverse=True)
    with open(output_file, 'w') as r:
        for i in descending:
            for checked_line in container[i]:
                r.write('Found suspected non-French words: {0} in line {1}, about {2} % of total words in line.'
                        .format(checked_line[0], checked_line[1], i))
                r.write('\n')

def main():
    import sys
    input_file = sys.argv[1]
    try:
        output_file = sys.argv[2]
    except IndexError:
        raise IndexError('Please write the output file name')

    inp = create_not_french_dictionary(input_file)
    write_result_to_file(inp, output_file)

if __name__ == "__main__":
    main()
