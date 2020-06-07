			;MACRO DEFINITIONS 

@MACRO sub 2 : %1 - %2										; $1  Single-line Macro
@MACRO ABC 2 : %1 / %2										; $2  Single-line Macro
@MACRO mul 0 : 78												; $3  Single-line Macro
@MACRO sdd 5 : %1+ ABC (%2,%3) + sub(%4,%5)			; $4  Single-line nested Macro
@MACRO lop 2 : %1 +sdd(%2,A,B,C,70)						; $5  Single-line nested Macro

@MACRO trash 3  :-											; $6  Multi-line nested Macro
{
%1= spam (%1,%2,%3) *%1
}

@MACRO spam 3 :-												; $7  Multi-line Macro
  {
   %3 = %1 + %2
   %2= %1+ %3
   }

@MACRO lop 2 : %1 + %2										; $8  Single-line Macro



			; CODE PART

section .data

a : dd 0
b : db "Hey There",10,0

section .text

global main
extern printf
extern atoi

main : 

push ebp
mov ebp.esp

sdd (a,b,c,d,f)  
                       
%undef $6  											; Undefining a Macro

%ifndef $6  										; Conditional ifndef 
{
push msg
call printf
}
 
                           
trash(l,m,n)
                            
%redef $6  											; Redefining a Macro
   
%ifdef $6    										; Conditional ifdef
{
mov a,b
add a,c
push a
push msg
call printf
} 
                         
trash(l,m,n) 

%ifndef $9
{
push format
push a
call scanf
}

%ifdef $10
{
mov a,c
push c
push msg
call printf
}

a= mul()

spam(j,k,l)          	

lop(1,3)

mov esp,ebp
pop ebp
