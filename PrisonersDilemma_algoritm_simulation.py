
import random
ROUND=10
POINT= {
    "CC":4,
    "CD":0,
    "DC":5,
    "DD":2
}

class BaseType:
    def __init__(self):
        self.total = []
        self.answer = ""

    def decision(self):
        pass

    def answers(self,other):
        pass


    def __mod__(self, other):
        #temp_self=[]
        #temp_other=[]
        for i in range(ROUND):

            self.decision()
            other.decision()

            self.answers(other)
            other.answers(self)

            final_answer = self.answer + other.answer
            final_enemy_anwer=other.answer+self.answer
            self.total.append(final_answer)
            other.total.append(final_enemy_anwer)
            
        #     temp_self.append(final_answer)
        #     temp_other.append(final_enemy_anwer)

        # print("First",temp_self,"\n"," Second ",temp_other)

class Type1(BaseType):
    def __init__(self):
        super().__init__()
        self.answer = "C"

class Type2(BaseType):
    def __init__(self):
        super().__init__()
        self.answer = "D"

class Type3(BaseType):
     
    def __init__(self):
        super().__init__()

    def decision(self):

        if random.random() > 0.5:
            self.answer="C"
        else:
            self.answer="D"

class Type4(BaseType):

    def __init__(self):
        super().__init__()
        self.no_round=0
        self.pre_enemy_answer="C"

    def decision(self):

        if self.no_round % 10 ==0:
            self.pre_enemy_answer="C"
        
        if self.pre_enemy_answer == "D":
            self.answer="D"
        else:
            self.answer="C"

        self.no_round+=1

    def answers(self,other):
        self.pre_enemy_answer=other.answer
        
type1_input=int(input("Type1:"))
type2_input=int(input("Type2:"))
type3_input=int(input("Type3:"))
type4_input=int(input("Type4:"))
        
type1_objects = [Type1() for _ in range(type1_input)]
type2_objects = [Type2() for _ in range(type2_input)]
type3_objects = [Type3() for _ in range(type3_input)]
type4_objects = [Type4() for _ in range(type4_input)]

objects=type1_objects+type2_objects+type3_objects+type4_objects

for i in range(len(objects)):
    for j in range(len(objects)):
        if i>=j:
            continue
        else:
            objects[i] % objects[j]

def type_total_point(type_object):
    type_total=0
    for i in range(len(type_object)):
        type_point = sum(list(map(lambda item: POINT[item], type_object[i].total)))
        #print("Length of type:",len(list(map(lambda item: POINT[item], type_object[i].total)) ))
        type_total+=type_point
    return type_total




print("Total Score:",type_total_point(objects),"\n")

if len(type1_objects)!=0:
    print("Type1:",type_total_point(type1_objects)/len(type1_objects)," Total Type 1: ",type_total_point(type1_objects), "\n")
if len(type2_objects)!=0:
    print("Type2:",type_total_point(type2_objects)/len(type2_objects)," Total Type 2: ",type_total_point(type2_objects), "\n")
if len(type3_objects)!=0:
    print("Type3:",type_total_point(type3_objects)/len(type3_objects)," Total Type 3:",type_total_point(type3_objects), "\n")
if len(type4_objects)!=0:
    print("Type4:",type_total_point(type4_objects)/len(type4_objects)," Total Type 4: ",type_total_point(type4_objects), "\n")   


