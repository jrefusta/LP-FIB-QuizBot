grammar Enquestes;

r : (tanda)+ enquesta EOF;

tanda : (pregunta)+ resposta (item)+ alternativa* ;

pregunta : ID DOSPUNTS PREGUNTA (ID)* INTERROGANT ;

resposta : ID DOSPUNTS RESPOSTA opcions;

opcions : (NUM DOSPUNTS (ID)+ PUNTICOMA)*;

item : ID DOSPUNTS ITEM ID FLETXA ID ;

alternativa : ID DOSPUNTS ALTERNATIVA ID OC implicacio CC ;

implicacio : implicacions (COMA implicacions)* ;

implicacions : OP NUM COMA ID CP ;

enquesta : ID DOSPUNTS ENQUESTA (ID)+ END;
    
PREGUNTA : 'PREGUNTA' ;    

RESPOSTA : 'RESPOSTA' ;

ITEM : 'ITEM' ;

ENQUESTA : 'ENQUESTA' ;

ALTERNATIVA : 'ALTERNATIVA' ;

END : 'END' ;

FLETXA : '->' ;

OP : '(' ;

CP : ')' ;

OC : '[' ;

CC : ']' ;

COMA : ',' ;

PUNTICOMA : ';' ;

INTERROGANT : '?' ;
    
DOSPUNTS : ':' ;    
    
NUM : [0-9]+ ;

ID : [A-Za-z][A-Za-z0-9\u0080-\u00FF]* ;   

WS : ('\t'|' '|'\r'|'\n'|'\f') -> skip ;
