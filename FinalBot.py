import Emotionset
Es=Emotionset.emotionSetter("","","curie","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")
# Anger Happy Fear Confusion
testemotions=[(55,11,77,88),
              (14,66,22,99)]
for test in testemotions:
    Anger,Happy,Fear,Confusion=test
    result=Es.generate_greeting(Anger,Happy,Fear,Confusion)
    print("Anger={Ang},Happy={Hap},Fear={Fea},Confusion={Con},Result={res}".format(Ang=Anger,Hap=Happy,Con=Confusion,Fea=Fear,res=result))


