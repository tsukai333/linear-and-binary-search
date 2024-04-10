from stackadtarray import StackArray
def main():
  stack = StackArray()
  while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Restore")
    print("6. Exit")
    print("7. Linear Search")
    print("8. Binary Search")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
      item = input("Enter item to push: ")
      stack.push(item)
    elif choice == "2":
      stack.pop()
    elif choice == "3":
      stack.peek()
    elif choice == "4":
      print("Stack size:", stack.size())
    elif choice == "5":
      stack.restore()
    elif choice == "6":
      print("Exiting........")
      break
    elif choice == "7":
        stack.linear(item)
    elif choice == "8":
        stack.binary_search(item)
    else:
      print("Invalid choice.")
      
if __name__ == "__main__":
    main()