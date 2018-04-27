import pygame,time,random,pygame.mixer,pickle,os
cash=0
print"**********************************************************************"
print"                  Welcome to Al Khor Community"
print"**********************************************************************"
print 
print "You may use the mouse to click the places you'd like to visit."
print 
print "For shopping purposes please make a new credit card at the Bank if you don't own one already"
print 
print "Happy Visiting Al Khor Community"
print 
simply=raw_input("Hit Enter to continue")
print 
pygame.init()

width,height=479,822
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Al Khor Community')



done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)

# Current position
x_coord = 0
y_coord = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x_coord=pos[0]
            y_coord=pos[1]
                        

#Codes for the changing of frames or going inside the building
                                
    #Entering the Medical Centre
    if x_coord in range (24,67) and y_coord in range(7,48):

        pygame.init()
        pygame.mixer.music.load('Start.wav')
        pygame.mixer.music.play()
        x_coord = 0
        y_coord = 0
        
        
    if x_coord in range (294,413) and y_coord in range(411,523):
        Total=0
        width,height=794,539
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Loading')
        background=pygame.image.load('load1.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1500)
        pygame.display.flip()
        clock.tick(30)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()
        
        pygame.init()
        width,height=708,424
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Medical Centre')
        done = False
        clock = pygame.time.Clock()
        # Current position
        x_coord = 0
        y_coord = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]


            #Go for Normal Health Checkup
            if x_coord in range (488,694) and y_coord in range(49,64):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                print "Please take a number."
                b=random.randrange(2,10)
                print "This is your number.\n",b,"\n"
                print "Please wait for your turn.\n"
                print random.randrange(11,30)
                print random.randrange(11,30)
                print b,"\n" 
                print"It's your turn. Please proceed to room 101 for a normal Health Checkup\n"
                number=raw_input("What is your QG/RG staff number?\n")  
                print "Please check and enter your height in 'cm' and weight in 'kilograms'."
                ht=input("Please enter your height-")
                wt=input("Please enter your weight-")

                print "Your height is",ht,"and weight is",wt,"\n"
                print "Checking your blood pressure...\n"
                
                pygame.init()
                width,height=670,503
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Checking Blood Pressure')
                background=pygame.image.load('bp.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                bps=random.randrange(115,185)
                bpd=random.randrange(75,115)
                if 115<bps<119 or 75<bpd<79:     
                    print "Your blood pressure is normal.",bps,"over",bpd

                if 120<bps<139 or 80<bpd<89:
                    print "Prehypertension.",bps,"over",bpd
                    print

                if 140<bps<170 or 90<bpd<105:
                    print "You have high blood pressure.",bps,"over",bpd
                    print
                                    
                if 175<bps<185 or 108<bpd<115:
                    print "Hypertensive Crisis!You will be admitted in the Hamad Hospital right away!",bps,"over",bpd
                    print "Please intake this tablet I'll be giving you immediately and lie down here. It is a capsule of 'captopril'.\nYou will be admitted in the AlKhor hospital for 5days at least"
                    print

                print"Now proceed onto meeting the doctor"
                print


                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 490
                y_coord = 93



                

            #Go for "Meet the Doctor"

                
            if x_coord in range (489,641) and y_coord in range(92,103):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                print"The doctors on duty are:"
                print"1. Dr. Anthony Amato, MD"
                print"2. Dr. Roger Spencer, MD"
                print"3. Dr. Adele O'Sullivan, MD "
                print"4. Dr. Robert Flores, MD"
                print
                choice=raw_input("Enter your preferred doctor's name:")
                print"Then please proceed to room number",random.randrange(102,106)
                print "Hello there! I'm ",choice
                print
                print "What happened?"
                print "1.Cold and cough?"
                print "2.Fever?"
                print "3.Sprain?"
                print "4.Pain?"
                e=input("What happened?")
                if (e==1):
                    print "Collect Paracetamol from the Pharmacy which is to be taken thrice a day every 8 hours.\n"
                    z=raw_input("Are you getting any pain?(Yes/No)")
                    if z=="Yes":
                        print "1.Stomach ache?"
                        print "2.Headache?"
                        print "3.Knee pain?"
                        print "4.Ear pain?"
                        print "5.Throat pain?"
                        p=input("What type of pain are you getting?")
                        print "Please collect Panadol strip from the Pharmacy\n"                 
                        print "Take care and Eat Healthy :)"


                              
                    else:
                        print "Okay then, please proceed to the pharmacy and buy the prescribed medicine.\n"
                        print "Take care and Eat Healthy :)"

                          
                if (e==2):
                    print "Collect Adol from the Pharmacy which is to be taken after dinner for 3 days.\n"
                    z=raw_input("Are you having any kinds of pain?(Yes/No)")
                    if z=="Yes":
                        print "1.Stomach ache?"
                        print "2.Headache?"
                        print "3.Knee pain?"
                        print "4.Ear pain?"
                        print "5.Throat pain?"
                        p=input("What type of pain are you getting?")
                        print "Please collect Panadol strip from the Pharmacy\n"
                        print "Take care and Eat Healthy :)"


                    else:
                        print "Okay then, please proceed to the pharmacy and buy the prescribed medicine\n"
                        print "Take care and Eat Healthy :)"


                      
                if (e==4):
                    print "1.Stomach ache?"
                    print "2.Headache?"
                    print "3.Knee pain?"
                    print "4.Ear pain?"
                    print "5.Throat pain?"
                    print "Okay then, please proceed to the pharmacy and buy the prescribed medicine"
                    print "Please collect Panadol strip and take 2 tablets a day every 12 hours for 2 days.\n"
                    print "Take care and Eat Healthy :)"



                if (e==3):
                    print "Please collect the following items from the pharmacy"
                    print "-Bandage \n-Sprain reliever cream \n-Panadol \n Put the bandage at the place where it hurts and apply some sprain reliever cream and if the pain is unbearable, take Panadol"
                    print "Take care and Eat Healthy :)"




                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 489
                y_coord = 132

            #Go to Pharmacy

            if x_coord in range (488,666) and y_coord in range(131,144):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                ab,bc,cd,de,ef,fg,gh,hi,ij,jk,kl,lm=0,0,0,0,0,0,0,0,0,0,0,0
                print "You have now entered the Pharmacy"
                print "The following are the medicines in the store"
                print"----------------------------------------------------------"
                print "      Item","                            Cost"            
                print"----------------------------------------------------------"
                print" "
                print" 1  Adol","                          Qr25 per bottle"  
                print" 2  Panadol","                       Qr10 per strip"  
                print" 3  Parcetamol","                    Qr20 per bottle"    
                print" 4  Lamisil(15g/tube)","             Qr30 per tube" 
                print" 5  Muscadol","                      Qr15 per strip"
                print" 6  Thyroxine(100mg)","              Qr70 per bottle"
                print" 7  Feneli","                        Qr25 per tube"
                print" 8  Aspirin","                       Qr20 per strip"
                print" 9  Calcium tablets","               Qr40 per strip"
                print" 10 Vital Vitamin Supplement","      Qr45 per strip"               
                print" 11 Bandage","                       Qr20 per packet"
                print" 12 Aveeno(20g/tube)","              Qr20 per tube"
                print" "
                print"----------------------------------------------------------"
                a=input("How many items do you want to buy?")
                print
                for i in range(a):
                    x=input("Enter number:")
                    if x==1:
                        aa=input("How many bottles?")
                        ab=aa*25
                    if x==2:
                        bb=input("How many strips (each having 8 capsules)?")
                        bc=bb*10
                    if x==3:
                        cc=input("How many bottles?")
                        cd=cc*20
                    if x==5:
                        dd=input("How many strips (each having 6 capsules)?")
                        de=dd*15
                    if x==4:
                        ee=input("How many tubes?")
                        ef=ee*30
                    if x==6:
                        ff=input("How many bottles (each having 50 100mg tablets)?")
                        fg=ff*70
                    if x==7:
                        gg=input("How many tubes?")
                        gh=gg*25
                    if x==8:
                        hh=input("How many strips (each having 4 capsules)?")
                        hi=hh*20
                    if x==9:
                        ii=input("How many strips (each having 8 capsules)?")
                        ij=ii*40
                    if x==10:
                        jj=input("How mnay strips (each having 8 capsules)?")
                        jk=jj*45
                    if x==11:
                        kk=input("How many packets (each having 5 bandages)?")
                        kl=kk*20
                    if x==12:
                        ll=input("How many tubes?")
                        lm=ll*20
                    continue
                    print
                Total=ab+bc+cd+de+ef+fg+gh+hi+ij+jk+kl+lm
                print "Your Total Bill is QR.",Total



                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                

            #Go back to AKC Map
            if x_coord in range (488,671) and y_coord in range(169,184):
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()
                print "Sir, please pay your bill before you leave the clinic"
                print"You have to pay a total of",Total,"Rupees."
                apple=raw_input("Sir, How would you like to pay the bill?(Credit Card or Cash)")
                if apple.lower()=="credit card":
                    chkname=raw_input("Please enter your name:")
                    chkccardno=input("Sir, please enter your credit card number:")

                    file=open('Bank.Dat','r')
                    file2=open('Temp.Dat','w')
                    try:
                        while True:    
                            x=pickle.load(file)
                            if x[2]==chkccardno and x[0]==chkname.lower():
                                if Total<x[2]:
                                    print"You have successfully paid Qr",Total
                                    x[3]=x[3]-Total
                                    pickle.dump(x,file2)
                                else:
                                    print "Sir, you don't have sufficient money in your account"
                            else:
                                pickle.dump(x,file2)
                            

                    except EOFError:
                        file2.close()
                        file.close()
                        os.rename('Bank.Dat','Bank1.Dat')
                        os.rename('Temp.Dat','Bank.Dat')
                        os.remove('Bank1.Dat')

                        
                        pass
                if apple.lower()=="cash":
                    if Total<cash:
                        
                        cash=cash-Total
                    else:
                        print "Ah, you don't have enough cash. We're gonna have to cancel the order. Please withdraw money from bank and return."
                break







            pygame.init()
            size = [708,424]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Al Khor Community")
            done = False
            clock = pygame.time.Clock()
            x_coord = 0
            y_coord = 0

            #Displaying the Home Screen(Medical Centre)            
            background=pygame.image.load('medical.jpg')
            screen.blit(background,(0,0))
            pygame.display.flip()
            clock.tick(30)







    #Entering the Shop
        
    if x_coord in range (67,187) and y_coord in range(49,161):
        Sum3,Sum,Sum2,Sum4,Sum1=0,0,0,0,0
        width,height=794,539
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Loading')
        background=pygame.image.load('load1.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1500)
        pygame.display.flip()
        clock.tick(30)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()
       

        
        pygame.init()
        width,height=888,491
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Shopping Centre')
        done = False
        clock = pygame.time.Clock()
        # Current position
        x_coord = 0
        y_coord = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]
                
            #Go to Accessories Shop
            if x_coord in range (627,865) and y_coord in range(79,101):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                
                
                Som,Sam,Lgm,Pam,Tom=0,0,0,0,0
                l3=[]
                print "------------------------------------------------------------"
                print "Item","                  ","Price","            ","Brand NO."
                print "------------------------------------------------------------"
                print
                print" 1. Gloves","         ","RS 50","               ","401"
                print" 2. Bag","            ","RS 100","              ","402"
                print" 3. Belt","           ","RS 120 ","             ","403"
                print" 4. Jewellery ","     ","RS 7000","             ","404"
                print" 5. Sun Glasses","    ","RS 700","              ","405"
                print
                n3=input("Enter how many items you want to buy")
                for i in range(n3):
                    if i==0:
                        cm=input("Enter the  Brand No.")
                    if i!=0:
                        cm=input("Enter the  Brand No. for the next item")
                    l3.append(cm)
                    if cm==401:
                        q=input("Enter how many pieces")
                        Som=q*50
                    if cm==402:
                        r=input("Enter how many pieces")
                        Sam=r*100
                    if cm==403:
                        t=input("Enter how many pieces")
                        Lgm=t*120
                    if cm==404:
                        y=input("Enter how many pieces")
                        Pam=y*7000
                    if cm==405:
                        u=input("Enter how many pieces")
                        Tom=u*700
                Sum3=Som+Sam+Lgm+Pam+Tom
                print Sum3,"is your bill for the Accessories section"
                print"Your final bill will be provided later"

                
                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #Go to Cinema Theater
            if x_coord in range (630,850) and y_coord in range(117,134):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()


                Tran,pop,cold,popcold,noth,Daw,Dho,Om,Sin=0,0,0,0,0,0,0,0,0
                Sum=0
                print"Welcome to Poojan Cinema Hall"
                print"Here is the list of some of the latest movies"
                print"1. Transformers: Age of Extinction in 3D","      ","RS 200"
                print"2. Dawn of the Planet of the Apes","             ","RS 300"
                print"3. Dhoom 3","                                    ","RS 500"
                print"4. Om Shanti Om","                               ","RS 350"
                print"5. Singham Returns","                            ","RS 300"
                    
                bm=input("Enter your choice(number)")
                if bm==1:
                    print"WELCOME"
                    print"Enjoy the movie"
                    print
                    print
                    po=input("Enter how many members")
                    
                    print"Sir, Do you want popcorn or colddrink"
                    print"It will cost RS 100 each"
                            
                    s=raw_input("Enter your requirement(Popcorn/Cold drink/Both/None")
                            
                    if s.lower()=="popcorn":
                        pop=pop+100
                    if s.lower()=="cold drink":
                        cold=cold+100
                    if s.lower()=="both":
                        popcold=popcold+200
                    if s.lower()=="none":
                        noth=noth+0
                    Tran=200*po+pop+cold+popcold+noth
                            
                    print Tran,'is your bill from Cinema Section'
                        
                if bm==2:
                    print"WELCOME"
                    print"Enjoy the movie"
                    print
                    print
                    po=input("Enter how many members")
                    print"Sir, Do you want popcorn or colddrink"
                    print"It will cost RS 100 each"
                          
                    s=raw_input("Enter your requirement(Popcorn/Cold drink/Both/None")
                            
                    if s.lower()=="popcorn":
                        pop=pop+100
                    if s.lower()=="cold drink":
                        cold=cold+100
                    if s.lower()=="both":
                        popcold=popcold+200
                    if s.lower()=="none":
                        noth=noth+0
                    Daw=300*po+pop+cold+popcold+noth
                    print Daw,'is your bill from Cinema Section'
                       
                    
                if bm==3:
                        
                    print"WELCOME"
                    print"Enjoy the movie"
                    print
                    print
                    po=input("Enter how many members")
                    print"Sir, Do you want popcorn or colddrink"

                    print"It will cost RS 100 each"

                    s=raw_input("Enter your requirement(Popcorn/Cold drink/Both/None")
                            
                    if s.lower()=="popcorn":
                        pop=pop+100
                    if s.lower()=="cold drink":
                        cold=cold+100
                    if s.lower()=="both":
                        popcold=popcold+200
                    if s.lower()=="none":
                        noth=noth+0
                    print Dho,'is your bill from Cinema Section'
                        
                if bm==4:
                        
                    print"WELCOME"
                    print"Enjoy the movie"

                    print
                    print
                    po=input("Enter how many members")
                    print"Sir, Do you want popcorn or colddrink"
                    print"It will cost RS 100 each"
                    s=raw_input("Enter your requirment")
                    s=raw_input("Enter your requirement(Popcorn/Cold drink/Both/None")
                            
                    if s.lower()=="popcorn":
                        pop=pop+100
                    if s.lower()=="cold drink":
                        cold=cold+100
                    if s.lower()=="both":
                        popcold=popcold+200
                    if s.lower()=="none":
                        noth=noth+0
                    Om=350*po+pop+cold+popcold+noth
                    print Om,'is your bill from Cinema Section'
                        
                if bm==5:
                        
                    print"WELCOME"
                    
                    print"Enjoy the movie"
                    print
                        
                    print
                    po=input("Enter how many members")
                    print"Sir, Do you want popcorn or colddrink"
                    print"It will cost RS 100 each"
                    s=raw_input("Enter your requirement(Popcorn/Cold drink/Both/None)")
                            
                    if s.lower()=="popcorn":
                        pop=pop+100
                    if s.lower()=="cold drink":
                        cold=cold+100
                    if s.lower()=="both":
                        popcold=popcold+200
                    if s.lower()=="none":
                        noth=noth+0
                    Sin=300*po+pop+cold+popcold+noth
                    print Sin,'is your bill from Cinema Section'
                    
                Sum=Tran+Daw+Dho+Om+Sin
                print
                print
                print
                print
                print
                print

                print Sum ,"is the final bill from the cinema section"

                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                
                
            #Go to Textile Shop
            if x_coord in range (629,805) and y_coord in range(155,173):
                
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()


                Sop,Sap,Lgp,Pap,Top=0,0,0,0,0
                l2=[]
                print "------------------------------------------------------------"
                print "Item","                  ","Price","            ","Brand NO."
                print "------------------------------------------------------------"
                print
                print" 1. T-shirt","          ","RS 95","               ","301"
                print" 2. Skirt","            ","RS 90","               ","302"
                print" 3. Track Suit","       ","RS 120 ","             ","303"
                print" 4. Trousers","         ","RS 70","               ","304"
                print" 5. Jacket","           ","RS 70","               ","305"
                print
                n2=input("Enter how many items you want to buy")
                print
                for i in range(n2):
                    if i==0:
                        cm=input("Enter the Brand No. for the first item:")
                    if i!=0:
                        cm=input("Enter the Brand No. for the next item:")
                    l2.append(cm)
                    if cm==301:
                        q=input("Enter how many pieces")
                        Sop=q*95
                    if cm==302:
                        r=input("Enter how many pieces")
                        Sap=r*90
                    if cm==303:
                        t=input("Enter how many pieces")
                        Lgp=r*120
                    if cm==304:
                        y=input("Enter how many pieces")
                        Pap=y*70
                    if cm==305:
                        u=input("Enter how many pieces")
                        Top=u*70
                Sum2=Sop+Sap+Lgp+Pap+Top
                print Sum2,"is your bill for the Clothes section"
                print
                print"Your final bill will be provided later"

                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                
            #Go to Electronics Shop
            if x_coord in range (630,862) and y_coord in range(188,210):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                So,Sa,Lg,Pa,To,S,Wh,Ro,Sam,No=0,0,0,0,0,0,0,0,0,0
                Sum4=0
                print "                        Welcome to the Electronics Section"
                l=[]
                print
                print


                print "Item","                  ","Price","            ","Brand No.","      ","      " ,"Warranty"
                print
                print
                print" 1.Sony Television","       ","RS 50,000","      ","101","            ","       ","2 years"
                print" 2.Samsung Television","    ","RS 60,000","      ","102","            ","       ","2.5 years"
                print" 3.LG Television","         ","RS 65,000 ","     ","103","            ","       ","2 years"
                print" 4.Panasonic Television","  ","RS 61,000","      ","104","            ","       ","3 years"
                print" 5.Toshiba Television","    ","RS 67,000","      ","105","            ","       ","5 years"
                print" 6.Samsung Refrigerator","  ","RS 75,000","      ","106","            ","       ","7 years"
                print" 7.Whirlpool Refrigerator"" ","RS 1,00,000","    ","107","            ","       ","8 years"
                print" 8.Rowenta Advancer Iron""  ","RS 40,000","      ","108","            ","       ","3 years"
                print" 9.Samamsung Galaxy NOTE 2""","RS 60,000","    ","  109","            ","       ","3 years"
                print" 10. Nokia N73 ","          ","RS 35000","     ","  110","            ","       ","5 years"
                print" "

                n=input("Enter how many items you want to buy")
                for i in range(n):
                    if i==0:
                        cm=input("Enter the Brand No. for the first item:")
                    if i!=0:
                        cm=input("Enter the Brand No. for the next item:")
                    l.append(cm)
                    if cm==101:
                        q=input("Enter how many pieces")
                        So=q*50000
                    if cm==102:
                        t=input("Enter how many pieces")
                        Sa=t*60000
                    if cm==103:
                        r=input("Enter the number of pieces")
                        Lg=r*65000
                    if cm==104:
                        y=input("Enter how many pieces")
                        Pa=y*61000
                    if cm==105:
                        u=input("Enter how many pieces")
                        To=u*67000
                    if cm==106:
                        i=input("Enter how many pieces")
                        S=i*75000
                    if cm==107:
                        o=input("Enter how many pieces")
                        Wh=o*100000
                    if cm==108:
                        p=input("Enter how many pieces")
                        Ro=p*40000
                    if cm==109:
                        lo=input("Enter how many pieces")
                        Sam=lo*60000
                    if cm==110:
                        mp=input("Enter how many pieces")
                        No=mp*35000
                        continue
                print
                print
                print
                        
                Sum4=So+Sa+Lg+Pa+To+S+Wh+Ro+Sam+No
                print Sum4,"is your bill for the electronics section"
                print
                print
                print"Your final bill will be provided later"

                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0                

            #Go to Grocery Shop
            if x_coord in range (630,823) and y_coord in range(231,248):
                width,height=813,601
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('load5.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(1500)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                Soa,Saa,Lga,Paa,Toa,Sa,Wha,Roa,Sama,Noa=0,0,0,0,0,0,0,0,0,0
                l1=[]
                print "-----------------------------------------------------------"
                print "       Item","             ","    Price","      ","  Item Code."
                print "-----------------------------------------------------------"
                print" 1.  Alphonso Mango","     "," RS 35 per piece","  "," 201"
                print" 2.  Watermelon","          ","RS 60 per kg","     "," 202"
                print" 3.  Peach","               ","RS 20 per kg ","    "," 203"
                print" 4.  Green Grapes","        ","RS 60 per kg","     "," 204"
                print" 5.  Black Grapes","        ","RS 67 per kg","     "," 205"
                print" 6.  Carrot","              ","RS 75 per kg","    ","  206"
                print" 7.  Musk melon""           ","RS 100 per piece","","  207"
                print" 8.  Orange","              ","RS 10 per piece","","   208"
                print" 9.  Lemon                ""","RS 5 per piece","","    209"
                print" 10. Raddish ","          ","  RS 10 per piece","","   210"
                print" "
                    
                n1=input("Enter how many items you want to buy")
                print
                for i in range(n1):
                    if i==0:
                        cm=input("Enter the Item Code for the first item:")
                    if i!=0:
                        cm=input("Enter the Item Code for the next item:")
                    l1.append(cm)
                    if cm==201:
                        q=input("Enter how many pieces")
                        Soa=q*35
                    if cm==202:
                        r=input("Enter how many kg")
                        Saa=r*60
                    if cm==203:
                        t=input("Enter how many kg")
                        Lga=t*20
                    if cm==204:
                        y=input("Enter how many kg")
                        Paa=y*60
                    if cm==205:
                        u=input("Enter how many kg")
                        Toa=u*67
                    if cm==206:
                        i=input("Enter how many kg")
                        Sa=i*75
                    if cm==207:
                        o=input("Enter how many pieces")
                        Wha=o*100
                    if cm==208:
                        p=input("Enter how many pieces")
                        Roa=p*10
                    if cm==209:
                        lo=input("Enter how many pieces")
                        
                        Sama=lo*5
                    if cm==210:
                        mpa=input("Enter how many pieces")
                        Noa=mpa*10
                        continue
                print
                print
                print
                Sum1=Soa+Saa+Lga+Paa+Toa+Sa+Wha+Roa+Sama+Noa
                print Sum1,"is your bill for the Grocery Section"

                print
                print "Thank You"                

                pygame.init()
                size = [888,491]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #Go back to AKC Map
            if x_coord in range (630,850) and y_coord in range(268,287):
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()
                print
                Final=Sum3+Sum+Sum2+Sum4+Sum1
                print"Thanks for Shopping at Al Khor Community Shopping Centre"
                print"Your final bill is",Final
                apple=raw_input("Sir, How would you like to pay the bill?(Credit Card or Cash)")
                if apple.lower()=="credit card":
                    chkname=raw_input("Please enter your name:")
                    chkccardno=input("Sir, please enter your credit card number:")

                    file=open('Bank.Dat','r')
                    file2=open('Temp.Dat','w')
                    try:
                        while True:    
                            x=pickle.load(file)
                            if x[2]==chkccardno and x[0]==chkname.lower():
                                if Final<x[2]:
                                    print"You have successfully paid Qr",Final
                                    x[3]=x[3]-Final
                                    pickle.dump(x,file2)
                                else:
                                    print "Sir, you don't have sufficient money in your account"
                            else:
                                pickle.dump(x,file2)
                            

                    except EOFError:
                        file2.close()
                        file.close()
                        os.rename('Bank.Dat','Bank1.Dat')
                        os.rename('Temp.Dat','Bank.Dat')
                        os.remove('Bank1.Dat')
                        
                        pass
                if apple.lower()=="cash":
                    if Final<cash:
                        
                        cash=cash-Final
                    else:
                        print "Ah, you don't have enough cash. We're gonna have to cancel the order. Please withdraw money from bank and return."

                    
                break #To come back to AKC Map







            pygame.init()
            size = [888,491]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Al Khor Community")
            done = False
            clock = pygame.time.Clock()
            x_coord = 0
            y_coord = 0
            #Displaying the Home Screen(Shop)            
            background=pygame.image.load('Shop.jpg')
            screen.blit(background,(0,0))
            pygame.display.flip()
            clock.tick(30)








    #Entering Club 1
        
    if x_coord in range (290,401) and y_coord in range(54,163):
        width,height=794,539
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Loading')
        background=pygame.image.load('load1.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1500)
        pygame.display.flip()
        clock.tick(30)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()


        a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
        pygame.init()
        pygame.mixer.music.load('Hotel.wav')
        pygame.mixer.music.play()
        width,height=708,424
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Restaurant')
        done = False
        clock = pygame.time.Clock()
        # Current position
        x_coord = 0
        y_coord = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]




            #1
            if x_coord in range (109,128) and y_coord in range(178,195):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Chicken Noodle Soup"
                a=a+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
            #2        
            if x_coord in range (131,149) and y_coord in range(226,242):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Caesar Salad"
                b=b+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
            #3        
            if x_coord in range (96,114) and y_coord in range(271,289):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Chicken Caesar Wrap"
                c=c+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
            #4        
            if x_coord in range (134,152) and y_coord in range(320,336):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Beef Lasagna"
                d=d+1
                
                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
            #5
            if x_coord in range (135,154) and y_coord in range(369,387):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Baked Ravioli"
                e=e+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #6
            if x_coord in range (133,151) and y_coord in range(414,430):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Cheeseburger"
                f=f+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #7
            if x_coord in range (155,174) and y_coord in range(461,477):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Tiramisu"
                g=g+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #8
            if x_coord in range (131,149) and y_coord in range(507,523):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Cafe Con Leche"
                h=h+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

            #9
            if x_coord in range (111,129) and y_coord in range(554,570):
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0

                print "You have ordered 1 Fresh Orange Juice"
                i=i+1
                

                size = [700,685]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("Al Khor Community")
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
            if x_coord in range (500,683) and y_coord in range(535,628):
                done = False
                pygame.mixer.music.stop()
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()
                print
                print "******************************************************************************"
                print "Item                             Quantity                    Price"
                print "******************************************************************************"
                for menu in range(1,10):
                    if menu==1:
                       print "Chicken Noodle Soup","               ",a,"                        ",14*a
                    if menu==2:
                       print "Caesar Salad","                      ",b,"                        ",18*b
                    if menu==3:
                       print "Chicken Caesar Wrap","               ",c,"                        ",20*c
                    if menu==4:
                       print "Beef Lasagna","                      ",d,"                        ",24*d
                    if menu==5:
                       print "Baked Ravioli","                     ",e,"                        ",28*e
                    if menu==6:
                       print "Cheeseburger","                      ",f,"                        ",15*f 
                    if menu==7:
                       print "Tiramisu","                          ",g,"                        ",12*g 
                    if menu==8:
                       print "Cafe Con Leche","                    ",h,"                        ",8*h
                    if menu==9:
                       print "Fresh Orange Juice","                ",i,"                        ",10*i
                       Final2=(14*a)+(18*b)+(20*c)+(24*d)+(28*e)+(15*f)+(12*g)+(8*h)+(10*i)
                       print "------------------------------------------------------------------------------"
                       print "Grand Total =",Final2,"Riyals"
                       print "------------------------------------------------------------------------------"

                Final2=(14*a)+(18*b)+(20*c)+(24*d)+(28*e)+(15*f)+(12*g)+(8*h)+(10*i)
                print"Your final bill is",Final2
                apple=raw_input("Sir, How would you like to pay the bill?(Credit Card or Cash)")
                if apple.lower()=="credit card":
                    chkname=raw_input("Please enter your name:")
                    chkccardno=input("Sir, please enter your credit card number:")

                    file=open('Bank.Dat','r')
                    file2=open('Temp.Dat','w')
                    try:
                        while True:    
                            x=pickle.load(file)
                            if x[2]==chkccardno and x[0]==chkname.lower():
                                if Final2<x[2]:
                                    print"You have successfully paid Qr",Final2
                                    x[3]=x[3]-Final2
                                    pickle.dump(x,file2)
                                else:
                                    print "Sir, you don't have sufficient money in your account"
                            else:
                                pickle.dump(x,file2)
                            

                    except EOFError:
                        file2.close()
                        file.close()
                        os.rename('Bank.Dat','Bank1.Dat')
                        os.rename('Temp.Dat','Bank.Dat')
                        os.remove('Bank1.Dat')
                        
                        pass
                if apple.lower()=="cash":
                    if Final2<cash:
                        
                        cash=cash-Final2
                    else:
                        print "Ah, you don't have enough cash. We're gonna have to cancel the order. Please withdraw money from bank and return."



                pygame.init()
                width,height=560,420
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Loading')
                background=pygame.image.load('dinerdash1.jpg')
                screen.blit(background,(0,0))
                pygame.display.flip()
                clock.tick(30)
                pygame.time.wait(2000)
                pygame.display.flip()
                clock.tick(30)
                done = False
                clock = pygame.time.Clock()
                x_coord = 0
                y_coord = 0
                pygame.display.flip()
                clock.tick(30)
                pygame.quit()

                        
                       
                break
                        
                


            pygame.init()
            size = [700,685]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Al Khor Community")
            done = False
            clock = pygame.time.Clock()
            x_coord = 0
            y_coord = 0
            #Displaying the Menu Card           
            background=pygame.image.load('menu1.jpg')
            screen.blit(background,(0,0))

                        
            pygame.display.flip()
            clock.tick(30)






    #Entering Club 2
        
    if x_coord in range (151,259) and y_coord in range(260,370):

        #Magic Gopher
        list=[1,2,3,4,5]
        f=0

        width,height=1084,669
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Magic Gopher')
        background=pygame.image.load('MM.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1700)
        pygame.display.flip()
        clock.tick(90)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(90)
        pygame.quit()

        #Screen 1 
        pygame.init()

        width,height=1084,669
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Magic Gopher')

        pygame.mixer.music.load('MagicS.wav')
        pygame.mixer.music.play()
        done = False
        clock = pygame.time.Clock()
        # Current position
        x_coord = 0
        y_coord = 0

        while not done:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]

            #Option/Box 1   
            if x_coord in range (835,874) and y_coord in range(357,397):

                x_coord = 2
                y_coord = 5

                
                if list==[]:
                    list=list+[1,2,3,4]
                    
                rad=random.sample(list,1)
                for i in rad:
                    b=i
                    list.remove(b)
                    

                a=0
            if f==1:
                break
            
            if x_coord in range (1,16) and y_coord in range(4,14):
                
                #Screen 2
                


                width,height=1084,669
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Magic Gopher')

                done = False
                clock = pygame.time.Clock()
                # Current position
                x_coord = 0
                y_coord = 0

                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            x_coord=pos[0]
                            y_coord=pos[1]
                            
                    #Option/Box 1   
                    if x_coord in range (835,874) and y_coord in range(357,397):


                        x_coord = 2
                        y_coord = 5

               
                        
                    if a==1 or f==1:
                        break
    
                    if x_coord in range (1,16) and y_coord in range(4,14):
                        
                        #Screen 3
                        

                        width,height=1084,669
                        screen=pygame.display.set_mode((width,height))
                        pygame.display.set_caption('Magic Gopher')

                        done = False
                        clock = pygame.time.Clock()
                        # Current position
                        x_coord = 0
                        y_coord = 0

                        while not done:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    done = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos=pygame.mouse.get_pos()
                                    x_coord=pos[0]
                                    y_coord=pos[1]
                                    
                            #Option/Box 1   
                            if x_coord in range (835,874) and y_coord in range(357,397):


                                x_coord = 2
                                y_coord = 5


                                
                            if a==1 or f==1:
                                break
                    
                            if x_coord in range (1,16) and y_coord in range(4,14):
                                
                            
                                width,height=1084,669
                                screen=pygame.display.set_mode((width,height))
                                pygame.display.set_caption('Magic Gopher')

                                done = False
                                clock = pygame.time.Clock()
                                # Current position
                                x_coord = 0
                                y_coord = 0

                                while not done:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            done = True
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos=pygame.mouse.get_pos()
                                            x_coord=pos[0]
                                            y_coord=pos[1]
                                            
                                    #Option/Box 1   
                                    if x_coord in range (835,874) and y_coord in range(357,397):


                                        x_coord = 2
                                        y_coord = 5
                                        


                                    if a==1 or f==1:
                                        break
                                        
                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                        

                                        width,height=1084,669
                                        screen=pygame.display.set_mode((width,height))
                                        pygame.display.set_caption('Guess Artist')

                                        done = False
                                        clock = pygame.time.Clock()
                                        # Current position
                                        x_coord = 0
                                        y_coord = 0

                                        while not done:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    done = True
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    pos=pygame.mouse.get_pos()
                                                    x_coord=pos[0]
                                                    y_coord=pos[1]
                                                    
                                            #Option/Box 1   
                                            if x_coord in range (890,955) and y_coord in range(359,424):


                                                x_coord = 2
                                                y_coord = 5

                                            if a==1 or f==1:
                                                break
                                                                                                

                                        
                                            if x_coord in range (1,16) and y_coord in range(4,14):
                                                pygame.mixer.music.stop()
                                                width,height=1084,669
                                                screen=pygame.display.set_mode((width,height))
                                                pygame.display.set_caption('Magic Gopher')
                                                background=pygame.image.load('M12.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(90)
                                                pygame.time.wait(2000)
                                                pygame.display.flip()
                                                clock.tick(30)
                                                done = False
                                                clock = pygame.time.Clock()
                                                x_coord = 0
                                                y_coord = 0



                                                                                        
                                                #Magic Result Display Screen

                                                width,height=1084,669
                                                screen=pygame.display.set_mode((width,height))
                                                pygame.display.set_caption('Magic Gopher')
                                                pygame.mixer.music.load('Chandlier.wav')
                                                pygame.mixer.music.play()
                                                done = False
                                                clock = pygame.time.Clock()
                                                # Current position
                                                x_coord = 0
                                                y_coord = 0

                                                while not done:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            done = True
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            pos=pygame.mouse.get_pos()
                                                            x_coord=pos[0]
                                                            y_coord=pos[1]
                                                            
                                                    #Hitting the Try Again option   
                                                    if x_coord in range (832,962) and y_coord in range(600,636):


                                                        x_coord = 2
                                                        y_coord = 5
                                                    

                                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                                        pygame.mixer.music.stop()
                                                        pygame.time.wait(1000)
                                                        pygame.mixer.music.load('MagicS.wav')
                                                        pygame.mixer.music.play()                                                        
                                                        a=1
                                                        break
                                                    
                                                    #Exit the Magic Gopher
                                                    if x_coord in range (0,101) and y_coord in range(629,669): 
                                                        pygame.mixer.music.stop()

                                                        f=1
                                                        break
                                                                                                        
                                                        
                                                               
                                                    #Round 6 Screen
                                                    pygame.init()
                                                    size = [1084,669]
                                                    screen = pygame.display.set_mode(size)
                                                    pygame.display.set_caption("Al Khor Community")
                                                    done = False
                                                    clock = pygame.time.Clock()
                                                    x_coord = 0
                                                    y_coord = 0
                                                    #Displaying the Round 3 Screen
                                                    if b==1:
                                                        
                                                        background=pygame.image.load('M6.jpg')
                                                        screen.blit(background,(0,0))
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                    if b==2:
                                                        
                                                        background=pygame.image.load('M8.jpg')
                                                        screen.blit(background,(0,0))
                                                        pygame.display.flip()
                                                        clock.tick(30)                                               
                                                    if b==3:
                                                        
                                                        background=pygame.image.load('M10.jpg')
                                                        screen.blit(background,(0,0))
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                    if b==4:
                                                        
                                                        background=pygame.image.load('M14.jpg')
                                                        screen.blit(background,(0,0))
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                        
                                                    if b==5:
                                                        
                                                        background=pygame.image.load('M16.jpg')
                                                        screen.blit(background,(0,0))
                                                        pygame.display.flip()
                                                        clock.tick(30)  
                                                        
                                            
                                            #Round 5 Screen
                                            pygame.init()
                                            size = [1084,669]
                                            screen = pygame.display.set_mode(size)
                                            pygame.display.set_caption("Al Khor Community")
                                            done = False
                                            clock = pygame.time.Clock()
                                            x_coord = 0
                                            y_coord = 0
                                            #Displaying the Round 3 Screen
                                            if b==1:
                                                
                                                background=pygame.image.load('M5.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(30)
                                            if b==2:
                                                
                                                background=pygame.image.load('M7.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(30)                                               
                                            if b==3:
                                                
                                                background=pygame.image.load('M9.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(30)
                                            if b==4:
                                                
                                                background=pygame.image.load('M11.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(30)
                                                
                                            if b==5:
                                                
                                                background=pygame.image.load('M15.jpg')
                                                screen.blit(background,(0,0))
                                                pygame.display.flip()
                                                clock.tick(30)                                                  
                                    #Round 4 Screen
                                    pygame.init()
                                    size = [1084,669]
                                    screen = pygame.display.set_mode(size)
                                    pygame.display.set_caption("Al Khor Community")
                                    done = False
                                    clock = pygame.time.Clock()
                                    x_coord = 0
                                    y_coord = 0
                                    #Displaying the Round 3 Screen            
                                    background=pygame.image.load('M4.jpg')
                                    screen.blit(background,(0,0))
                                    pygame.display.flip()
                                    clock.tick(30)    


                                
                            #Round 3 Screen
                            pygame.init()
                            size = [1084,669]
                            screen = pygame.display.set_mode(size)
                            pygame.display.set_caption("Al Khor Community")
                            done = False
                            clock = pygame.time.Clock()
                            x_coord = 0
                            y_coord = 0
                            #Displaying the Round 3 Screen            
                            background=pygame.image.load('M3.jpg')
                            screen.blit(background,(0,0))
                            pygame.display.flip()
                            clock.tick(30)                                
                                

                    #Round 2 Screen
                    pygame.init()
                    size = [1084,669]
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("Al Khor Community")
                    done = False
                    clock = pygame.time.Clock()
                    x_coord = 0
                    y_coord = 0
                    #Displaying the Round 2 Screen            
                    background=pygame.image.load('M2.jpg')
                    screen.blit(background,(0,0))
                    pygame.display.flip()
                    clock.tick(30)

                



            #Round 1 Screen
            pygame.init()
            size = [1084,669]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Al Khor Community")
            done = False
            clock = pygame.time.Clock()
            x_coord = 0
            y_coord = 0
            #Displaying the Round 1 Screen            
            background=pygame.image.load('M1.jpg')
            screen.blit(background,(0,0))
            pygame.display.flip()
            clock.tick(30)






    #Entering Bank
        
    if x_coord in range (61,172) and y_coord in range(421,524):
        width,height=794,539
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Loading')
        background=pygame.image.load('load1.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1500)
        pygame.display.flip()
        clock.tick(30)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()

        
        pygame.init()


        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]

            loop=1
            while loop==1:
                print "The options are:"
                print "1. Make a new credit card"
                print "2. Withdraw money"
                print "3. Check balance"
                print "4. Exit Bank"
                bankchoice=input("Enter your choice:")
                if bankchoice==1:
                    blist=[]
                    file=open("Bank.Dat",'a')
                    bname=raw_input("Sir, please enter your name:")
                    bage=input("Please enter your age:")
                    credit=2000
                    creditcardno=input("Please enter a 4 digit number to be chosen as your credit card no:")
                    if creditcardno==0000 and bname.lower()=='admin':
                        credit=100000
                    blist.append(bname.lower())
                    blist.append(bage)
                    blist.append(creditcardno)
                    blist.append(credit)
                    pickle.dump(blist,file)
                    file.close()
                    print "Congratulations, your credit has been successfully made. We're gonna add a credit of Qr",credit,"into your credit card. Happy Shopping"
                if bankchoice==2:
                    chkname=raw_input("Please enter your name:")
                    chkccardno=input("Sir, please enter your credit card number:")

                    

                    file=open('Bank.Dat','r')
                    file2=open('Temp.Dat','w')
                    try:
                        while True:    
                            x=pickle.load(file)
                            if x[2]==chkccardno and x[0]==chkname.lower():
                                cash2=input("How much money would you like to withdraw?")
                                if cash2<x[2]:
                                    print"You have successfully withdrawn Qr",cash2
                                    x[3]=x[3]-cash2
                                    cash=cash+cash2
                                    pickle.dump(x,file2)
                                else:
                                    print "Sir, you don't have sufficient money in your account"
                            else:
                                pickle.dump(x,file2)
                            

                    except EOFError:
                        file2.close()
                        file.close()
                        os.rename('Bank.Dat','Bank1.Dat')
                        os.rename('Temp.Dat','Bank.Dat')
                        os.remove('Bank1.Dat')


                        
                        pass
                    
                if bankchoice==3:
                    chkname=raw_input("Please enter your name:")
                    chkccardno=input("Sir, please enter your credit card number:")

                    file=open('Bank.Dat','r')
                    try:
                        while True:    
                            x=pickle.load(file)
                            if x[2]==chkccardno and x[0]==chkname.lower():
                                print "You have a total of",x[3],"in your account"
                                done=0
                            

                    except EOFError:
                        if done!=0:
                            print "Sir, you did not enter a valid credit card number"
                        file.close()
                        pass

                if bankchoice==4:
                    print "Thanks for visiting our Bank"
                    break
            x_coord=489
            y_coord=170

                    
         


            #Go back to AKC Map
            if x_coord in range (488,671) and y_coord in range(169,184):
                break





    #Entering Youth Club



        
    if x_coord in range (83,235) and y_coord in range(583,691):
        #Songpop
        a=0
        score=0

        width,height=851,315
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Songpop')
        background=pygame.image.load('load1.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
        pygame.time.wait(1700)
        pygame.display.flip()
        clock.tick(30)
        done = False
        clock = pygame.time.Clock()
        x_coord = 0
        y_coord = 0
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()

        
        pygame.init()
        width,height=574,733
        screen=pygame.display.set_mode((width,height))
        pygame.display.set_caption('Playlist')
        done = False
        clock = pygame.time.Clock()
        # Current position
        x_coord = 0
        y_coord = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]

            #1. Today's Hits
                    
            if x_coord in range (23,546) and y_coord in range(216,298):
                
                #Song 1 - Sing(Ed Sheeran) 
                pygame.init()
                a=0
                score=0
                width,height=708,424
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Guess Artist')
                
                sound=pygame.mixer.Sound('Sing.wav')
                sound.play()
                done = False
                clock = pygame.time.Clock()
                # Current position
                x_coord = 0
                y_coord = 0

                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            x_coord=pos[0]
                            y_coord=pos[1]

                    #Option/Box 1   
                    if x_coord in range (72,405) and y_coord in range(312,406):
                        pygame.display.flip()
                        clock.tick(30)
                        pygame.quit()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5
                        
                    #Option/Box 2
                    if x_coord in range (439,777) and y_coord in range(313,403):
                        pygame.display.flip()
                        clock.tick(30)
                        pygame.quit()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5

                    #Option/Box 3                
                    if x_coord in range (73,407) and y_coord in range(442,536):
                        pygame.display.flip()
                        clock.tick(30)
                        pygame.quit()
                        score=score+1
                        print "Correct Answer"

                        x_coord = 2
                        y_coord = 5


                    #Option/Box 4
                    if x_coord in range (436,777) and y_coord in range(442,535):
                        pygame.display.flip()
                        clock.tick(30)
                        pygame.quit()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5     

                    if a==1:
                        break
                    
                    if x_coord in range (1,16) and y_coord in range(4,14):
                        
                        #Song 2 - Magic(Rude!)
                        
                        pygame.init()
                        width,height=708,424
                        screen=pygame.display.set_mode((width,height))
                        pygame.display.set_caption('Guess Artist')
                        sound=pygame.mixer.Sound('Magic.wav')
                        sound.play()
                        done = False
                        clock = pygame.time.Clock()
                        # Current position
                        x_coord = 0
                        y_coord = 0

                        while not done:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    done = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos=pygame.mouse.get_pos()
                                    x_coord=pos[0]
                                    y_coord=pos[1]
                                    
                            #Option/Box 1   
                            if x_coord in range (72,405) and y_coord in range(312,406):
                                pygame.display.flip()
                                clock.tick(30)
                                pygame.quit()
                                score=score+1
                                print "Correct Answer"
                                x_coord = 2
                                y_coord = 5
                                
                            #Option/Box 2
                            if x_coord in range (439,777) and y_coord in range(313,403):
                                pygame.display.flip()
                                clock.tick(30)
                                pygame.quit()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5

                            #Option/Box 3                
                            if x_coord in range (73,407) and y_coord in range(442,536):
                                pygame.display.flip()
                                clock.tick(30)
                                pygame.quit()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5


                            #Option/Box 4
                            if x_coord in range (436,777) and y_coord in range(442,535):
                                pygame.display.flip()
                                clock.tick(30)
                                pygame.quit()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5     
                       
                                
                            if a==1:
                                break

                            if x_coord in range (1,16) and y_coord in range(4,14):
                                
                                #Song 3 - Sweet Nothing(Calvin Harris)
                                
                                pygame.init()
                                width,height=708,424
                                screen=pygame.display.set_mode((width,height))
                                pygame.display.set_caption('Guess Artist')
                                sound=pygame.mixer.Sound('Sweet Nothing.wav')
                                sound.play()
                                done = False
                                clock = pygame.time.Clock()
                                # Current position
                                x_coord = 0
                                y_coord = 0

                                while not done:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            done = True
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos=pygame.mouse.get_pos()
                                            x_coord=pos[0]
                                            y_coord=pos[1]
                                            
                                    #Option/Box 1   
                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                        pygame.display.flip()
                                        clock.tick(30)
                                        pygame.quit()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5
                                        
                                    #Option/Box 2
                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                        pygame.display.flip()
                                        clock.tick(30)
                                        pygame.quit()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5

                                    #Option/Box 3                
                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                        pygame.display.flip()
                                        clock.tick(30)
                                        pygame.quit()
                                        score=score+1
                                        print "Correct Answer"
                                        x_coord = 2
                                        y_coord = 5


                                    #Option/Box 4
                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                        pygame.display.flip()
                                        clock.tick(30)
                                        pygame.quit()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5     

                                        
                                    if a==1:
                                        break
                            
                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                        
                                        #Song 4 - Pitbull(Tchu Tchu Tcha)
                                        
                                        pygame.init()
                                        width,height=708,424
                                        screen=pygame.display.set_mode((width,height))
                                        pygame.display.set_caption('Guess Artist')
                                        sound=pygame.mixer.Sound('Pitbull.wav')
                                        sound.play()
                                        done = False
                                        clock = pygame.time.Clock()
                                        # Current position
                                        x_coord = 0
                                        y_coord = 0

                                        while not done:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    done = True
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    pos=pygame.mouse.get_pos()
                                                    x_coord=pos[0]
                                                    y_coord=pos[1]
                                                    
                                            #Option/Box 1   
                                            if x_coord in range (72,405) and y_coord in range(312,406):
                                                pygame.display.flip()
                                                clock.tick(30)
                                                pygame.quit()
                                                score=score+1
                                                print "Correct Answer"
                                                x_coord = 2
                                                y_coord = 5
                                                
                                            #Option/Box 2
                                            if x_coord in range (439,777) and y_coord in range(313,403):
                                                pygame.display.flip()
                                                clock.tick(30)
                                                pygame.quit()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5

                                            #Option/Box 3                
                                            if x_coord in range (73,407) and y_coord in range(442,536):
                                                pygame.display.flip()
                                                clock.tick(30)
                                                pygame.quit()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5


                                            #Option/Box 4
                                            if x_coord in range (436,777) and y_coord in range(442,535):
                                                pygame.display.flip()
                                                clock.tick(30)
                                                pygame.quit()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5     


                                            if a==1:
                                                break
                                                
                                            if x_coord in range (1,16) and y_coord in range(4,14):
                                                
                                                #Song 5 - Bailando 
                                                pygame.init()
                                                width,height=708,424
                                                screen=pygame.display.set_mode((width,height))
                                                pygame.display.set_caption('Guess Artist')
                                                sound=pygame.mixer.Sound('Bailando.wav')
                                                sound.play()
                                                done = False
                                                clock = pygame.time.Clock()
                                                # Current position
                                                x_coord = 0
                                                y_coord = 0

                                                while not done:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            done = True
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            pos=pygame.mouse.get_pos()
                                                            x_coord=pos[0]
                                                            y_coord=pos[1]
                                                            
                                                    #Option/Box 1   
                                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                        pygame.quit()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5
                                                        
                                                    #Option/Box 2
                                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                        pygame.quit()
                                                        score=score+1
                                                        print "Correct Answer"
                                                        x_coord = 2
                                                        y_coord = 5

                                                    #Option/Box 3                
                                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                        pygame.quit()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5


                                                    #Option/Box 4
                                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                                        pygame.display.flip()
                                                        clock.tick(30)
                                                        pygame.quit()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5     

                                                
                                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                                        print "Your score is",score
                                                        print "We're gonna add a cash prize of Qr",score*100,"into your account"
                                                        chkname=raw_input("Please enter your name:")
                                                        chkccardno=input("Sir, please enter your credit card number:")

                                                        

                                                        file=open('Bank.Dat','r')
                                                        file2=open('Temp.Dat','w')
                                                        try:
                                                            while True:    
                                                                x=pickle.load(file)
                                                                if x[2]==chkccardno and x[0]==chkname.lower():
                                                                        x[3]=x[3]+(score*100)
                                                                        pickle.dump(x,file2)
                                                                else:
                                                                    pickle.dump(x,file2)
                                                                

                                                        except EOFError:
                                                            file2.close()
                                                            file.close()
                                                            os.rename('Bank.Dat','Bank1.Dat')
                                                            os.rename('Temp.Dat','Bank.Dat')
                                                            os.remove('Bank1.Dat')

                                                        

                                                                                                        
                                                        a=1                                                                                                           
                                                        break
                                                                
                                                    
                                                    #Round 5 Screen
                                                    pygame.init()
                                                    size = [819,644]
                                                    screen = pygame.display.set_mode(size)
                                                    pygame.display.set_caption("Al Khor Community")
                                                    done = False
                                                    clock = pygame.time.Clock()
                                                    x_coord = 0
                                                    y_coord = 0
                                                    #Displaying the Round 3 Screen            
                                                    background=pygame.image.load('Song2.jpg')
                                                    screen.blit(background,(0,0))
                                                    pygame.display.flip()
                                                    clock.tick(30)    

                                            #Round 4 Screen
                                            pygame.init()
                                            size = [819,644]
                                            screen = pygame.display.set_mode(size)
                                            pygame.display.set_caption("Al Khor Community")
                                            done = False
                                            clock = pygame.time.Clock()
                                            x_coord = 0
                                            y_coord = 0
                                            #Displaying the Round 3 Screen            
                                            background=pygame.image.load('Artist1.jpg')
                                            screen.blit(background,(0,0))
                                            pygame.display.flip()
                                            clock.tick(30)    


                                        
                                    #Round 3 Screen
                                    pygame.init()
                                    size = [819,644]
                                    screen = pygame.display.set_mode(size)
                                    pygame.display.set_caption("Al Khor Community")
                                    done = False
                                    clock = pygame.time.Clock()
                                    x_coord = 0
                                    y_coord = 0
                                    #Displaying the Round 3 Screen            
                                    background=pygame.image.load('Artist2.jpg')
                                    screen.blit(background,(0,0))
                                    pygame.display.flip()
                                    clock.tick(30)                                
                                        

                            #Round 2 Screen
                            pygame.init()
                            size = [819,644]
                            screen = pygame.display.set_mode(size)
                            pygame.display.set_caption("Al Khor Community")
                            done = False
                            clock = pygame.time.Clock()
                            x_coord = 0
                            y_coord = 0
                            #Displaying the Round 2 Screen            
                            background=pygame.image.load('Song1.jpg')
                            screen.blit(background,(0,0))
                            pygame.display.flip()
                            clock.tick(30)

                        



                    #Round 1 Screen
                    pygame.init()
                    size = [819,644]
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("Al Khor Community")
                    done = False
                    clock = pygame.time.Clock()
                    x_coord = 0
                    y_coord = 0
                    #Displaying the Round 1 Screen            
                    background=pygame.image.load('Artist1.jpg')
                    screen.blit(background,(0,0))
                    pygame.display.flip()
                    clock.tick(30)


            #2. Modern Rap
            if x_coord in range (24,549) and y_coord in range(311,389):

                
                #Song 1 - Black and Yellow(Wiz Khalifa)
                pygame.init()
                a=0
                score=0
                width,height=708,424
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Guess Artist')
                
                sound=pygame.mixer.Sound('BlackandYellow.wav')
                sound.play()
                done = False
                clock = pygame.time.Clock()
                # Current position
                x_coord = 0
                y_coord = 0

                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            x_coord=pos[0]
                            y_coord=pos[1]

                    #Option/Box 1   
                    if x_coord in range (72,405) and y_coord in range(312,406):
                        sound.stop()
                        score=score+1
                        print "Correct Answer"
                        x_coord = 2
                        y_coord = 5
                        
                    #Option/Box 2
                    if x_coord in range (439,777) and y_coord in range(313,403):
                        sound.stop()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5

                    #Option/Box 3                
                    if x_coord in range (73,407) and y_coord in range(442,536):
                        sound.stop()
                        print "Incorrect Answer"

                        x_coord = 2
                        y_coord = 5


                    #Option/Box 4
                    if x_coord in range (436,777) and y_coord in range(442,535):
                        sound.stop()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5     

                    if a==1:
                        break
                    
                    if x_coord in range (1,16) and y_coord in range(4,14):
                        
                        #Song 2 - Day n Nite(Kid Cudi)
                        

                        width,height=708,424
                        screen=pygame.display.set_mode((width,height))
                        pygame.display.set_caption('Guess Artist')
                        sound=pygame.mixer.Sound('DaynNite.wav')
                        sound.play()
                        done = False
                        clock = pygame.time.Clock()
                        # Current position
                        x_coord = 0
                        y_coord = 0

                        while not done:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    done = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos=pygame.mouse.get_pos()
                                    x_coord=pos[0]
                                    y_coord=pos[1]
                                    
                            #Option/Box 1   
                            if x_coord in range (72,405) and y_coord in range(312,406):
                                sound.stop()
                                score=score+1
                                print "Correct Answer"
                                x_coord = 2
                                y_coord = 5
                                
                            #Option/Box 2
                            if x_coord in range (439,777) and y_coord in range(313,403):
                                sound.stop()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5

                            #Option/Box 3                
                            if x_coord in range (73,407) and y_coord in range(442,536):
                                sound.stop()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5


                            #Option/Box 4
                            if x_coord in range (436,777) and y_coord in range(442,535):
                                sound.stop()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5     
                       
                                
                            if a==1:
                                break

                            if x_coord in range (1,16) and y_coord in range(4,14):
                                
                                #Song 3 - Love the way you lie(Eminem ft. Rihanna)
                                

                                width,height=708,424
                                screen=pygame.display.set_mode((width,height))
                                pygame.display.set_caption('Guess Artist')
                                sound=pygame.mixer.Sound('Eminem.wav')
                                sound.play()
                                done = False
                                clock = pygame.time.Clock()
                                # Current position
                                x_coord = 0
                                y_coord = 0

                                while not done:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            done = True
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos=pygame.mouse.get_pos()
                                            x_coord=pos[0]
                                            y_coord=pos[1]
                                            
                                    #Option/Box 1   
                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5
                                        
                                    #Option/Box 2
                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5

                                    #Option/Box 3                
                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                        sound.stop()
                                        score=score+1
                                        print "Correct Answer"
                                        x_coord = 2
                                        y_coord = 5


                                    #Option/Box 4
                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5     

                                        
                                    if a==1:
                                        break
                            
                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                        
                                        #Song 4 - How to Love(Lil Wayne)
                                        

                                        width,height=708,424
                                        screen=pygame.display.set_mode((width,height))
                                        pygame.display.set_caption('Guess Artist')
                                        sound=pygame.mixer.Sound('HTW.wav')
                                        sound.play()
                                        done = False
                                        clock = pygame.time.Clock()
                                        # Current position
                                        x_coord = 0
                                        y_coord = 0

                                        while not done:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    done = True
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    pos=pygame.mouse.get_pos()
                                                    x_coord=pos[0]
                                                    y_coord=pos[1]
                                                    
                                            #Option/Box 1   
                                            if x_coord in range (72,405) and y_coord in range(312,406):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5
                                                
                                            #Option/Box 2
                                            if x_coord in range (439,777) and y_coord in range(313,403):
                                                sound.stop()
                                                score=score+1
                                                print "Correct Answer"                                                

                                                x_coord = 2
                                                y_coord = 5

                                            #Option/Box 3                
                                            if x_coord in range (73,407) and y_coord in range(442,536):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5


                                            #Option/Box 4
                                            if x_coord in range (436,777) and y_coord in range(442,535):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5     


                                            if a==1:
                                                break
                                                
                                            if x_coord in range (1,16) and y_coord in range(4,14):
                                                
                                                #Song 5 - Power(Kanye West)

                                                width,height=708,424
                                                screen=pygame.display.set_mode((width,height))
                                                pygame.display.set_caption('Guess Artist')
                                                sound=pygame.mixer.Sound('Power.wav')
                                                sound.play()
                                                done = False
                                                clock = pygame.time.Clock()
                                                # Current position
                                                x_coord = 0
                                                y_coord = 0

                                                while not done:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            done = True
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            pos=pygame.mouse.get_pos()
                                                            x_coord=pos[0]
                                                            y_coord=pos[1]
                                                            
                                                    #Option/Box 1   
                                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5
                                                        
                                                    #Option/Box 2
                                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5

                                                    #Option/Box 3                
                                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5


                                                    #Option/Box 4
                                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                                        sound.stop()
                                                        score=score+1
                                                        print "Correct Answer"
                                                        x_coord = 2
                                                        y_coord = 5     

                                                
                                                    if x_coord in range (1,16) and y_coord in range(4,14):

                                                        print "Your score is",score
                                                        print "We're gonna add a cash prize of Qr",score*100,"into your account"
                                                        chkname=raw_input("Please enter your name:")
                                                        chkccardno=input("Sir, please enter your credit card number:")

                                                        

                                                        file=open('Bank.Dat','r')
                                                        file2=open('Temp.Dat','w')
                                                        try:
                                                            while True:    
                                                                x=pickle.load(file)
                                                                if x[2]==chkccardno and x[0]==chkname.lower():
                                                                        x[3]=x[3]+(score*100)
                                                                        pickle.dump(x,file2)
                                                                else:
                                                                    pickle.dump(x,file2)
                                                                

                                                        except EOFError:
                                                            file2.close()
                                                            file.close()
                                                            os.rename('Bank.Dat','Bank1.Dat')
                                                            os.rename('Temp.Dat','Bank.Dat')
                                                            os.remove('Bank1.Dat')

                                                        

                                                                                                        
                                                        a=1                                                                                                           
                                                        break
                                                                
                                                    
                                                    #Round 5 Screen
                                                    pygame.init()
                                                    size = [819,644]
                                                    screen = pygame.display.set_mode(size)
                                                    pygame.display.set_caption("Al Khor Community")
                                                    done = False
                                                    clock = pygame.time.Clock()
                                                    x_coord = 0
                                                    y_coord = 0
                                                    #Displaying the Round 3 Screen            
                                                    background=pygame.image.load('PS5.jpg')
                                                    screen.blit(background,(0,0))
                                                    pygame.display.flip()
                                                    clock.tick(30)    

                                            #Round 4 Screen
                                            pygame.init()
                                            size = [819,644]
                                            screen = pygame.display.set_mode(size)
                                            pygame.display.set_caption("Al Khor Community")
                                            done = False
                                            clock = pygame.time.Clock()
                                            x_coord = 0
                                            y_coord = 0
                                            #Displaying the Round 3 Screen            
                                            background=pygame.image.load('PS4.jpg')
                                            screen.blit(background,(0,0))
                                            pygame.display.flip()
                                            clock.tick(30)    


                                        
                                    #Round 3 Screen
                                    pygame.init()
                                    size = [819,644]
                                    screen = pygame.display.set_mode(size)
                                    pygame.display.set_caption("Al Khor Community")
                                    done = False
                                    clock = pygame.time.Clock()
                                    x_coord = 0
                                    y_coord = 0
                                    #Displaying the Round 3 Screen            
                                    background=pygame.image.load('PS3.jpg')
                                    screen.blit(background,(0,0))
                                    pygame.display.flip()
                                    clock.tick(30)                                
                                        

                            #Round 2 Screen
                            pygame.init()
                            size = [819,644]
                            screen = pygame.display.set_mode(size)
                            pygame.display.set_caption("Al Khor Community")
                            done = False
                            clock = pygame.time.Clock()
                            x_coord = 0
                            y_coord = 0
                            #Displaying the Round 2 Screen            
                            background=pygame.image.load('PS2.jpg')
                            screen.blit(background,(0,0))
                            pygame.display.flip()
                            clock.tick(30)

                        



                    #Round 1 Screen
                    pygame.init()
                    size = [819,644]
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("Al Khor Community")
                    done = False
                    clock = pygame.time.Clock()
                    x_coord = 0
                    y_coord = 0
                    #Displaying the Round 1 Screen            
                    background=pygame.image.load('PS1.jpg')
                    screen.blit(background,(0,0))
                    pygame.display.flip()
                    clock.tick(30)



            #3. The Grammy's
            if x_coord in range (23,545) and y_coord in range(406,483):

                
                #Song 1 - Girl On Fire(Alicia Keys)
                pygame.init()
                a=0
                score=0
                width,height=708,424
                screen=pygame.display.set_mode((width,height))
                pygame.display.set_caption('Guess Artist')
                
                sound=pygame.mixer.Sound('Alicia.wav')
                sound.play()
                done = False
                clock = pygame.time.Clock()
                # Current position
                x_coord = 0
                y_coord = 0

                while not done:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            x_coord=pos[0]
                            y_coord=pos[1]

                    #Option/Box 1   
                    if x_coord in range (72,405) and y_coord in range(312,406):
                        sound.stop()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5
                        
                    #Option/Box 2
                    if x_coord in range (439,777) and y_coord in range(313,403):
                        sound.stop()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5

                    #Option/Box 3                
                    if x_coord in range (73,407) and y_coord in range(442,536):
                        sound.stop()
                        score=score+1
                        print "Correct Answer"

                        x_coord = 2
                        y_coord = 5


                    #Option/Box 4
                    if x_coord in range (436,777) and y_coord in range(442,535):
                        sound.stop()
                        print "Incorrect Answer"
                        x_coord = 2
                        y_coord = 5     

                    if a==1:
                        break
                    
                    if x_coord in range (1,16) and y_coord in range(4,14):
                        
                        #Song 2 - Clarity - Zedd
                        
                        pygame.init()
                        width,height=708,424
                        screen=pygame.display.set_mode((width,height))
                        pygame.display.set_caption('Guess Artist')
                        sound=pygame.mixer.Sound('Clarity.wav')
                        sound.play()
                        done = False
                        clock = pygame.time.Clock()
                        # Current position
                        x_coord = 0
                        y_coord = 0

                        while not done:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    done = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos=pygame.mouse.get_pos()
                                    x_coord=pos[0]
                                    y_coord=pos[1]
                                    
                            #Option/Box 1   
                            if x_coord in range (72,405) and y_coord in range(312,406):
                                sound.stop()    

                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5
                                
                            #Option/Box 2
                            if x_coord in range (439,777) and y_coord in range(313,403):
                                sound.stop()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5

                            #Option/Box 3                
                            if x_coord in range (73,407) and y_coord in range(442,536):
                                sound.stop()
                                print "Incorrect Answer"
                                x_coord = 2
                                y_coord = 5


                            #Option/Box 4
                            if x_coord in range (436,777) and y_coord in range(442,535):
                                sound.stop()
                                score=score+1                                
                                print "Correct Answer"
                                x_coord = 2
                                y_coord = 5     
                       
                                
                            if a==1:
                                break

                            if x_coord in range (1,16) and y_coord in range(4,14):
                                
                                #Song 3 - Get Lucky(Daft Punk)
                                
                                pygame.init()
                                width,height=708,424
                                screen=pygame.display.set_mode((width,height))
                                pygame.display.set_caption('Guess Artist')
                                sound=pygame.mixer.Sound('DaftPunk.wav')
                                sound.play()
                                done = False
                                clock = pygame.time.Clock()
                                # Current position
                                x_coord = 0
                                y_coord = 0

                                while not done:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            done = True
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos=pygame.mouse.get_pos()
                                            x_coord=pos[0]
                                            y_coord=pos[1]
                                            
                                    #Option/Box 1   
                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                        sound.stop()
                                        score=score+1                                        
                                        print "Correct Answer"
                                        x_coord = 2
                                        y_coord = 5
                                        
                                    #Option/Box 2
                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5

                                    #Option/Box 3                
                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5


                                    #Option/Box 4
                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                        sound.stop()
                                        print "Incorrect Answer"
                                        x_coord = 2
                                        y_coord = 5     

                                        
                                    if a==1:
                                        break
                            
                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                        
                                        #Song 4 - Can't Hold Us(Macklemore)
                                        
                                        pygame.init()
                                        width,height=708,424
                                        screen=pygame.display.set_mode((width,height))
                                        pygame.display.set_caption('Guess Artist')
                                        sound=pygame.mixer.Sound('Macklemore.wav')
                                        sound.play()
                                        done = False
                                        clock = pygame.time.Clock()
                                        # Current position
                                        x_coord = 0
                                        y_coord = 0

                                        while not done:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    done = True
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    pos=pygame.mouse.get_pos()
                                                    x_coord=pos[0]
                                                    y_coord=pos[1]
                                                    
                                            #Option/Box 1   
                                            if x_coord in range (72,405) and y_coord in range(312,406):
                                                sound.stop()
                                                score=score+1
                                                print "Correct Answer"
                                                x_coord = 2
                                                y_coord = 5
                                                
                                            #Option/Box 2
                                            if x_coord in range (439,777) and y_coord in range(313,403):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5

                                            #Option/Box 3                
                                            if x_coord in range (73,407) and y_coord in range(442,536):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5


                                            #Option/Box 4
                                            if x_coord in range (436,777) and y_coord in range(442,535):
                                                sound.stop()
                                                print "Incorrect Answer"
                                                x_coord = 2
                                                y_coord = 5     


                                            if a==1:
                                                break
                                                
                                            if x_coord in range (1,16) and y_coord in range(4,14):
                                                
                                                #Song 5 - Lorde(Royals)
                                                pygame.init()
                                                width,height=708,424
                                                screen=pygame.display.set_mode((width,height))
                                                pygame.display.set_caption('Guess Artist')
                                                sound=pygame.mixer.Sound('Royals.wav')
                                                sound.play()
                                                done = False
                                                clock = pygame.time.Clock()
                                                # Current position
                                                x_coord = 0
                                                y_coord = 0

                                                while not done:
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            done = True
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            pos=pygame.mouse.get_pos()
                                                            x_coord=pos[0]
                                                            y_coord=pos[1]
                                                            
                                                    #Option/Box 1   
                                                    if x_coord in range (72,405) and y_coord in range(312,406):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5
                                                        
                                                    #Option/Box 2
                                                    if x_coord in range (439,777) and y_coord in range(313,403):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5

                                                    #Option/Box 3                
                                                    if x_coord in range (73,407) and y_coord in range(442,536):
                                                        sound.stop()
                                                        print "Incorrect Answer"
                                                        x_coord = 2
                                                        y_coord = 5


                                                    #Option/Box 4
                                                    if x_coord in range (436,777) and y_coord in range(442,535):
                                                        sound.stop()
                                                        score=score+1                                                        
                                                        print "Correct Answer"
                                                        x_coord = 2
                                                        y_coord = 5     

                                                
                                                    if x_coord in range (1,16) and y_coord in range(4,14):
                                                        
                                                        print "Your score is",score
                                                        print "We're gonna add a cash prize of Qr",score*100,"into your account"
                                                        chkname=raw_input("Please enter your name:")
                                                        chkccardno=input("Sir, please enter your credit card number:")

                                                        
                                                        file=open('Bank.Dat','r')
                                                        file2=open('Temp.Dat','w')
                                                        try:
                                                            while True:    
                                                                x=pickle.load(file)
                                                                if x[2]==chkccardno and x[0]==chkname.lower():
                                                                        x[3]=x[3]+(score*100)
                                                                        pickle.dump(x,file2)
                                                                else:
                                                                    pickle.dump(x,file2)
                                                                

                                                        except EOFError:
                                                            file2.close()
                                                            file.close()
                                                            os.rename('Bank.Dat','Bank1.Dat')
                                                            os.rename('Temp.Dat','Bank.Dat')
                                                            os.remove('Bank1.Dat')

                                                        
                                                                                                        
                                                        a=1                                                                                                           
                                                        break
                                                                
                                                    
                                                    #Round 5 Screen
                                                    pygame.init()
                                                    size = [819,644]
                                                    screen = pygame.display.set_mode(size)
                                                    pygame.display.set_caption("Al Khor Community")
                                                    done = False
                                                    clock = pygame.time.Clock()
                                                    x_coord = 0
                                                    y_coord = 0
                                                    #Displaying the Round 3 Screen            
                                                    background=pygame.image.load('S5.jpg')
                                                    screen.blit(background,(0,0))
                                                    pygame.display.flip()
                                                    clock.tick(30)    

                                            #Round 4 Screen
                                            pygame.init()
                                            size = [819,644]
                                            screen = pygame.display.set_mode(size)
                                            pygame.display.set_caption("Al Khor Community")
                                            done = False
                                            clock = pygame.time.Clock()
                                            x_coord = 0
                                            y_coord = 0
                                            #Displaying the Round 3 Screen            
                                            background=pygame.image.load('S4.jpg')
                                            screen.blit(background,(0,0))
                                            pygame.display.flip()
                                            clock.tick(30)    


                                        
                                    #Round 3 Screen
                                    pygame.init()
                                    size = [819,644]
                                    screen = pygame.display.set_mode(size)
                                    pygame.display.set_caption("Al Khor Community")
                                    done = False
                                    clock = pygame.time.Clock()
                                    x_coord = 0
                                    y_coord = 0
                                    #Displaying the Round 3 Screen            
                                    background=pygame.image.load('S3.jpg')
                                    screen.blit(background,(0,0))
                                    pygame.display.flip()
                                    clock.tick(30)                                
                                        

                            #Round 2 Screen
                            pygame.init()
                            size = [819,644]
                            screen = pygame.display.set_mode(size)
                            pygame.display.set_caption("Al Khor Community")
                            done = False
                            clock = pygame.time.Clock()
                            x_coord = 0
                            y_coord = 0
                            #Displaying the Round 2 Screen            
                            background=pygame.image.load('S2.jpg')
                            screen.blit(background,(0,0))
                            pygame.display.flip()
                            clock.tick(30)

                        




                    #Round 1 Screen
                    pygame.init()
                    size = [819,644]
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("Al Khor Community")
                    done = False
                    clock = pygame.time.Clock()
                    x_coord = 0
                    y_coord = 0
                    #Displaying the Round 1 Screen            
                    background=pygame.image.load('S1.jpg')
                    screen.blit(background,(0,0))
                    pygame.display.flip()
                    clock.tick(30)





            #6. Go back to AKC
            if x_coord in range (0,99) and y_coord in range(696,730):
                break
                

            #Playlist Screen
            pygame.init()
            size = [574,733]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Al Khor Community")
            done = False
            clock = pygame.time.Clock()
            x_coord = 0
            y_coord = 0
            #Displaying the Playlist Screen           
            background=pygame.image.load('Playlist3.jpg')
            screen.blit(background,(0,0))
            pygame.display.flip()
            clock.tick(30)





    #Displaying the Home Screen(AKC Map)            
    width,height=479,822
    screen=pygame.display.set_mode((width,height))           
    background=pygame.image.load('bg.jpg')
    screen.blit(background,(0,0))       
    pygame.display.flip()
    clock.tick(30)
pygame.quit()


