import glob 
from pathlib import Path 
from infinix.utils import load_plug
import logging 
from logging import getLogger
from . import bot,bot1,bot2,bot3,bot4,bot5
pikalog = getLogger(__name__)


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)
async def start():
  path= "infinix/plugins/*.py"
  files=glob.glob(path)

  for name in files:
    with open(name) as a:
      pxt = Path(a.name)
      plug_name = pxt.stem
      load_plug(plug_name.replace(".py", ""))  
      
  try:    
    await bot1.start()
  except Exception as e:
    pikalog.info(str(e))
  try:    
    await bot2.start()
  except Exception as e:
    pikalog.info(str(e))
  try:    
    await bot3.start()
  except Exception as e:
    pikalog.info(str(e))
  try:    
    await bot4.start()
  except Exception as e:
    await pikalog.info(str(e))  
  try:    
    await bot5.start()
  except Exception as e:
    pikalog.info(str(e))
    
    
  bot.run_until_disconnected()
print("ClBot_started")

if __name__ == "__main__":
  pikaloop = asyncio.get_event_loop()  
  pikaloop.run_until_complete(start())
  

    
