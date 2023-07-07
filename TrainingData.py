import openai
import os
import json
openai.api_key = "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"

# Amood ="furious"
     #  Amood="irked"
   #     Amood="calm"
#       Hmood ="ecstatic"
   #     Hmood="deppresed"
   #     Hmood="content"
   #     AXmood="extremly nervous"
     #   AXmood="nervous"
   #     AXmood="not nervous"
  #  mood ="I feel " + " and ".join([Amood,Hmood,AXmood]) 
   # return {"role": "user","content": mood}

Training=[("they feel happy. My response:", "you seem well, how is your day going?"),
          ("they feel Depressed, Angry, scared and confused. My response: , ","you seem upset is everything alright?"),
          ("they feel confused and Scared. My response: ","Is everything all right you seem out of it"),
          ("they feel happy, my Response: ","hello, hows it hanging?'"),
          ('they feel Angry and Confused. My response:"','you seem upset, what is the issue?"'),
          ("they feel calm depressed and confused,","you seem down today could you tell me more about it?"),
          ("they feel confused, depressed, and scared, my response:'You seem upset, is something the matter?")
          ]
outitems=[]
for item in Training:
    out=repr({"prompt":item[0],"completion":item[1]})
    outitems.append(out)
outstring="\n".join(outitems)
outstring=outstring.replace("'",'"')
f =open("./FineTG2","w+")
f.write(outstring)
f.close()
#openai--api-key "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" api fine_tunes.create -t "C:/Users/ccace/VSAI/FineT3_prepared.jsonl" -m "davinci-003" 







