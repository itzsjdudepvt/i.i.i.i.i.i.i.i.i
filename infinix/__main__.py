import os
import subprocess
import asyncio

def get_server():
  a=os.environ.get("cvzhost", "")
  return a 
loop = asyncio.get_event_loop()

cmd = "git clone https://github.com/"
async def _u():
  if get_server() == "a1":
    os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25")
    os.system(cmd + "sunilsaini0/codingbot" + " " + "./cvzb08")  
    os.system(cmd + "rizaul0/Myaibot_tg" + " " + "./cvzb28") 
    os.system(cmd + "rahul-jerthi/tgbot" + " " + "./cvza22" + " " + "&& cd tgbot && python -m project_bot")
    os.system(cmd + "shubhra2005/Shubh" + " " + "./cvza09")      
     
  

        


if __name__ == "__main__":
  loop.run_until_complete(_u())      
    
