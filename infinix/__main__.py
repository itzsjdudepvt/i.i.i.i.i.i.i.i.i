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
    await asyncio.sleep(5)
    os.system(cmd + "sunilsaini0/codingbot" + " " + "./cvzb08"  + " " + "&& cd ./cvzb08 && python3 -m coding &" )
    await asyncio.sleep(5)
    os.system(cmd + "Nehaa1727/Codybot" + " " + "./cvza05"  + " " + "&& cd ./cvza05 && python3 -m cody &" )
    await asyncio.sleep(5)
    os.system(cmd + "rizaul0/Myaibot_tg" + " " + "./cvzb28"  + " " + "&& cd ./cvzb28 && python3 -m infinix &" ) 
    await asyncio.sleep(5)
    os.system(cmd + "shubhra2005/Shubh" + " " + "./cvza09"  + " " + "&& cd ./cvza09 && python3 -m cupid &")
    await asyncio.sleep(5)
    os.system(cmd + "rahul-jerthi/tgbot" + " " + "./cvza22" + " " + "&& cd ./cvza22 && python3 -m project_bot && wait")
    
  if get_server() == "a2":  
     os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &") 
     os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &" )
     os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &" )
     os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &" )
     os.system(cmd + "Anantpreet512/my_bot" + " " + "./cvza25" + " " + "&& cd ./cvza25 && python3 -m INFINITY &" )
     
   
   
  

        


if __name__ == "__main__":
  loop.run_until_complete(_u())      
    
