''' 										 NAME : RITESH KUMAR               |  NAME : PAWAN KUMAR
			 								 STUDENT ID : 2015UCP1727			  |  STUDENT ID : 2015UCP1622
			 								 BATCH : B(7,8)						  |  BATCH : B(7,8) 																	'''


'''												 	    *** MACRO Mini-project ***																					'''


''' 														   *** FILE HANDLING ***																						'''
import sys
import re																									# Imports Regular Expression
from colorama import Fore, Back,Style																# Imports styles from COLORMA
me = input("Enter the file name : ")																# Ask for the file
if not ( me.endswith('.c') or me.endswith('.asm') or me.endswith('.py') ) :			# Error Condition
	print(Fore.RED + "\nFatal Error ! File type unrecognized.\nPlease try with a different file.\n" + Style.RESET_ALL)
	sys.exit()
fo = open(me, "r+")                                                               	# Opens the file in read mode
text = fo.read()                                                                    # Reads the file
fo.close()																									# Closes the file
op1 = ['+', '-']																							# Initialization of required variables
op2 = [ '*', '/', '%']
op3= ['|','&','!']
op = op1 + op2 + op3
list=[] 

''' 														  *** COMMENTS REMOVAL *** 																					'''

# 1). C Comments Removal :

if me.endswith('.c') :																					# Checks whether it is a C file
	while "//" in text :																					# Single-line Comments removal
		text=re.sub("//.*?\n",'\n',text)
	while "/*" in text :																					# Multi-line Comments removal
		cntr=0
		while "/*" in text[cntr:] :
			cntr+=1
		cntr-=1
		cend=cntr
		if "*/" not in text[cend:] :
			text=text[:cntr]
		while "*/" in text[cend:]:
			cend+=1
		cend+=2
		text=text[:cntr]+text[cend:]

# 2). PYTHON Comments Removal :

elif me.endswith('.py') :																				# Checks whether it is a PYTHON file
	while "#" in text :																					# Single-line Comments removal
		text=re.sub("#.*?\n",'\n',text)

# 3). ASSEMLY Comments Removal :

elif me.endswith('.asm') :																				# Checks whether it is a ASSEMBLY file
	while ";" in text :																					# Single-line Comments removal
		text=re.sub(";.*?\n",'\n',text)

while "\t" in text :
	text=text.replace("\t"," ")
while "  " in text :
	text=text.replace('  ',' ') 
while " \n" in text :																					# Extra Spaces & new-line removal
	text=text.replace(' \n','\n')
while "\n " in text :
	text=text.replace('\n ','\n')
while "\n\n" in text :
	text=text.replace('\n\n','\n')
text=text.strip()
test=text

''' 																*** MACRO EXTRACTION ***																				'''

while '@' in text :																						# MACRO Definition extraction
	defn=""
	for letter in text :
		if letter!='@' :
			text=text[1:]
		else :
			break
	for letter in text :
		if letter != ":" :
			defn+=letter
			text=text[1:]
		else :
			defn+=letter
			text=text[1:]
			break
	li=[]
	list1=[]
	text=text.strip()
	defn=defn.strip()
	li=defn.split(" ")
	if li[0] == "@MACRO" :
		if text[0]=='-' :																					# Multi-line MACRO extraction
			func=''
			text=text[2:]
			if text[0]!="{" :
				print("Error !")
			else :
				count=0
				list1+=[li[1]]
				list1+=[li[2]]
				for letter in text :
					if letter == "{" :
						count+=1
					if letter == "}" :
						count-=1
					if count==0 and letter == "}" :
						func+=letter
						text=text[1:]
						break
					elif count!=0 :
						func+=letter
						text=text[1:]
				func=func[1:len(func)-1]
				func=func.strip()
				list1+=[func]
		else :																								# Single-line MACRO extraction
			func=''
			list1+=[li[1]]
			list1+=[li[2]]
			for letter in text :
				if letter!='\n' : 
					func+=letter
					text=text[1:]
				else :
					text=text[1:]
					break
			list1+=[func]
	flag=0
	for item in list :																					# Checks the redefined MACROs
		if item[0]== list1[0] :
			flag=1
			print(Fore.CYAN + "\nError !")
			print(Fore.RED + item[0] +Fore.CYAN + " Macro redefined. Previously defined macro will be considered implicitly." + Style.RESET_ALL)
			break
	if list1!=[] and flag == 0 :
		list+=[list1]																						# Accumulation of all the defined MACROs along with 
																												# their no. of parameters and definition



name = []																									# Creates a list with the names of all defined MACROs
for x in list :
	name+=[x[0]]

''' 																	*** NESTING ***																						'''

for x in list :																							# Nested MACROs
	str1=x[2]
	while any (ext in str1 for ext in name) :
		for item in name :
			if item in str1 :
				break
		cnt=0
		while item in str1[cnt:] :
			cnt+=1
		cnt-=1
		cntstrt=cnt
		for i in range (cnt,len(str1)) :
			if str1[i] == "(" :
				break
		str2=''
		count=0
		param=[]
		for j in range (i,len(str1)) :
			if str1[j] == "(" :
				count +=1
			if str1[j] == ")" :
				count -=1
			if count==0 and str1[j]==")" :
				str2+=str1[j]
				break
			elif count!=0 :
				str2+=str1[j]
		cnt=j+1
		str3=str2
		str2=str2[1:len(str2)-1]
		if str2 != '' :
			if ',' in str2 :
				param=str2.split(',')
			else :
				param=[str2]
		str2=str1[cntstrt:cnt]
		for lol in list :
			if item == lol[0] :
				break
		str3=''
		str4=lol[2]
		k=int(lol[1])
		for i in range (1,k+1) :
			str5="a["+str(i)+"]"
			str3="%" + str(i)
			str4=str4.replace(str3,str5)
		for i in range (1,k+1) :
			str5="a["+str(i)+"]"
			str4=str4.replace(str5,param[i-1])
		str1 =str1.replace(str2,str4)
		x[2]=str1																							# Overwrites the nested defind MACROs


'''												      	*** PRE-PROCESSING of FILE ***																			'''

text=text.strip()
test=text

rep=[]
while any (ext in test for ext in name) :
		label=1
		for item in name :
			if item in test :
				break
			else :
				label+=1
		haha=["rep[" + str(label) + "]"]
		cnt=0
		while item in test[cnt:] :
			cnt+=1
		cnt-=1
		cntstrt=cnt
		for i in range (cnt,len(test)) :
			if test[i] == "(" :
				break
		str2=''
		count=0
		param=[]
		for j in range (i,len(test)) :
			if test[j] == "(" :
				count +=1
			if test[j] == ")" :
				count -=1
			if count==0 and test[j]==")" :
				str2+=test[j]
				break
			elif count!=0 :
				str2+=test[j]
		cnt=j+1
		str2=str2[1:len(str2)-1]
		if str2 != '' :
			if ',' in str2 :
				param=str2.split(',')
			else :
				param=[str2]
		str2=test[cntstrt:cnt]
		for lol in list :
			if item == lol[0] :
				break
		str3=''
		str4=lol[2]
		k=int(lol[1])
		for i in range (1,k+1) :
			str3="%" + str(i)
			str4=str4.replace(str3,param[i-1])
		while '\n\n' in str4 :																				# undef & redef
			str4=str4.replace("\n\n","\n")
		str6 = "%undef $" + str(label)
		str7= "%redef $" +str(label)
		if str6 in test[:cntstrt] :
			cnt1=0 
			while str6 in test[cnt1:cntstrt] :
				cnt1+=1
			cnt1-=1
			if str7 in test[cnt1:cntstrt] :
				test = test[:cntstrt]+test[cntstrt:].replace(str2,str4)
			else :
				haha+=[str2]
				test = test[:cntstrt]+test[cntstrt:].replace(str2,haha[0])
				rep+=[haha]
		else :
			test = test.replace(str2,str4)
name1=[]
for item in rep :
	name1+=[item[0]]
while any (ext in test for ext in name1) :
	label = 0
	for item in name1 :
			if item in test :
				break
			else :
				label+=1
	cnt=0
	while item in test[cnt:] :
		cnt+=1
	cnt-=1
	cntstrt=cnt
	for i in range (cntstrt , len(test)) :
		if test[i] =="]" :
			break
	str9=test[cntstrt:i+1]
	test=test.replace(str9,rep[label][1])

'''																	*** CONDITIONALS ***																					'''

label=0
cony=[]
conn=[]
namey=[]
namen=[]
for item in list :
	label+=1
	namey+=["%ifdef $" + str(label)]
	namen+=["%ifndef $" + str(label)]

while any(ext in test for ext in namen) :																# ifndef CONDITIONS
	for item in namen :
		if item in test :
			break
	cnt=0
	while item in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	flag=0
	str10=''
	lol=''
	for letter in test[cntstrt:] :
		if letter == "{" :
			flag+=1
		if letter == "}" :
			flag-=1
		if letter == "}" and flag==0 :
			str10+=letter
			break
		elif letter != "}" :
			str10 += letter
	for letter in str10 :
		if letter !="{" :
			lol+=letter
			str10=str10[1:]
		else :
			break
	rofl=lol
	text = lol+str10
	str10=str10[1:len(str10)-1]
	text=text.strip()
	str10=str10.strip()
	rofl=rofl.strip()
	for letter in lol :
		if letter == "$" :
			lol=lol[1:]
			break
		else :
			lol=lol[1:]
	lol=lol.strip()
	label1=int(lol)
	str6 = "%undef $" + str(label1)
	str7= "%redef $" +str(label1)
	if rofl in namen :
		if str6 in test[:cntstrt] :
				cnt1=0 
				while str6 in test[cnt1:cntstrt] :
					cnt1+=1
				cnt1-=1
				if str7 in test[cnt1:cntstrt] :
					test = test[:cntstrt]+test[cntstrt:].replace(text,'')
				else :
					test = test[:cntstrt]+test[cntstrt:].replace(text,str10)
		else :
			test = test.replace(text,'')
	else :
		test =test.replace(text,str10)

while any(ext in test for ext in namey) :																# %ifdef CONDITIONS	
	for item in namey :
		if item in test :
			break
	cnt=0
	while item in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	flag=0
	str10=''
	lol=''
	for letter in test[cntstrt:] :
		if letter == "{" :
			flag+=1
		if letter == "}" :
			flag-=1
		if letter == "}" and flag==0 :
			str10+=letter
			break
		elif letter != "}" :
			str10 += letter
	for letter in str10 :
		if letter !="{" :
			lol+=letter
			str10=str10[1:]
		else :
			break
	rofl=lol
	text = lol+str10
	str10=str10[1:len(str10)-1]
	for letter in lol :
		if letter == "$" :
			lol=lol[1:]
			break
		else :
			lol=lol[1:]
	lol=lol.strip()
	label1=int(lol)
	str6 = "%undef $" + str(label1)
	str7= "%redef $" +str(label1)
	str10=str10.strip()
	text =text.strip()
	rofl = rofl.strip()
	if rofl in namey :
		if str6 in test[:cntstrt] :
				cnt1=0 
				while str6 in test[cnt1:cntstrt] :
					cnt1+=1
				cnt1-=1
				if str7 in test[cnt1:cntstrt] :
					test = test[:cntstrt]+test[cntstrt:].replace(text,str10)
				else :
					test = test[:cntstrt]+test[cntstrt:].replace(text,'')
		else :
			test = test.replace(text,str10)
	else :
		test=test.replace(text,'')

lol = ["%undef","%redef"]
while any (ext in test for ext in lol) :
	cnt=0
	while lol[0] in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	str6=''
	for letter in test[cntstrt:] :
		if letter == "\n" :
			str6+=letter
			break
		else :
			str6+=letter
	test = test.replace(str6,'')
	cnt=0
	while lol[1] in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	str6=''
	for letter in test[cntstrt:] :
		if letter == "\n" :
			str6+=letter
			break
		else :
			str6+=letter
	test = test.replace(str6,'')

while "%ifdef" in test :
	cnt=0
	while "%ifdef" in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	str10=''
	lol=''
	for letter in test[cntstrt:] :
		if letter == "{" :
			flag+=1
		if letter == "}" :
			flag-=1
		if letter == "}" and flag==0 :
			str10+=letter
			break
		elif letter != "}" :
			str10 += letter
	test=test.replace(str10,'')

while "%ifndef" in test :
	cnt=0
	while "%ifndef" in test[cnt:] :
		cnt+=1
	cntstrt=cnt-1
	str10=''
	lol=''	
	for letter in test[cntstrt:] :
		if letter == "{" :
			flag+=1
		if letter == "}" :
			flag-=1
		if letter == "}" and flag==0 :
			str10+=letter
			break
		elif letter != "}" :
			str10 += letter
	for letter in str10 :
		if letter !="{" :
			lol+=letter
			str10=str10[1:]
		else :
			break
	text = lol+str10
	str10=str10[1:len(str10)-1]
	str10=str10.strip()
	text =text.strip()
	test=test.replace(text,str10)



'''																		*** OUTPUT ***																						'''

print(Fore.BLUE + "\nThe preprocessed file is : \n\n" +Style.RESET_ALL)
print(test,"\n\n")
