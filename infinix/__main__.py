import glob 
from pathlib import Path 
from infinix.utils import load_plug
import logging 
from logging import getLogger
import asyncio
from . import bot,bot1,bot2,bot3,bot4,bot5
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

log=logging.getLogger("main")
path= "infinix/plugins/*.py"
files=glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plug_name = pxt.stem
    load_plug(plug_name.replace(".py", ""))  
      
try:    
  bot1.start()
  log.info("c1 Started")      
except Exception as e:
  log.info(str(e))
try:    
  bot2.start()
  log.info("c2 Started")
except Exception as e:
  log.info(str(e))
try:    
  bot3.start()
  log.info("c3 Started")
except Exception as e:
  log.info(str(e))
try:    
  bot4.start()
  log.info("c4 Started")
except Exception as e:
  log.info(str(e)) 
try:    
  bot5.start()
  log.info("c5 Started")
except Exception as e:
  log.info(str(e))
    
    
print("ClBot_started")

if __name__ == "__main__":
  bot1.run_until_disconnected()
  bot2.run_until_disconnected()
  
  bot3.run_until_disconnected()
  bot4.run_until_disconnected()

  bot.run_until_disconnected()
    
