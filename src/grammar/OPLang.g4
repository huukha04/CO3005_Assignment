grammar OPLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit();
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    
    elif tk == self.STRING_LIT:
        result.text = result.text[1:-1]


    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text); 
    elif tk == self.ERROR_FLOAT:
        raise ErrorToken(result.text); 
    else:
        return result
}

options{
	language=Python3;
}

// =======================
// PARSER RULES
// =======================

// Parser rules
program
    : (classdecl)* EOF
    ;


// Khai báo lớp
classdecl 
    : CLASS IDENTIFIER (EXTENDS IDENTIFIER)? LCB (vardecl | funcdecl)* RCB 
    ;

// Khai báo biến
vardecl
    : modifier* datatype varList SEMI
    ;
// Danh sách biến
varList
    : var (COMMA var)*
    ;
// Biến
var
    : IDENTIFIER (ASSIGN (expr | arrayInit))?
    ;
// Khởi tạo mảng
arrayInit
    : LCB expr (COMMA expr)* RCB
    | LCB arrayInit (COMMA arrayInit)* RCB
    ;






// Khai báo hàm
funcdecl
    : modifier? datatype AMPERSAND? IDENTIFIER LP paramlist? RP block
    ;
// Danh sách tham số
paramlist : param (SEMI param)* ;
param : datatype AMPERSAND? IDENTIFIER (ASSIGN expr)?;
// Khối lệnh
block : LCB stmt* RCB ;
// Câu lệnh 
stmt
    : vardecl
    | IDENTIFIER ASSIGN_OP expr SEMI   
    | block
    | expr SEMI  
    | ifstmt
    | forstmt
    | return                       
    ;
// Trả về
return 
    : RETURN expr? SEMI
    ;
// Câu lệnh điều kiện
ifstmt
    : IF expr THEN block (ELSE block)?
    ;
// Vòng lặp for
forstmt
    : FOR IDENTIFIER ASSIGN_OP expr (TO | DOWNTO) expr DO block
    | FOR datatype IDENTIFIER ASSIGN expr (TO | DOWNTO) expr DO block
    ;









// Kiểu dữ liệu
datatype : basetype (LSB INT_LIT? RSB)* ;
basetype : INT
         | FLOAT
         | BOOLEAN
         | STRING
         | VOID
         | IDENTIFIER
         ;

// modifier có thể là static hoặc final
modifier
    : STATIC
    | FINAL
    ;




// Biểu thức 
expr
    : expr ADD expr
    | expr SUB expr
    | expr MUL expr
    | expr DIV expr
    | expr MOD expr
    | expr EQ expr
    | expr NEQ expr
    | expr GT expr
    | expr LT expr
    | expr GTE expr
    | expr LTE expr
    | expr AND expr
    | expr OR expr
    | expr CONCAT expr
    | expr ASSIGN_OP expr
    | LP expr RP
    | expr '.' IDENTIFIER   
    | expr '.' IDENTIFIER LP arglist? RP
    | IDENTIFIER LSB expr RSB
    | NEW IDENTIFIER LP (expr (COMMA expr)*)? RP
    | NEW IDENTIFIER LSB expr RSB
    | IDENTIFIER
    | INT_LIT
    | FLOAT_LIT
    | TRUE
    | FALSE
    | STRING_LIT
    | NIL
    ;
arglist : expr (COMMA expr)* ;








// =======================
// LEXER RULES
// =======================

// Keyword
BOOLEAN   : 'boolean' ;
BREAK     : 'break' ;
CLASS     : 'class' ;
CONTINUE  : 'continue' ;
DO        : 'do' ;
ELSE      : 'else' ;
EXTENDS   : 'extends' ;
FLOAT     : 'float' ;
IF        : 'if' ;
INT       : 'int' ;
NEW       : 'new' ; //
STRING    : 'string' ;
THEN      : 'then' ;
FOR       : 'for' ;
RETURN    : 'return' ;
TRUE      : 'true' ;
FALSE     : 'false' ;
VOID      : 'void' ;
NIL       : 'nil' ;
THIS      : 'this' ;
FINAL     : 'final' ;
STATIC    : 'static' ;
TO        : 'to' ;
DOWNTO    : 'downto' ;

// Character Set
WS : [ \t\f\r\n]+ -> skip ; // Bỏ qua whitespace

// Comment
LINE_COMMENT : '#' ~[\r\n]* -> skip ; // Line comment: từ # đến hết dòng
BLOCK_COMMENT : '/*' .*? '*/' -> skip ; // Block comment: từ /* đến */

// Operator
// Arithmetic operators
ADD  : '+' ;
SUB  : '-' ;
MUL  : '*' ;
DIV  : '/' ;
MOD  : '%' ;
BACKSLASH : '\\' ;

// Relational operators
EQ   : '==' ;
NEQ  : '!=' ;
GT   : '>' ;
LT   : '<' ;
GTE  : '>=' ;
LTE  : '<=' ;

// Logical operators
AND  : '&&' ;
OR   : '||' ;
NOT  : '!' ;
// Other operators
CONCAT  : '^' ;
ASSIGN_OP : ':=' ;
ASSIGN : '=' ;
// New: Trong keyword

// Separator
LSB : '[' ;   
RSB : ']' ;   
LP  : '(' ;  
RP  : ')' ;  
LCB : '{' ; 
RCB : '}' ;   
SEMI : ';' ; 
COLON : ':' ; 
DOT : '.' ;   
COMMA : ',' ; 


// Special Characters
TILDE : '~' ;
AMPERSAND : '&' ;

// Literal
INT_LIT : DIGIT+ ;

FLOAT_LIT
    : DIGIT+ '.' DIGIT* ( [eE] [+-]? DIGIT+)?
    | DIGIT+ [eE][+-]?DIGIT+
    ;
ERROR_FLOAT
    : '.' DIGIT+            // .12
    | DIGIT+ [eE] [+-]?     // 5e, 5e+, 5e-
    ;


STRING_LIT
    : '"' ( ~["\\\r\n] 
    | ESCAPE_SEQ )* '"' 
    ;
STRING_LITERAL
    : '"' ( ~["\\\r\n] | ESCAPE_SEQ )* '"'
    ;

ILLEGAL_ESCAPE
    : '"' ( ~["\\\r\n] | ESCAPE_SEQ )* ILLEGAL_ESC
    ;

UNCLOSE_STRING
    : '"' ( ~["\\\r\n] | ESCAPE_SEQ )* ( '\\'? EOF | '\r'? '\n' )
    ;

// BOOL_LIT: Đã có trong keyword
// ARRAY_LIT: Xử lí trong Parser



// Identifier
IDENTIFIER : (LETTER | '_') (LETTER | DIGIT | '_')* ;

// Fragment rules
fragment DIGIT  : [0-9] ;
fragment LETTER : [a-zA-Z] ;
fragment ESCAPE_SEQ : '\\' [btnfr"\\] ; // Escape hợp lệ
fragment ILLEGAL_ESC : '\\' ~[btnfr"\\] ; // Escape không hợp lệ

ERROR_CHAR
    : .
    ;