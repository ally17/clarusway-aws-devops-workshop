while True:
    print("###  This program converts milliseconds into hours, minutes, and seconds ###\n") 
    num = input("""(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) :  """)
    if num.lower() == "exit":
        print("Exiting the program... Good Bye")
        break
    if not num.isdecimal() or int(num) < 1:
        print("\nNot Valid Input !!!\n")
    
    if num.isdecimal():
        num = int(num)
        
        hour = num // 3600000
        num = num - hour * 3600000
        
        minute = num // 60000
        num = num - minute * 60000
        
        second = num // 1000
        num = num - second * 1000
        
        if hour == 0 and minute == 0 and second == 0:
            print(f"\njust {num} millisecond/s")
        elif hour == 0 and minute == 0 and second != 0:
            print(f"\n{second} second/s")
        elif hour == 0 and minute != 0 and second == 0:
            print(f"\n{minute} minute/s")
        elif hour != 0 and minute == 0 and second == 0:
            print(f"\n{hour} hour/s")
        elif hour == 0 and minute != 0 and second != 0:
            print(f"\n{minute} minute/s {second} second/s")
        elif hour != 0 and minute == 0 and second != 0:
            print(f"\n{hour} hour/s {second} second/s")
        elif hour != 0 and minute != 0 and second == 0:
            print(f"\n{hour} hour/s {minute} minute/s")
        elif hour != 0 and minute != 0 and second != 0:
            print(f"\n{hour} hour/s {minute} minute/s {second} second/s")