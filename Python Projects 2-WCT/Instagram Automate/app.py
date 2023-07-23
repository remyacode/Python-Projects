from instabot import Bot

bot=Bot()
bot.login(username="",password="") #your username and apssword
bot.follow('') #who do u want to follow-username

#upload image
bot.upload_photo("",caption="") #enter path with / slashes

bot.unfollow('') #who do u want to unfollow-username

#send message to multiple people
bot.send_message("i love python",["","",""]) #enter usernames

#see followers 
followers=bot.get_user_followers("")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following("")
for Following in following:
    print(bot.get_user_info(Following))