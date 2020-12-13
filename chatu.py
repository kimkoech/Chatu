#!/usr/bin/env python

# Program that takes a python file in swahili converts it to english and
# executes it on the python intepretter

import translations as TRANS
import argparse
import os

# command line handler
parser = argparse.ArgumentParser(description='Takes a chatu file and executes it')
parser.add_argument('chatu_script', metavar='.ch', type=str, nargs='+',
                   help='chatu script script')

args = parser.parse_args()
# TODO: handle other inputs from chatu file

# open and parse chatu script
user_chatu_script = [line for line in open(args.chatu_script[0])]

# generate translations
swa_to_eng = TRANS.gen_map("translations.csv")[0]

# apply translations
converted = []
for line in user_chatu_script:
    
    # only alter uncommented lines
    if "#" not in line:
        for swa_key,eng_val in swa_to_eng.items():
            line = line.replace(swa_key, eng_val)
            
    converted.append(line)

# write to compiled file and execute

# name for compiled file
_chatu_file_name = args.chatu_script[0].split("/")
_chatu_file_name.reverse()
chatu_compile_file_name = _chatu_file_name[0] + "c"

f = open(chatu_compile_file_name, "w+")
# header
f.write("#!/usr/bin/env python\n\n")
# script
f.writelines(converted)
f.close

# execute
#print("python " + chatu_compile_file_name)

os.system('python ' + chatu_compile_file_name)
# execute
#execfile(chatu_compile_file_name)