import os
import subprocess

def get_server():
  a=os.environ.get("cvzhost", "")
  return a 


cmd = "git clone https://github.com/"
def _u():
  if get_server() == "a1":
    os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25")
    os.system(cmd + "sunilsaini0/codingbot" + " " + "./cvzb08")  
    os.system(cmd + "rizaul0/Myaibot_tg" + " " + "./cvzb28") 
    os.system(cmd + "rahul-jerthi/tgbot" + " " + "./cvza22")
    os.system(cmd + "shubhra2005/Shubh" + " " + "./cvza09")      
    p1 = subprocess.Popen(["python", "./cvza25/project_bot/__main__.py"]) 
    p1.wait()    
  

        


if __name__ == "__main__":
  _u()      
    
