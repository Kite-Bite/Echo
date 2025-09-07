from pathlib import Path
import os
import shutil

def copyFile(source,destination):
  if not os.path.exists(source):
      return f"{source} dosn't exists"

  if not os.path.exists(destination):
    os.mkdir(destination)

  try:
      if os.path.isdir(source):
        shutil.copytree(source,destination,dirs_exist_ok=True)
      else:
        shutil.copy2(source,destination)

      return f"{source} ---> {destination}"

  except Exception as e:
     return f"Error occured while transferring : {e}"

def copyMultiple(*file,destination):

  destPath=Path(destination)
  destPath.mkdir(parents=True,exist_ok=True)

  try:
    for f in file:
      shutil.copy2(f,destPath/Path(f).name())
      return f"{f:10} ---> {destination:>5}"

  except Exception as e:
    return f"An error occured : {e}"


def main():

  source=input("Enter the name of the source file(s) : ").split()
  destination=input("Enter the name of the destionation file : ")

  if len(source<2):
      print(copyFile(source,destination))
  else:
      print(copyMultiple(source,destination))


if __name__=="__main__":
   main()