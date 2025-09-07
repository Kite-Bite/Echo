from datetime import datetime

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main(errors):

  with open("Errors.log","a") as f:
    f.write(errors+ "\t" + time +"\n")

  return

if __name__ == "__main__":
  main()

