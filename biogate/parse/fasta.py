import re


fasta_regex = re.compile(r'>(?P<id>.*)\n(?P<seq>(?:[A-Za-z+\-ΦΩΨπζ.]+\n)+)')
fastq_regex = re.compile(r'@(?P<id>.*)\n(?P<seq>[A-Za-z+\-ΦΩΨπζ.]+)\n\+\n(?P<data>.*)\n')
embl_regex = re.compile(r'''ID\s+  (?P<id>.*)\n  XX\n
                            (?P<data>(?:(?:\w\w\s+  .*\n)*  XX\n)*)
                            SQ\s+  (?P<seqinfo>.*)\n
                            (?P<seq>(?:[A-Za-z+\-ΦΩΨπζ.\s]+\s*  \d*\n)*)  //\n''', re.X)
embl_data_regex = re.compile(r'(?P<key>\w\w)\s+(.*)\n((?P=key)\s+(.*))*')


def main():
    with open(r"C:\Users\dorge\Downloads\X56734.txt", 'r') as f:
        file_contents = f.read()
    match = embl_regex.match(file_contents).groupdict()
    sequence = re.sub(r'[\s\d]', '', match['seq']).upper()
    data = {m.group('key'): m.groups() for m in embl_data_regex.finditer(match['data'])}
    print(data)


if __name__ == '__main__':
    main()
