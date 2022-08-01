
class Camera():
    
    def __init__(self):
        self.dic_data = {   
                            "200D":["200D01","200D02","200D03"],
                            "750D":["750D01","750D02","750D03"],
                            "850D":["850D01","850D02","850D03"]
                        }
        return None
    
        
            
    def data_Pop(self,model):
       
        for i in self.dic_data:
            if model == i:
                obj2 = self.dic_data[i]
                Atpop = obj2.pop()
            else:
                pass
        return Atpop
    
    def showStock(self):
        for stoke in self.dic_data:
            print("เหลือกล้อง "+stoke+"  "+str(len(self.dic_data[stoke]))+" ตัว")
        

if __name__=="__main__": 
    pass
    #d = Camera()

    #print(d.data_Pop("200D"))
    #print(d.dic_data["200D"])
    #print(d.dic_data)
    #print(d.showStock())
      
    ###b = obj1.dic_data.keys()

   ## for i in range(2):
       # a = input("===")
       # if len(obj1.dic_data["200D"]) > 0:
           # obj1.havePop(a)
          #  print(obj1.dic_data)
        
        
    #print(len(obj1.dic_data["200D"]))

    #obj1.showStoke
