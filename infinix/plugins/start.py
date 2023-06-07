
from .. import bot
from .. import bot2
from .. import bot3
from .. import bot4
from .. import bot1
from .. import bot5

from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError,UserAlreadyParticipantError,FloodWaitError,UserNotMutualContactError,UserChannelsTooMuchError
from telethon import events
from telethon import functions
import asyncio

sarwan=-1001565496823
sarwandes =-100195759753
abhi=-1001925550869
abhides=-1001905069234
nilesh = -1001534347784
nileshdes=-1001909694342


#b1 sarwanji 
#b2 nilesh ji
#b3 abhisk ji
#b4 sarwanji 
#b5 nilesh ji 


async def add(client,dest,target,ev):
  a = await client.get_participants(target, aggressive=True)
  for i in a:
    if not i.bot:
      if "Online" in str(i.status):
        await asyncio.sleep(5)
        try: 
           await client(functions.channels.InviteToChannelRequest(channel=dest,users=[i]))
        except UserPrivacyRestrictedError:
          await asyncio.sleep(2)
          continue
        except UserNotMutualContactError:
          await asyncio.sleep(2)
          continue
        except UserChannelsTooMuchError:
          await asyncio.sleep(2)
          continue
        except UserAlreadyParticipantError:
          await asyncio.sleep(2)
          continue
        except Exception as e:
          await asyncio.sleep(930)
          await ev.reply("waiting for 15 mins") 
          break
        except FloodWaitError:
          await ev.reply("Limit Exceeded")
          break  



@bot.on(events.NewMessage(incoming = True, pattern = "/ping"))
async def start(event):
  await event.reply("Hello This is Infinix Bot")

@bot.on(events.NewMessage(incoming = True, pattern = "/add"))
async def start(event):
  #await add(bot1,sarwandes,sarwan)
   await add(bot2,nileshdes,nilesh,event)
 # await add(bot3,abhides,abhi) 
  #await add(bot4,sarwandes,sarwan)
 # await add(bot5,nileshdes,nilesh)
  
           
 
