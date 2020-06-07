			#MACRO DEFINITIONS 

@MACRO sub 2 : %1 - %2										# $1  Single-line Macro
@MACRO ABC 2 : %1 / %2										# $2  Single-line Macro
@MACRO mul 0 : 78												# $3  Single-line Macro
@MACRO sdd 5 : %1+ ABC (%2,%3) + sub(%4,%5)			# $4  Single-line nested Macro
@MACRO lop 2 : %1 +sdd(%2,A,B,C,70)						# $5  Single-line nested Macro

@MACRO trash 3  :-											# $6  Multi-line nested Macro
{
%1= spam (%1,%2,%3) *%1
}

@MACRO spam 3 :-												# $7  Multi-line Macro
  {
   %3 = %1 + %2
   %2= %1+ %3
   }

@MACRO lop 2 : %1 + %2										# $8  Single-line Macro

			# Code Part

c=sdd (a,b,c,d,f) 					
                       
%undef $6 												# Undefining Macro

%ifndef $6  													# Conditionals ifndef
{ 
print("Hey ! This block should be there ")
a=7+8
}  
                           
trash(l,m,n)
                            
%redef $6 													# Redifing Macro
   
%ifdef $6 														# Conditionals ifdef
{
print("Hey ! This block should be there ")
a = b+c 
} 
                         
trash(l,m,n) 

%ifndef $9
{
print("Hey ! This block should be there ")
input(nm)
}

%ifdef $10
{
print("ERROR ! This block shoud not be there ")
}

a= mul() 

spam(j,k,l)          	

lop(1,3)

