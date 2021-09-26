#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Name                     :S.Ravindu Fernando
#Student ID (Wesminister ):w1809768
#Student ID (IIT)         :2019404
#Part Five


pro  =0     #Total Progress
mt   =0     #Total module tralier
mr   =0     #Total module retriever
exc  =0     #Total excluded
count=0     #count is for total students
total_c=0


try:
    Pass  = [120, 100, 100, 80, 60, 40, 20, 20 ,20,0]
    Defer = [0,20,0,20,40,40,40,20,0,0]
    Fail  = [0,0,20,20,20,40,60,80,100,120]


    for i in range (0,10):
        count += 1
        Pass_c  = Pass[i]           #Assigning character to Pass,Defer,Fail to list in range
        Defer_c = Defer[i]
        Fail_c =Fail[i]
        total_c=Pass_c + Defer_c + Fail_c   
        if total_c==120:
            if Pass_c==120 and Defer_c==0 and Fail_c==0:
                print("-----Progress-----")                                    #Progress
                pro+=1
            elif Pass_c==100 and (Defer_c==20 or Fail_c==20):
                print("-----Progress - (Module trailer)-----")                 #Progress - (Module trailer)                
                mt+=1
            elif Pass_c<=80 and Defer_c<=120 and Fail_c<=60:
                print("-----Do not progress - Module retriever-----")          #Do not progress - Module retriever 
                mr+=1

            else:
                print("-----Exclude-----")                                     #Exclude                            
                exc+=1
        else:
            print("-----Total Invalid-----")                                   #Total invalid
except:
    print()



print('')
print("-----Progress :",pro,"=","*"*pro)                                       #Printing verticle histogram
print("-----Trailing :",mt,"=","*"*mt)
print("-----Retriever:",mr,"=","*"*mr)
print("-----Excluded :",exc,"=","*"*exc)
print('')
print(count,"Total outcomes in total.")



