import os
import json
import shutil
from subprocess import PIPE, run
import sys #access to command line arguments

def find_all_game_dirs(source):
    pass

def main(source,target):
    cwd = os.getcwd() #current working directory
    source_path = os.path.join(cwd,source)
    target_path = os.path.join(cwd,target)
    

if __name__ == "__main__":
    args  = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only")
    source, target = args[1:] #store the second and third argument in the variables
    main(source,target)
