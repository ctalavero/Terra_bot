from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot ( token='940348155:AAGW5ZQ7UQ68lE7Lvb6EOThbfxUI7AG6h_M' )
dp = Dispatcher ( bot )
#############################++

@dp.message_handler ()
async def get_message(message: types.message):
    chat_id = message.chat.id
    if message.text == '!сбор':
        text = '@NeKot1n @DimaReznik @Ctalavero12 @Author1ty @Akonsu @sashkaaa_0911 @menthyl_isovalerate Гудыма @Magic_rabbit_rin @leonid_nen Stas Vania''😀😀😀😀😀😀😀 @waiiffu @Vee122 @sacred_Helga Max @viannedi @glebanchik228 @illyadooms'
        f = open ( 'log.txt', 'a' )
        log=await bot.send_message ( chat_id=chat_id, text=text )
        f.write(str(log)+'\n'+'_________________________________________________'+'\n')
        f.close ()
executor.start_polling ( dp )
'''
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot ( token='940348155:AAGW5ZQ7UQ68lE7Lvb6EOThbfxUI7AG6h_M' )
dp = Dispatcher ( bot )
@dp.message_handler ()
async def get_message(message: types.message):
    chat_id = message.chat.id
    if message.text == 'Збор!всех':
        tex = '@Author1ty @Akonsu @NeKot1n Дима @sashkaaa_0911 @menthyl_isovalerate @Magic_rabbit_rin @leonid_nen Stas Vania''😀😀😀😀😀😀😀 @waiiffu @Vee122 @sacred_Helga @viannedi @glebanchik228 @illyadooms Гудыма '
    f = open ( 'log.txt', 'a' )
    log=await bot.send_message ( chat_id=chat_id, text=text )
    f.write(str(log)+'\n'+'________________________________________________________________________'+'\n')
    f.close ()
executor.start_polling ( dp )'''