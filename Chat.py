# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:22:24 2020

@author: PRADHYUMNA
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
        'Medizoid',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        
    )
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
def chatty(text):
    bot_input = bot.get_response(text)
    return str(bot_input)