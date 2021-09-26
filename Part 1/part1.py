#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Name                     :S.Ravindu Fernando
#Student ID (Wesminister ):w1809768
#Student ID (IIT)         :2019404
#Part one

total_c=0


Pass_c  =int(input("Please enter your pass credits:"))                         #Enter user inputs
Defer_c =int(input("Please enter your defer credits:"))
Fail_c  =int(input("Please enter your fail credits:"))

total_c=Pass_c + Defer_c + Fail_c                                              #Total of pass credits + defer credits + fail credits

if ((Pass_c in range(0,125,20)) and (Defer_c in range(0,125,20)) and (Fail_c in range(0,125,20))):               #Enrer the valid range 
        if total_c==120:
            if Pass_c ==120 and Defer_c==0 and Fail_c==0:                      #Progress Module
               print("-----Progress-----")                                     
            elif Pass_c<=80 and Defer_c<=120 and Fail_c<=60:                         
                print("-----Do not Progress-Module Retriever-----")            #Do not progress module retriever
            elif Pass_c==100 and (Defer_c==20 or Fail_c==20):
                print("-----Progress-(Module Trailer)-----")                     #Module Trailer
            else:
                print("-----Exclude-----")                                     #Exclude
     
            
           
