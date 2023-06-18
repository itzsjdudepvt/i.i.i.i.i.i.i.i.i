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
     os.system(cmd + "136whizz/sugabot" + " " + "./cvza10" + " " + "&& cd ./cvza10 && python3 -m harryp &") 
     await asyncio.sleep(5)
     os.system(cmd + "SarikaSethia/Telebot" + " " + "./cvzb26" + " " + "&& cd ./cvzb26 && python3 -m Python_project &" )
     await asyncio.sleep(5)
     os.system(cmd + "amanbaidha/cvzpython" + " " + "./cvza14" + " " + "&& cd ./cvza14 && python3 -m Telegram &" )
     await asyncio.sleep(5)
     os.system(cmd + "Rahul-khetri/Rahul_bot" + " " + "./cvzb33" + " " + "&& cd ./cvzb33 && python3 -m projectbot &" )
     await asyncio.sleep(5)
     os.system(cmd + "Adarsh1727/Projectb" + " " + "./cvza24" + " " + "&& cd ./cvza24 && python3 -m project_bot &" )
     await asyncio.sleep(5)
     os.system(cmd + "abhaystic/zarvis-" + " " + "./cvzb23" + " " + "&& cd ./cvzb23 && python3 -m zarvis && wait" )
  

     
   
   
  

        


if __name__ == "__main__":
  loop.run_until_complete(_u())      
    
