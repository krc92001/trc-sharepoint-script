import sys
import os
import re
#takes in directory as argument

def create_file_list(directory):
  """Grabs list of files from the specified directory 
     finds the files containing illegal names"""

  # match string for illegal one drive char
  illegal_chars = r'["*:<>?/\|]+'
  # set if you want to pause between each file to make sure it runs error free!
  slow_input  = False 
  

  unfiltered_list = os.listdir(directory)
  filtered_list = [] # initial list
  
  #filters list for files containing illegal charts
  for file in unfiltered_list:

    if re.match(illegal_chars, file):
      print(f"filename {file} contains illegal characters")
      filtered_list.append(file)
    else :
      print(f"filename: {file} is acceptable")
    if slow_input :
      input("Press any key to continue")
  return filtered_list

def rename_files(list_of_files):
  """
  Renames a list of files by replacing illegal chracters
  set debug true for confirmation on each file
  """
  debug = True # set false for no confirmation

  illegal_chars = ["\"","*",":","<",">","?","/","\\","|","]","+"]
  #dicitonary for replacement can be modified to different chars
  illegal_dict = {
  "\"": "",
  "*": "x",
  ":": "_by_", # essentially for aspect ratios, this is the main concern << 'photo 3_by_9'
  "<": "_",
  ">": "_",
  "?": "_",
  "/": "-",
  "\\": "-",
  "|": "-",
  "]": "x",
  "+": "x"
}
  
  for file_name in list_of_files:
    # iterate through list of files with illegal names
    for char in illegal_chars:
      if char in file_name:
        old_fname = file_name
        file_name = file_name.replace(char, illegal_dict["char"])
        print(f'File: {old_fname} is going to be renamed to: {file_name}')
        error_check = input("Enter y to accept the changes").lower()
        if(error_check  ==  'y' and debug):
          #renames if user specifies error check
          os.rename(sys.argv[1]+"\\"+old_fname,sys.argv[1]+"\\"+file_name)
          print(f"Success...File {file_name}  has been  created")
        else:
          print("Filename change not accepted, moving to next file...")

  
def main():

  list_of_files = create_file_list(sys.argv[1])
  rename_files(list_of_files)

if __name__ == "__main__":
    main()
  






