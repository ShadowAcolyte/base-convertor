import sys


def base_to_decimal(digits, base):
    num = 0
    digits = digits.upper()
    for digit in digits:
        x = digit
        if x not in '0123456789':
            x = ord(x) - 65 + 10
        num = base * num + int(x)
    return num


def decimal_to_base(num, base):
    digits = ''
    while num > 0:
        rem = num % base
        if rem > 9:
            rem = chr(rem - 10 + 65)
        digits = str(rem) + digits
        num  = num // base
    return digits


def show_help():
    print()
    print('A utility script to convert numbers in a file between any two bases')
    print('It will also display the corresponding unicode text for the numbers if the \'--ascii\' flag is given')
    print()
    print('Usage:')
    print('\tpython base_decoder.py [options]')
    print()
    print('Options:')
    print('-h or --help - display this help message')
    print('--file=<path> - required, path to file containg numbers as text')
    print('\tmultiple numbers should either be seperated by a whitespace or by new lines')
    print('\tnote : end file path with proper extension (.txt, etc)')
    print('--base=<base> - required, the base of original numbers')
    print('--convert=<base> - required, the base to convert to')
    print('--outfile=<path> - optional argument, file where the converted numbers and/or ascii text will be written')
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

    # get all arguments and initialize variables
    for argument in sys.argv:
        if argument.startswith('--file='):
            infile_path = argument[len('--file='):]
        if argument.startswith('--outfile='):
            outfile_path = argument[len('--outfile='):]
        if argument.startswith('--base='):
            original_base = int(argument[len('--base='):])
        if argument.startswith('--convert='):
            converting_base = int(argument[len('--convert='):])
        if argument.startswith('--unicode'):
            convert_unicode = True

    # check if any arguments are missing
    if infile_path == '' or original_base == '' or converting_base == '':
        print('Error: Missing one or more required arguments.')
        exit();
    
    # open/read file, also check if file exists
    try:
        with open(infile_path) as f:
            original_numbers = f.read().split()
    except FileNotFoundError as e:
        print('Could not find file : ', infile_path)
        exit();
    
    # convert numbers
    for number in original_numbers:
        dec = base_to_decimal(number, original_base)
        new_num = decimal_to_base(dec, converting_base)
        if convert_unicode:
            unicode_text += chr(dec)
        converted_numbers.append(new_num)

    # print in terminal if no output file is specified
    if outfile_path == '' :
        print(converted_numbers)
        if convert_unicode:
            print(unicode_text)
    else:
        try:
            with open(outfile_path, 'a') as f:
                for i in range(0, len(converted_numbers)):
                    f.write(converted_numbers[i] + '\n')
                if convert_unicode:
                    f.write(unicode_text)
        except FileNotFoundError as e:
            with open(outfile_path, 'x'):
                for i in range(0, len(converted_numbers)):
                    f.write(converted_numbers[i] + '\n')
                if convert_unicode:
                    f.write(unicode_text)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        show_help()
    else:
        main()
