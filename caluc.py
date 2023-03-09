#this program do the calcoulator program
# first inter the first number and make sure its number and its 
while (True) :
  fnum = float ( input ( ' plase enter the first number,'))
 # first num
  Snum = float( input( ' plase enter the second number,'))   #Second num
  opt = input('plase chose the operation,')
  #opreation
  if Snum== 0.0 and opt=='/': 
       print ('error can not do opreation')               
  elif Snum!=0.0: 
      print (fnum/Snum)
  elif opt=="+":
      print (fnum+Snum)
  elif opt=="-":
       print (fnum-Snum)
  elif opt=="*":
     print (fnum*Snum)
  else:
     print('error input opreation')
 # match opt :
  #       case "+": 
      #          print (fnum-Snum)
 #        case  "*" :
#               print(fnum*Snum)
#         case _:
#  break;
  flg=input('do you want anthor opreation input : y/n ')
  if flg=='n' :
    input(' the program is finish ')
     break;

            
    
    
