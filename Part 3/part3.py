#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
#Any code taken from other sources is referenced within my code solution.

#Name                     :S.Ravindu Fernando
#Student ID (Wesminister ):w1809768
#Student ID (IIT)         :2019404
#Part three




pro  =0     #Total Progress
mt   =0     #Total module tralier
mr   =0     #Total module retriever
exc  =0     #Total excluded
count=0     #count is for total students
ex   =""    #User exit
total_c=0



while ex!='q' :
    try:
        Pass_c  =int(input("Please enter your pass credits:"))                      #user credits input
        Defer_c =int(input("Please enter your defer credits:"))
        Fail_c  =int(input("Please enter your fail credits:"))
        total_c=Pass_c + Defer_c + Fail_c
        count+=1                                                          #Total credits     
        if((Pass_c in range(0,125,20)) and (Defer_c in range(0,125,20)) and (Fail_c in range(0,125,20))):           #User range
            if total_c==120:                                                        #Total range
                if Pass_c==120 and Defer_c==0 and Fail_c==0:
                    print("-----Progress-----")                                     #progress               
                    pro+=1
                elif Pass_c<=80 and Defer_c<=120 and Fail_c<=60:
                    print("-----Do not progress - module retriever-----")           #Do not progress - module retriever
                    mr+=1
                elif Pass_c==100 and (Defer_c==20 or Fail_c==20):
                    print("-----Progress - (Module trailer)-----")                    #Progress - module trailer
                    mt+=1
                else:
                    print("-----Exclude-----")                                      #Exclude
                    exc+=1
            else:
                print("-----Total Invalid-----")                                    #Total Invalid
        else:
            print("-----Invalid Range-----")                                       #Invalid Range
    except ValueError:
        print("-----Integer Requried-----")                                        #Interger requried
    ex=input("-----If User want to exit press *q* if user want to continue press any key-----")  #If user press (q) exit and print histrogram" or If user want to continue press any key

print('')
print("-----Horizontal Histogram:")
print('')
print("-----Progress :" ,pro,"=", "*"*pro)                                        #user output star print
print("-----Trailer  :",mt,"=", "*"*mt)                                           #printing horizontal histrogram
print("-----Retriever:",mr,"=", "*"*mr)  
print("-----Excluded :",exc,"=", "*"*exc)
print('')
print(count,"Total outcomes in total.")

