
def find_brackets(string):
    cont = True
    while cont == True:
        cont = False
        for i in ["()","{}","[]"]:
            if i in string:
                cont = True
                string = string.replace(i,"")
    return len(string) == 0
                
print(find_brackets(""))