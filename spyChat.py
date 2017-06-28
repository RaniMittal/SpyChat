from steganography.steganography import Steganography
from datetime import datetime,timedelta

spy_details={
    'rani':{
        'spy_salutation':'Ms.',
        'spy_age':21,
        'spy_status':'online',
        'spy_rating':4,
        'friend details':{
            'nikita':{
                'friend_salutation':'Ms.',
                'friend_age':22,
                'friend_rating':4.2,
                'chat_dict':{

                }
            },
            'lucky':{
                'friend_salutation':'Mr.',
                'friend_age':19,
                'friend_rating':3.5,
                'chat_dict':{

                }
            }
        }
    }
}



def spy_validation(spy_name):
    if len(spy_name) > 0:
        spy_salutation = raw_input("How we can address you? As Mr. or Ms.")
        spy_age = int(raw_input("What is your age?"))
        if spy_age >= 12 and spy_age <= 50:
            spy_status = "online"
            spy_rating = float(raw_input("enter your ratings between 1 to 5"))
            if spy_rating > 4 and spy_rating <= 5:
                print "Thanks.We think you enjoyed using this app"
            elif spy_rating > 3 and spy_rating <= 4:
                print "We hope you are enjoying this app."
            elif spy_rating > 2 and spy_rating <= 3:
                print "use this app more and more.we will add more features in the future"
            elif spy_rating > 1 and spy_rating <= 2:
                print "we think you are not happy with this app.if u have any problem mail us we will help you."
            else:
                print "ratings should be between 1 to 5"
                quit()
            print "Welcome %s %s.Your age is %i and your rating for this app is %f."%(spy_salutation,spy_name,spy_age,spy_rating)

            spy_details[spy_name] = {}
            spy_details[spy_name]['spy salutation']=spy_salutation
            spy_details[spy_name]['spy age']=spy_age
            spy_details[spy_name]['spy status'] = spy_status
            spy_details[spy_name]['spy rating'] = spy_rating
            print spy_details
            return spy_rating

        else:
            print "age must be between 12 and 50"
            quit()
    else:
        print "Name is invalid.Name can never be an empty string"
        quit()

status_list=['Available','Busy','In a meeting','Sleeping','Don\'t disturb']
no_of_friends=0

# function to add status
def add_status():
    status_choice=int(raw_input("1.you want to select a status from predefined list or to 2.create your own status"))
    if status_choice==1:
       print status_list
       current_status=int(raw_input("Choose a status\n 1.Available\n 2.Busy\n 3.In a meeting\n 4.Sleeping\n 5.Don't disturb"))
       print "your updated status is " + str(current_status)
    elif status_choice==2:
        new_status=raw_input("what is the status?")
        status_list.append(new_status)
        print "updated status is " + new_status
        current_status=new_status

# function to add a new friend
def add_friend(spy_name,spy_rating):
    friend_name = raw_input("What is your friend name?")
    if friend_name in spy_details[spy_name]['friend details'].keys():
        print "your friend %s is already exist in your friend list"%(friend_name)
    else:
        if len(friend_name) > 0:
            friend_salutation = raw_input("How you can address your friend? As Mr. or Ms.")
            friend_age = int(raw_input("What is your friend age?"))
            if friend_age>=12 and friend_age<=50:
                friend_rating = float(raw_input("enter your friends ratings"))
                if friend_rating >= spy_rating:
                    spy_details[spy_name]['friend details'][friend_name]={}
                    spy_details[spy_name]['friend details'][friend_name]['friend salutation'] = friend_salutation
                    spy_details[spy_name]['friend details'][friend_name]['friend age'] = friend_age
                    spy_details[spy_name]['friend details'][friend_name]['friend rating'] = friend_rating
                else:
                    print "rating is less than the spy rating"
            else:
                print "age is invalid"
        else:
            print "name is invalid"
    print str(spy_name) + " your friends are "
    print spy_details[spy_name]['friend details'].keys()
    return len(spy_details[spy_name]['friend details'].keys())


# function to select a friend with whom user want to communicate
def select_a_friend(spy_name1):
    print spy_details[spy_name1]['friend details'].keys()
    friend_choice = raw_input("select a friend from the above list to whom you want to talk to?")
    print "you selects the friend " + str(friend_choice)
    return spy_details[spy_name1]['friend details'].keys().index(friend_choice)


# function to send message
def send_message(spy_name):
    spy_name1=spy_name
    friend_choosen=select_a_friend(spy_name1)
    image_choice=raw_input("enter the name or path of image with which you want to encode the message ")
    secret_message=raw_input("enter the message you want to encode")
    image_choice2=raw_input("enter the name or path of encrypted image")
    Steganography.encode(image_choice,image_choice2,secret_message)
    message_time=datetime.today()
    sender_name=spy_name
    spy_details[spy_name1]['friend details'][spy_details[spy_name1]['friend details'].keys()[friend_choosen]]['chat_dict']['image having hidden message']=image_choice2
    spy_details[spy_name1]['friend details'][spy_details[spy_name1]['friend details'].keys()[friend_choosen]]['chat_dict']['receiver name']=spy_details[spy_name1]['friend details'].keys()[friend_choosen]
    spy_details[spy_name1]['friend details'][spy_details[spy_name1]['friend details'].keys()[friend_choosen]]['chat_dict']['message time']=message_time
    return image_choice2

# function to read message
def read_message(spy_name):
    sender_name=spy_name
    friend_choosen=select_a_friend(sender_name)
    image_choice=spy_details[sender_name]['friend details'][spy_details[sender_name]['friend details'].keys()[friend_choosen]]['chat_dict']['image having hidden message']
    secret_text2=Steganography.decode(image_choice)
    if len(spy_details[sender_name]['friend details'][spy_details[sender_name]['friend details'].keys()[friend_choosen]]['chat_dict'].keys())==0:
        print "you have no message to read from this friend"
    else:
        print secret_text2
# function to read chat history
def read_chat(spy_name):
    sender_name = spy_name
    friend_choosen = select_a_friend(sender_name)
    if len(spy_details[sender_name]['friend details'][spy_details[sender_name]['friend details'].keys()[friend_choosen]]['chat_dict'].keys())==0:
        print "you have no previous chat history with this friend"
    else:
        print spy_details[sender_name]['friend details'][spy_details[sender_name]['friend details'].keys()[friend_choosen]]['chat_dict']

# main program
more_user=0
print "Hlo spy! Welcome to the spy chat"
user_choice = int(raw_input("Do you want to continue with the 1.default user or 2.create a new one"))
if user_choice == 1:
    print spy_details
elif user_choice==2:
    while more_user!=2:
         spy_name=raw_input("What is your name?")
         if spy_name in spy_details.keys():
             print "you already exist"
             print spy_details
         else:
             spy_validation(spy_name)
         more_user=int(raw_input("do u want to add more spies 1.yes 2.no"))
spy_choice=0
while spy_choice!=6:

    spy_choice=int(raw_input("What you want to do?\n 1.Add Status\n 2.Add a friend\n 3.Send an encoded message\n 4.Read message\n 5.Read previous history\n 6.Close the app"))
    if spy_choice==1:
       add_status()
    elif spy_choice==2:
        if user_choice==1:
            spy_name=spy_details.keys()[0]
        else:
            print spy_details.keys()
            spy_name = raw_input("choose a name from above list")
        spy_rating=spy_details[spy_name]['spy_rating']
        no_of_friends=add_friend(spy_name,spy_rating)
        print "you have " + str(no_of_friends) + "friends"
    elif spy_choice==3:
        if user_choice==1:
            spy_name = spy_details.keys()[0]
        else:
            print spy_details.keys()
            spy_name = raw_input("choose a name from above list")
        send_message(spy_name)
    elif spy_choice==4:
        if user_choice==1:
            spy_name = spy_details.keys()[0]
        else:
            print spy_details.keys()
            spy_name = raw_input("choose a name from above list")
        read_message(spy_name)
    elif spy_choice==5:
        if user_choice==1:
            spy_name = spy_details.keys()[0]
        else:
            print spy_details.keys()
            spy_name = raw_input("choose a name from above list")
        read_chat(spy_name)
    elif spy_choice==6:
        quit()
    else:
         print "wrong choice"

