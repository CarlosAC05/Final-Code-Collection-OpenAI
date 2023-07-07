import random
import GPTI
import Emotionset

numb= random.randint(0,100)
if numb<33:
    person="amanda"
if 32<numb<66:
    person="my friend"
if numb>65:
    person="he"
print(person)

testingset=Emotionset.emotionSetter((random.randint(0,100)),(random.randint(0,100)),(random.randint(0,100)),(random.randint(0,100)),"","amanda")
testingset.generate_call()







