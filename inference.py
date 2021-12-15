import os
interpreter = 'python'
args = 'tools/test.py configs/nucleus_model.py final_checkpoint.pth'
keyword_args = '--format-only --options "jsonfile_prefix=./answer"'
command = f'{interpreter} {args} {keyword_args}'
os.system(command)
