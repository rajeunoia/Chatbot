from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import datetime 
import json

chatbot = ChatBot("doc")

vaccine_details = [
    "what are the vaccines at Birth ?",
    '{"0":{"vaccine_name":"BCG","total_number_of_doses":1,"dose_number":1,"number_of_days":0},"1":{"vaccine_name":"OPV","total_number_of_doses":4,"dose_number":1,"number_of_days":0},"2":{"vaccine_name":"Hep-B","total_number_of_doses":3,"dose_number":1,"number_of_days":0}}',
    "when is the next vaccine after Birth ? ",
    "6 weeks",
    "what are the vaccines at 6 weeks ?",
    '{"0":{"vaccine_name":"Rotavirus","total_number_of_doses":3,"dose_number":1,"number_of_days":42},"1":{"vaccine_name":"IPV","total_number_of_doses":4,"dose_number":1,"number_of_days":42},"2":{"vaccine_name":"Hib","total_number_of_doses":3,"dose_number":1,"number_of_days":42},"3":{"vaccine_name":"Hep-B","total_number_of_doses":1,"dose_number":1,"number_of_days":42},"4":{"vaccine_name":"PCV","total_number_of_doses":1,"dose_number":1,"number_of_days":42},"5":{"vaccine_name":"Dtwp/DTP","total_number_of_doses":1,"dose_number":1,"number_of_days":42}}',
    "when is the next vaccine after 6 weeks ? ",
    "10 weeks",
    "what are the vaccines at 10 weeks ?",
    '{"0":{"vaccine_name":"Rotavirus","total_number_of_doses":3,"dose_number":2,"number_of_days":42},"1":{"vaccine_name":"IPV","total_number_of_doses":4,"dose_number":1,"number_of_days":42},"2":{"vaccine_name":"Hib","total_number_of_doses":3,"dose_number":1,"number_of_days":42},"3":{"vaccine_name":"PCV","total_number_of_doses":1,"dose_number":1,"number_of_days":42},"4":{"vaccine_name":"Dtwp/DTP","total_number_of_doses":1,"dose_number":1,"number_of_days":42}}',
    "when is the next vaccine after 10 weeks ? ",
    "14 weeks",
    "what are the vaccines at 14 weeks ?",
    '{"0":{"vaccine_name":"Rotavirus","total_number_of_doses":3,"dose_number":3,"number_of_days":42},"1":{"vaccine_name":"IPV","total_number_of_doses":4,"dose_number":1,"number_of_days":42},"2":{"vaccine_name":"Hib","total_number_of_doses":3,"dose_number":1,"number_of_days":42},"3":{"vaccine_name":"PCV","total_number_of_doses":1,"dose_number":1,"number_of_days":42},"4":{"vaccine_name":"Dtwp/DTP","total_number_of_doses":1,"dose_number":1,"number_of_days":42}}',
    "when is the next vaccine after 14 weeks ? ",
    "6 months",
    "what are the vaccines at 6 months ?",
    '{"0":{"vaccine_name":"Hep-B","total_number_of_doses":3,"dose_number":3,"number_of_days":180},"1":{"vaccine_name":"OPV","total_number_of_doses":3,"dose_number":2,"number_of_days":180}}',
    "when is the next vaccine after 6 months ? ",
    "9 months",
    "what are the vaccines at 9 months ?",
    '{"0":{"vaccine_name":"MMR","total_number_of_doses":2,"dose_number":1,"number_of_days":270},"1":{"vaccine_name":"OPV","total_number_of_doses":3,"dose_number":3,"number_of_days":270}}',
    "when is the next vaccine after 9 months ? ",
    "1 year",
    "what are the vaccines at 1 year or 12 months ?",
    '{"0":{"vaccine_name":"Typhoid","total_number_of_doses":2,"dose_number":1,"number_of_days":365},"1":{"vaccine_name":"Hep-A","total_number_of_doses":2,"dose_number":1,"number_of_days":365}}',
    "when is the next vaccine after 1 year ? ",
    "15 months",
    "what are the vaccines at 15 months ?",
    '{"0":{"vaccine_name":"Typhoid","total_number_of_doses":2,"dose_number":1,"number_of_days":365},"1":{"vaccine_name":"Hep-A","total_number_of_doses":2,"dose_number":1,"number_of_days":365}}',
    "when is the next vaccine after 15 months ? ",
    "18 months",
    "what are the vaccines at 18 months ?",
    '{"0":{"vaccine_name":"Typhoid","total_number_of_doses":2,"dose_number":1,"number_of_days":365},"1":{"vaccine_name":"Hep-A","total_number_of_doses":2,"dose_number":1,"number_of_days":365}}',
    "when is the next vaccine after 18 months ? ",
    "2 years",
    "what are the vaccines at 2 years ?",
    '{"0":{"vaccine_name":"Typhoid","total_number_of_doses":2,"dose_number":1,"number_of_days":365},"1":{"vaccine_name":"Hep-A","total_number_of_doses":2,"dose_number":1,"number_of_days":365}}',
    "when is the next vaccine after 2 years ? ",
    "4 years",
    "what are the vaccines at 4 years ?",
    '{"0":{"vaccine_name":"Typhoid","total_number_of_doses":2,"dose_number":1,"number_of_days":365},"1":{"vaccine_name":"Hep-A","total_number_of_doses":2,"dose_number":1,"number_of_days":365}}',
    "when is the next vaccine after 4 years ? ",
    "10 years"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(vaccine_details)
msg = ""
inp = ""
conv = []
mode = "train"
global context_data
context_data = {"child_name":None,"child_age":None,"child_gender":None,"child_dob":None}
def child_register():
    child_name = input("What is your child name? ")
    child_gender = input("Is "+child_name+" male or female? ")
    print("What is "+child_name+" Date of Birth?")
    dob_month = int(input("Month(1-12): "))
    dob_day = int(input("Day(1-31): "))
    dob_year = int(input("Year(YYYY): "))
    born = datetime.date(dob_year,dob_month,dob_day)
    today = born.today() 
    age = today.year - born.year - (1 if today.month-born.month<0 else 0) , today.month - born.month - (1 if today.day-born.day<0 else 0),today.day-born.day if today.day-born.day>0 else (30 - born.day + today.day)
    child_details = {"name":child_name,"gender":child_gender,"dob":born}
    context_data = {"child_name":child_name,"child_age":age,"child_gender":child_gender,"child_dob":born}
    return child_details

def parse_vaccine_data(response):
    try:
        vacc_resp = json.loads(response.text)
        #print(vacc_resp)
        if vacc_resp is not str:
            for each_vacc in vacc_resp:
                for key,value in vacc_resp[each_vacc].items():
                    print(key, "  --  ", value)
                print("--------------------")
    except Exception as exp:
        print("Error ",exp.args)
   


if input("Do you want to share your child details ?(yes or no) ") == "yes":
    child_details = child_register()
    print(child_details)
while mode == "train" or mode == "talk":
    mode = input("you want to train or talk or exit :")

    if mode == "train":
        if input("Question and Answer ? ") == "Yes":
            qst = input("Enter the question: ")
            ans = input("Enter the answer :")
            conv = [qst,ans]
        elif input("Conversation ? ") == "Yes":
            while(inp != "Bye" and inp != "bye" ):
                inp = input("Enter : ")
                conv.append(inp)
        chatbot.train(conv)
        conv = []
    elif mode == "talk":
        while msg != "Bye" and msg !="bye":
            msg = input("You: ")
            if msg.find('month') != -1 and msg.find('week') != -1 and msg.find('year') != -1 and msg.find('day') != -1:
                if contex_data["child_age"] != None:
                    msg = msg + contex_data["child_age"]
                elif input("Do you want to share your child details ?(yes or no) ") == "yes":
                    child_details = child_register()
                    print(child_details)
                    
            response = chatbot.get_response(msg)
            #We need to have question type and basing on that , we need to have preprocessor call here, which will convert the dictonary to human readable format. 
            if msg.count("vaccine") > 0 and msg.count("next vaccine") < 1:
                parse_vaccine_data(response)
            else: 
                print(response)
    else: 
        print("Thanks for using our bot")
        

    