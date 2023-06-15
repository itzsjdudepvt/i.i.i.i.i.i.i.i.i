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
  print(str(e))
try:    
  bot2.start()
except Exception as e:
  print(str(e))
try:    
  bot3.start()
except Exception as e:
  print(str(e))
try:    
  bot4.start()
except Exception as e:
  print(str(e)) 
try:    
  bot5.start()
except Exception as e:
  print(str(e))
    
    
print("ClBot_started")

if __name__ == "__main__":
  bot.run_until_disconnected()
  

    
