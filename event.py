from user import Person
from rental_shop import Camera

def display(answer):
    if answer == "1":
        name = input("name : ")
        numph = input("phone number : ")
        card_id = input("card id : ")
        print(
                """
                ===คุณต้องการกล้อง Model ไหน===
                กด 1 Model 200D   400บาท/วัน
                กด 2 Model 750D   350บาท/วัน
                กด 3 Model 850D   500บาท/วัน
                """
        )
        Ansmodel = input("camera model : ")
        obj1 = Camera()
        
        if Ansmodel == "1":
            model = obj1.data_Pop("200D")
        elif Ansmodel == "2":
            model = obj1.data_Pop("750D")
        elif Ansmodel == "3":
            model = obj1.data_Pop("850D")
            
        day = input("How many days : ")
        
        u = Person()
        u.inseart(name,numph,card_id,model,day,"ON")
        
        obj1.showStock()
    
    
    elif answer == "2":
        pass
    
    elif answer == "3":
        ca = Camera()
        ca.showStock()
        print("==================================")
        
        
    elif answer == "4":
        pass

            

       

    def re_camera():
        pass
    
    
    def check_stock():
        pass
    
    def exitPro():
        pass
    