import sys


def base_to_decimal(digits, base):
    num = 0
    for digit in digits:
        num = base * num + int(digit)
    return num


def decimal_to_base(num, base):
    digits = ''
    while num > 0:
        digits = str(num % base) + digits
        num  = num // base
    return digits


def show_help():
    print()
    print('This program converts numbers in a file between any two bases')
    print('It will also display the corresponding unicode text for the numbers if the \'--ascii\' flag is given')
    print()
    print('Usage:')
    print('\tpython base_decoder.py [options]')
    print()
    print('Options:')
    print('--file=<path> - required, path to file containg numbers as text. Multiple numbers should either be seperated by a whitespace or by new lines')
    print('--base=<base> - required, the base in which the numbers in the file are given')
    print('--convertingBase=<base> - required, the base in which the numbers will be converted to')
    print('--outputFile=<path> - optional argument, file where the converted numbers and/or ascii text will be written')
    print('--unicode - optional argument; if flag is present, unicode characters of the corresponding digits will also be displayed')


def main():
    infile_path = ''
    outfile_path = ''
    original_base = ''
    converting_base = ''
    convert_unicode = False
    original_numbers = []
    converted_numbers = []
    unicode_text = ''

    for argument in sys.argv:
        if argument.startswith('--file='):
            infile_path = argument[len('--file='):]
        if argument.startswith('--outputFile='):
            outfile_path = argument[len('--outputFile='):]
        if argument.startswith('--base='):
            original_base = int(argument[len('--base='):])
        if argument.startswith('--convertingBase='):
            converting_base = int(argument[len('--convertingBase='):])
        if argument.startswith('--unicode'):
            convert_unicode = True

    if infile_path == '' or original_base == '' or converting_base == '':
        print('Error: Missing one or more required arguments.')
    else:
        try:
            with open(infile_path) as f:
                original_numbers = f.read().split()
        except FileNotFoundError as e:
            print('Could not find file:', infile_path)
    
        for number in original_numbers:
            dec = base_to_decimal(number, original_base)
            new_num = decimal_to_base(dec, converting_base)
            if convert_unicode:
                unicode_text += chr(dec)
            converted_numbers.append(new_num)

        print(converted_numbers)
        if convert_unicode:
            print(unicode_text)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        show_help()
    else:
        main()
