import argparse
import sys
import os
import display

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n')
        self.print_help()
        sys.exit(2)


class Config():
    def __init__(self):
        self.current_path = os.getcwd()
        self.ext = '.*\..*'

    def set_path(self, path=''):
        if path != '':
            self.current_path = path

    def set_mode(self, mode):
        self.mode = mode

    def set_ext(self, ext=''):
        if ext != '':
            self.ext = '.*\\' + ext


my_parser = MyParser(prog='Bulk File Rename',
                     description='This app enables you to bulk rename '
                                 'the files.')
my_parser.add_argument('-path', action='store',
                       help='Your directory full path, if skipped, '
                            'will use currect directory')
my_group = my_parser.add_mutually_exclusive_group(required=True)
my_group.add_argument('-lowercase', action='store_true',
                      help='This option will change files casing to lowercase')
my_group.add_argument('-uppercase', action='store_true',
                      help='This option will change files casing to uppercase')
my_group.add_argument('-convention', action='store',
                      help='This option will apply specific convention to'
                           'files eg. "File000" will name files in'
                           'the following manner: File001, File002... '
                           'Please note that the 000 will be used as starting'
                           'point and it can be used wherever in the name.')
my_parser.add_argument('-ext', action='store',
                       help='This option will narrow group of files,'
                            'to those matching convention. For convention,'
                            'use extension eg. ".txt", ".xlsx"')

args = my_parser.parse_args()

cnfg = Config()
if args.path:
    cnfg.set_path(args.path)
if args.lowercase:
    cnfg.set_mode('lower')
if args.uppercase:
    cnfg.set_mode('upper')
if args.convention:
    cnfg.set_mode(args.convention)
if args.ext:
    cnfg.set_ext(args.ext)

rename = display.Printer(cnfg.current_path, cnfg.mode, cnfg.ext)
rename.print_proposition()

option = input('\nDo you want to proceed with the change? (Y|N) ')

if option == 'Y':
    rename.change()
else:
    sys.exit(2)