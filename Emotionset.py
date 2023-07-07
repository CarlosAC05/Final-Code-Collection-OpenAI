
import openai
import GPTI

class emotionSetter:
    def __init__(self,who="",context="",model="curie",api_key="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"):
        gpt=GPTI.GPT(who,context,model,api_key)#Context and who passed to GPT,developed here

        self.who=who
        self.model=model
        self.api_key=api_key
    def categorize(self):
        if self.Ang >50:
            Anger="Angry"
        if self.Ang<=50:
            Anger=""
        Hmood=self.contracheck()
        if self.Fea >60:
            Feamood="scared"
        if self.Fea<61:
            Feamood =""
        if self.Con >55:
            Conf="confused"
        if self.Con<56:
            Conf =""
        self.Con=Conf
        self.Ang=Anger
        self.Fea=Feamood
        self.Hap=Hmood
        #Ang,Hap,Fea,Con
    def contracheck(self):
        if ((self.Hap +10)<self.Ang)and self.Hap>50:
            return ""
        if ((self.Hap +5)<self.Fea) and self.Hap>50:
            return ""
        if ((self.Hap)<self.Con)and self.Hap>50:
            return ""
        if (self.Hap)>50:
            return "Happy,"
        if (self.Hap)<51:
            return "Depressed"
    def neutralcheck(self):
        if self.Hap<50:
            print("False: not neutral scenerio")
            return False
        if (self.Ang and self.Fea and self.Con)<50:
            print("True: neutral response deployed")
            return True
    def neutralcat(self):
        self.Hap="happy"

    def generate_greeting(self,Ang,Hap,Fea,Con):#Use 
        prompt=self.generate_prompt(Ang,Hap,Fea,Con)
        result=self.GPT.generate_comp(prompt)
        return result
        
    

    def generate_prompt(self,Ang,Hap,Fea,Con):
        #tempE=emotionSetter(self.Ang,self.Hap,self.Fea,self.Con)
        print(Hap,Fea,Con,Ang)
        if(self.neutralcheck()):
            self.neutralcat()
            tempP= (self.who + " feels " + Hap  +'. My response:"' )
            self.model= "curie:ft-personal-2023-06-30-15-56-57"
            print(self.model)
            print(tempP)
            
        else:
            self.categorize()
            tempP= (self.who + " feels " +Hap +" , "+ Ang + ", " + Fea + " and " + Con+'. my response:"')
            self.model= "curie:ft-personal-2023-06-30-15-56-57"
            print(self.model)
            print(tempP)    
        return tempP
    



#Class strucutre was changed remember to change



#NEEDS TO BE CHANGED LATER TO REFLECT FINAL COMBINATIONS --changed but probably not final
#document these functions for future use in ECL bundle
#look at GNN bundle ECL by dev roger