from pathlib import Path
import os
import shutil

def moveFile(source,destination)->str:

  if not os.path.exists(source):
    return f"{source} dosn't exists"

  if not os.path.exists(destination):
    os.mkdir(destination)

  try:
    shutil.move(source,destination)
    return f"{source:10} ---> {destination:>5}"

  except Exception as e:
    return f"An error occured : {e}"


def moveMultiple(*file,destination):

  destPath=Path(destination)
  destPath.mkdir(parents=True,exist_ok=True)

  try:
    for f in file:
      shutil.move(f,destPath/Path(f).name())
      return f"{f:10} ---> {destination:>5}"

  except Exception as e:
    return f"An error occured : {e}"


def main():

  source=input("Enter the name of the source file(s) : ").split()
  destination=input("Enter the name of the destionation file : ")

  if len(source)<2:
    print(moveFile(source,destination))
  else:
    print(moveMultiple(*source,destination))


if __name__=="__main__":
  main()