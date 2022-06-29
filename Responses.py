from datetime import datetime
import random

def sample_responses(input_txt):
    user_message = str(input_txt).lower()
    result = []
    if user_message in ("i need a friend", "be my friend", "will you be my friend"):
        return "hi👋..\n\nMessage form creator: My bot took on my charector and is a little introverted but i hope you treat my BlueBat as a friend"
        
    if user_message == "i am an idiot":
        return"Same"

    if user_message in ("time", "time?", "what is the time", "what is the time now?"):
        now  = datetime.now()
        return str(now.strftime("%d/%m/%y, %H:%M:%S"))

    if user_message == "luck please":
        charm= " ᓚᘏᗢ \n 'the cat wishpers--meow'"
        return charm


    options = ("rock", "paper", "scissors")
    if user_message in options:
        computerChoice = random.choice(options)

        l1 = len(user_message)
        l2 = len(computerChoice)
        result.append(computerChoice)
        #rock:4--paper:5--scissors:8
        if (l1 == 4 and l2 ==8) or (l1==5 and l2==4) or (l1==8 and l2==4):
            game_result= "You Win"
            return "computer choose: \t"+computerChoice+"\nResult: \t"+game_result
        elif (l1 == l2):
            game_result= "Its a tie"
            return "computer choose: \t"+computerChoice+"\nResult: \t"+game_result
        else:
            game_result= "You loose"
            return "computer choose: \t"+computerChoice+"\nResult: \t"+game_result
    else:
        v = False
        return v
