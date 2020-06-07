#include<stdio.h>

			/* MACRO DEFINITIONS */

@MACRO sub 2 : %1 - %2										// $1		Single-line
@MACRO ABC 2 : %1 / %2										// $2		Single-line
@MACRO mul 0 : 78												// $3		Single-line

@MACRO sdd 5 : %1+ ABC (%2,%3) + sub(%4,%5)			// $4    Nested Macro, Single-line
@MACRO lop 2 : %1 +sdd(%2,A,B,C,70)						// $5    Nested Macro, Single-line

@MACRO trash 3  :-											// $6    Nested Macro, Multi-line macro
{
%1= spam (%1,%2,%3) *%1
}

@MACRO spam 3 :-												// $7		Multi-line
  {
   %3 = %1 + %2
   %2= %1+ %3
   }

@MACRO lop 2 : %1 + %2										// $8		Single-line
      	
      	/* MAIN */
      	
int main() 
    
{

sdd (a,b,c,d,f) 					
                       
%undef $6 ; 													// Undefining Macro

%ifndef $6  													// Conditionals ifndef
{ 
printf("Hey ! This block should be there ");
a=7+8;
}  
                           
trash(l,m,n)
                            
%redef $6 ;														// Redifing Macro
   
%ifdef $6 														// Conditionals ifdef
{
printf("Hey ! This block should be there ");
a = b+c ;
} 
                         
trash(l,m,n) 

%ifndef $9
{
printf("Hey ! This block should be there ");
scanf("%d",&nm);
}

%ifdef $10
{
printf("ERROR ! This block shoud not be there ");
}

a= mul() ;

spam(j,k,l)          	

lop(1,3)

}
