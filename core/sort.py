import os
import shutil


def sort_files_by_extension(source_dir=None):

  typeOfFiles = {
              "PDFs": [".pdf"],
              'Images':[".jpg",".jpeg",".png"],
              'Documents':[".docs",".docx",".txt"],
              'Audio':[".mp3",".wav"],
              'Videos':[".mp4",".mkv",".flac"],
              'Exec':[".exe",".msi",".bat",".sh"],
              'Zip':[".rar",".zip",".tar",".gz",".7z"],
              'torrent':[".torrent"],
              'Others':[]
              }

  if source_dir is None:
    source_dir = os.path.join(os.path.expanduser("~"), 'Downloads')

  for key in typeOfFiles.keys():
      dest_dir = os.path.join(source_dir, key)
      if not os.path.exists(dest_dir):
          os.makedirs(dest_dir)

  for filename in os.listdir(source_dir):

      file_path = os.path.join(source_dir, filename)

      if os.path.isfile(file_path):
          ext = os.path.splitext(filename)[1].lower()
          extension_dir = next((f for f in typeOfFiles if ext in typeOfFiles[f]), 'Others')
          dest_folder = os.path.join(source_dir, extension_dir)

          if not os.path.exists(dest_folder):
              os.makedirs(dest_folder)

          shutil.move(file_path, os.path.join(dest_folder, filename))

  return "Files sorted successfully."

if __name__=="__main__":
  sort_files_by_extension()