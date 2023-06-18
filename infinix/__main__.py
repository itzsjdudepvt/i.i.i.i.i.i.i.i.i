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
    os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &" )
    
    os.system(cmd + "sunilsaini0/codingbot" + " " + "./cvzb08"  + " " + "&& cd ./cvzb08 && python3 -m coding &" )
     
    os.system(cmd + "rizaul0/Myaibot_tg" + " " + "./cvzb28"  + " " + "&& cd ./cvzb28 && python3 -m infinix &" ) 
   
    os.system(cmd + "rahul-jerthi/tgbot" + " " + "./cvza22" + " " + "&& cd ./cvza22 && python3 -m project_bot &")
    os.system("wait")
    # os.system(cmd + "shubhra2005/Shubh" + " " + "./cvza09")
  
   
   
  

        


if __name__ == "__main__":
  loop.run_until_complete(_u())      
    
