class TicketQueue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self,ticket):
        if not ticket:
            return None
        else:
            self.queue_list.append(ticket)
            return self.size()
        
    def size(self):
        return len(self.queue_list)
    
    def peek(self):
        if  not self.queue_list:
            return None
        else:
            first_value = self.queue_list[0]
            return first_value
        
    def dequeue(self):
         if self.peek() is None:
             return None
         else:
             self.queue_list.pop(0)
             return self.peek()

