from random import randint
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(slf, fro, to):
        print(f"Ticket is booked in train no {slf.trainNo} from {fro} to {to}")
    
    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is runnig on time")
        
    def getFare(slf, fro, to):
         print(f"Ticket is booked in train no {slf.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(456555)
t.book("delhi", "surat")
t.getStatus()
t.getFare("suart", "delhi")