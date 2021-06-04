__author__ = "Shubham Srivatava / DecodingCausality"

import subprocess
import os

file_name_list = []


code_path_1 = ''
code_path_2 = ''


for root, dirs, files in os.walk(code_path_2):
    for filename in files:
        file_name_list.append(filename)



for file_name in file_name_list :
    print(f'***************************************Comparing file {file_name}')
    command_2 = f'diff -y -w -d --color {code_path_1}/{file_name} {code_path_2}/{file_name} >> diff_report.txt'
    command_3 = f'diff -y -w -d --color {code_path_1}/{file_name} {code_path_2}/{file_name}'
    command_5 = f"diff -y -w -d --color {code_path_1}/{file_name} {code_path_2}/{file_name} grep '>' wc -l"
    command_4 = f'echo {file_name} >> diff_report.text'

    out_2 = subprocess.run(command_2, shell=True)
    out_3 = subprocess.run(command_3, shell=True)
    out_4 = subprocess.run(command_4, shell=True)



