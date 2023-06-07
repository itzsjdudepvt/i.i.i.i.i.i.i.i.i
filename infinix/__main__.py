import glob 
from pathlib import Path 
from infinix.utils import load_plug
import logging 
from . import bot,bot1,bot2,bot3,bot4,bot5

path= "infinix/plugins/*.py"
files=glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plug_name = pxt.stem
    load_plug(plug_name.replace(".py", ""))
    
bot1.start()
bot2.start()
bot3.start()
bot4.start()
bot5.start()
print("ClBot_started")

if __name__ == "__main__":
  
  bot1.run_until_disconnected()
  bot2.run_until_disconnected()
  bot3.run_until_disconnected()
  bot4.run_until_disconnected()
  bot5.run_until_disconnected()
  bot.run_until_disconnected()


    
