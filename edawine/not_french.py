import sys

lib = ['Á', 'á', 'Č', 'č', 'Ď', 'ď', 'Ě', 'ě', 'Í', 'í', 'Ň', 'ň', 'Ó', 'ó',
       'Ř', 'ř', 'Š', 'š', 'Ť', 'ť', 'Ú', 'ú', 'Ů', 'ů', 'Ý', 'ý', 'Ž', 'ž']

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        line_count = 0
        for line in f:
            line_count += 1
            for i in lib:
                if i in line:
                    print('Found not French alphabet:', i, 'in line',
                          line_count,', in sentence:', line)
                    break

if __name__ == "__main__":
    main()
