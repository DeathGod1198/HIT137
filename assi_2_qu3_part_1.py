def decryption_code(x,value): #created a function that takes two parameters
    value=value%26 #checking is the key/shift is more than 26 or not.
    ab="" # an empty string to store the decrypted code
    for ch in x: # using for loop 
      if ch.isalpha(): #checking if the contion is true or not.
         newone=ord(ch)-value 
         if ch.isupper():#checking if the contion is true or not.
            if newone > ord("Z"):
               newone-=26
            elif newone <ord("A"):
                newone+=26
         elif ch.islower():#checking if the contion is true or not.
              if newone > ord("z"):#checking if the contion is true or not.
                    newone-=26
              elif newone< ord("a"):#checking if the contion is true or not.
                newone+=26
         ab +=chr(newone) 


            
      else:
        ab+=ch
    return ab 
x='''tybony_inevnoyr = 100   #encrypted code
zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr 
ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > 0:
vs ybpny_inevnoyr % 2 == 0: 
    ahzoref.erzbir (ybpny_inevnoyr)
ybpny_inevnoyr -= 1
erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)
qrs zbqvsl_qvpg():
ybpny_inevnoyr = 10
zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvsl_qvpg(5)
qrs hcqngr_tybony():
 tybony tybony_inevnoyr
 tybony_inevnoyr += 10
sbe v va enatr(5):
 cevag(v)
 V += 1
vs zl_frg vf abg Abar naq z1_qvpg['xr14'] == 10: 
    cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
 cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
   '''       
for i in range(1,26):#to find the shift/value
    
  z=decryption_code(x,i) 
  print(f"Shift {i}:")  
  print(z)   