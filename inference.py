import os
os.system('python tools/test.py configs/nucleus_model.py final_checkpoint.pth --format-only --options "jsonfile_prefix=./answer"')