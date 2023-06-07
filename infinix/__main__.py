import glob 
from pathlib import Path 
from infinix.utils import load_plug
import logging 
from logging import getLogger
import asyncio
from . import bot,bot1,bot2,bot3,bot4,bot5
pikalog = getLogger(__name__)
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

  
path= "infinix/plugins/*.py"
files=glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plug_name = pxt.stem
    load_plug(plug_name.replace(".py", ""))  
      
try:    
  bot1.start()
except Exception as e:
  pikalog.info(str(e))
try:    
  bot2.start()
except Exception as e:
  pikalog.info(str(e))
try:    
  bot3.start()
except Exception as e:
  pikalog.info(str(e))
try:    
  bot4.start()
except Exception as e:
  pikalog.info(str(e))  
try:    
  bot5.start()
except Exception as e:
  pikalog.info(str(e))
    
    

print("ClBot_started")

if __name__ == "__main__":
  bot.run_until_disconnected()
  

    
