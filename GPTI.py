import random
import Emotionset
import openai
#from Emotionset import categorize

def generaterA(scoreA):
    if scoreA >.66:
        Amood="calm"
    if .66> scoreA >.33:
        Amood="irked"
    if .33>scoreA:
        Amood= "furious"
    return Amood
def generatedH(scoreH):
    if scoreH <.5:
        Hmood= "depressed"
    if scoreH>.5:
        Hmood= "Happy"
    return Hmood
def generateAX(scoreAX):
    if scoreAX <.33:
        AXmood ="Very Anxious"
    if .33<scoreAX <.66:
        AXmood ="nervous"
    if  scoreAX>.66:
        AXmood ="not nervous"
    return (AXmood)

class GPT:
    def __init__(self,who="",context="",model="curie",api_key="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"): #just provide key
        self.api_key=api_key
        self.who=who
        self.model=model
        self.context=context
        
        
    def generate_fullprompt(self,prompt):#remember to combine 
        return prompt

    def generate_comp(self,prompt):#should take in both self an prompt
        openai.api_key = "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"
        fullprompt=self.generate_fullprompt(prompt)
        Chat_Completion = openai.Completion.create(
            prompt=fullprompt,
            model= self.model,
            frequency_penalty=2,
            presence_penalty=.5,
            stop=['"'],
            top_p =.2,     
            temperature =.2,
            max_tokens=50,
        )
        print(Chat_Completion)
        return Chat_Completion




#myGPT =GPT("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", 20,0,"friend")

#response = myGPT.generate_comp(myprompt)


#
#resuse with self.
#ex. who,key
#class that sets emotional state
#change testing to use lower level classes
#completion first
# provide context through lower level class
#structure highlevel class that uses lower level
# Create a function to organize....


#Class organization
    # HigherLevel
        #