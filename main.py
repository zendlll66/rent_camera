from event import display
from rental_shop import Camera

while exitPro == 1:
    print(
                    """
                    
                ================================
                ==      คุณต้องการจะทำอะไร      ==
                ==   พิมพ์ 1. เพื่อทำการ  ยืม     ==
                ==   พิมพ์ 2. เพื่อทำการ  คืน     ==
                ==   พิมพ์ 3. เพื่อเช็คของในคลัง   ==
                ==   พิมพ์ 4. ออกโปรแกรม       == 
                ================================
                    """
            )
    
    answer = input("โปรดเลือกสิ่งที่คุณต้องการ : ")
    if answer == "4":
        exitPro = exitPro+1
    else:
        display(answer)
        
    
        
        
        