from datetime import datetime

def log_error(errors="ERROR"):

  time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  with open("Errors.log","a") as f:
    f.write(errors+ "\t" + time +"\n")

  return

if __name__ == "__main__":
  log_error()
