# Telelogger
You can find the keylogger program which gives the output to the telegram chat group.

To get the output in your telegram group please follow the below steps.

1) Create a Bot using @BotFather
     1) Select the /newbot option to create your bot and add a name and username to it.
     2) Once this is done, @BotFather will generate an API token for you (which should not be shared)
     3) Use this in the API token field mentioned in the code (Token Ex: 987654321:qwertyuioppiojnun_bhcbdh)

2) Create a Group
    1) In this Group add the bot that you created.
    2) Once this is done, we need the chat ID of the group to which we have the bot added. For this use this URL ( https://api.telegram.org/bot{YourBOTToken}/getUpdates ) and mostly your output will be "{"ok":true,"result":[]} " which is not one that we want. So in order for the URL to work, first run the command (/my_id @YOUR_BOT_Name) in the group and then run the URL (if it does not work retry again). You will get a similar output.
  
    {
    "update_id": 1234,
    "message": {
        "message_id": 3,
        "from": {
            "id": 9874,
            "first_name": "AAA"
        },
        "chat": {
            "id": <CHAT_ID>,
            "title": "<Group name>"
        },
        "date": 25497,
        "new_chat_participant": {
            "id": 71, 
            "first_name": "NAME",
            "username": "YOUR_BOT_NAME"
        }
    }

} 
     3)Once we obtain the chat ID we can use it in the below URL inorder to get an output by the bot. 
          https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=<CHAT_ID>&text="This is a message"

3) RUNNING THE PROGRAM
     1) Make sure the install pynput and requests library before running the code.
