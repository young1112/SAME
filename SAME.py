��  import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("SAME").keyx()
       __import__("SAME").login()
   except Exception as a:
       exit(str(a))
