#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Name                     :S.Ravindu Fernando
#Student ID (Wesminister ):w1809768
#Student ID (IIT)         :2019404
#Part two


total_c=0

while True:
    try:
        Pass_c  =int(input("Please enter your pass credits:"))                              
        Defer_c =int(input("Please enter your defer credits:"))      #User credits
        Fail_c  =int(input("Please enter your fail credits:"))
        total_c=Pass_c + Defer_c + Fail_c                                                      #Total credits = pass + defer + fail
        if((Pass_c in range(0,125,20)) and (Defer_c in range(0,125,20)) and (Fail_c in range(0,125,20))):                          #User range
            if total_c==120:
                if Pass_c==120 and Defer_c==0 and Fail_c==0:                                #progress
                    print("-----Progress-----")
                    break
                elif Pass_c<=80 and Defer_c<=120 and Fail_c<=60:
                    print("-----Do not progress - module retriever-----")
                    break                                                                   #Do not module retriever
                elif Pass_c==100 and (Defer_c==20 or Fail_c==20):
                    print("-----Progress -(Module trailer)-----")
                    break                                                                   #Progress module trailer
                else:
                    print("-----Exclude-----")
                    break                                                                   #Exclude
            else:
                print("-----Total incorrect.-----")                                         #If user input total invalid
        else:
            print("-----Out of Range.-----")                                                #If user input Invalid range
    except ValueError:
        print("-----Integer Requried-----")                                                 #Integer requried
                                            
                                                                              
