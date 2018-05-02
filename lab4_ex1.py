from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dbtest

def new_task(bot, update, args):
    taskToAdd = ' '.join(args)
    if taskToAdd and taskToAdd.strip() and (not taskToAdd.isspace()):
        result = dbtest.db_insert_task(taskToAdd)
        if result > 0:
            message = "The new task was successfully added to the list!"
        else:
            message = "No task was inserted due to a problem! Try again!"
    else:
        message = "You did not specify any task!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

def remove_task(bot, update, args):
    taskToRemove = ' '.join(args)
    message = ''
    if taskToRemove and taskToRemove.strip() and (not taskToRemove.isspace()):
        if dbtest.db_contains(taskToRemove):
            result = dbtest.db_remove_task(taskToRemove)
            if result > 0:
                message = "The task was successfully removed!"
            else:
                message = "No task was deleted due to a problem! Try again!"
        else:
            message = "The task you specified is not in the database!"
    else:
        message = "You did not specify any task!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    newMessage = "Now the list contains the following items:"
    bot.sendMessage(chat_id=update.message.chat_id, text=newMessage)
    updatedTaskList = dbtest.get_sorted_tasks_list()
    bot.sendMessage(chat_id=update.message.chat_id, text=updatedTaskList)

def remove_multiple_tasks(bot, update, args):
    substring = ' '.join(args)
    message = ''
    if substring and substring.strip() and (not substring.isspace()):
        result = dbtest.db_remove_multiple_tasks(substring)
        if (result > 0):
            message = "The elements were successfully removed!"
        else:
            message = "No task was deleted due to a problem! Try again!"
    else:
        message = "You did not specify any string!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    newMessage = "Now the list contains the following items:"
    bot.sendMessage(chat_id=update.message.chat_id, text=newMessage)
    updatedTaskList = dbtest.get_sorted_tasks_list()
    bot.sendMessage(chat_id=update.message.chat_id, text=updatedTaskList)

def print_sorted_list(bot, update):
    tasks_list = dbtest.get_sorted_tasks_list()
    message = ''
    if (len(tasks_list) == 0):
        message = "Nothing to do, here!"
    else:
        message = tasks_list
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

def start(bot, update):
    update.message.reply_text('Hello! This is AmITaskListBot. You can use one of the following commands:')
    update.message.reply_text('/newTask <task to add>')
    update.message.reply_text('/removeAllTasks <substring used to remove all the tasks that contain it>')
    update.message.reply_text('/showTasks')

def echo(bot, update):
    receivedText = update.message.text
    textToSend = "I'm sorry,. I'm afraid I can't do that"
    bot.sendMessage(chat_id=update.message.chat_id, text=textToSend)

if __name__ == '__main__':
    updater = Updater(token='579651830:AAFTlYal4Z_v6BGROXO0HRNVXnkDO-dp4CI')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    newTask_handler = CommandHandler('newTask', new_task, pass_args=True)
    dispatcher.add_handler(newTask_handler)
    removeTask_handler = CommandHandler('removeTask', remove_task, pass_args=True)
    dispatcher.add_handler(removeTask_handler)
    removeAllTasks_handler = CommandHandler('removeAllTasks', remove_multiple_tasks, pass_args=True)
    dispatcher.add_handler(removeAllTasks_handler)
    showTasks_handler = CommandHandler('showTasks', print_sorted_list)
    dispatcher.add_handler(showTasks_handler)
    updater.start_polling()
    updater.idle()
