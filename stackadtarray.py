class StackArray:
    def __init__(self):
        self.items = []
        self.actions = []  
        self.popped_items = [] 
        
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < 10:
            if item not in self.items: 
                self.items.append(item)
                print(item, "pushed onto the stack.")
                self.actions.append(('push', item))  
            else:
                print("Cannot push item. Item already exists in the stack.")
        else:
            print("Cannot push more items. Stack is full.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print("Popped:", popped_item)
            self.actions.append(('pop', popped_item))  
            if len(self.popped_items) < 2:
                self.popped_items.append(popped_item)  
            else:
                self.popped_items.pop(0)  
                self.popped_items.append(popped_item)  
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            print("Top item:", self.items[-1])
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def restore(self):
        if self.popped_items:
            item_to_restore = self.popped_items.pop()  
            self.push(item_to_restore) 
            print("Restored:", item_to_restore)
        else:
            print("Can't restore anymore.")

    def linear(self, x):
            x = input("Enter Item: ")
            for i in range(len(self.items)):
                if self.items[i] == x:
                    return print(" fajdfa: ",i)
            return print("-1")
            

    def binary_search(self, target):
        target= input("Enter Item: ")
        left, right = 0, len(self.items) - 1
        while left <= right:
            mid = (left + right) // 2
            match = self.items[mid]

            if target == match:
                return print("Found at : ", mid)
            elif target < match:
                right = mid - 1
            else:
                left = mid + 1
        return print("kahit ano")

    
    
        
                
                
    
    
         
        
    

    

 