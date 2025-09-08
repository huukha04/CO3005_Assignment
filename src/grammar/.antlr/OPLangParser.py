# Generated from c:/Users/khahu/Desktop/CO3005_Assignment/src/grammar/OPLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,66,327,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,1,1,1,1,1,
        5,1,56,8,1,10,1,12,1,59,9,1,1,1,1,1,1,2,5,2,64,8,2,10,2,12,2,67,
        9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,4,
        1,4,1,4,1,4,3,4,85,8,4,3,4,87,8,4,1,5,1,5,1,5,1,5,5,5,93,8,5,10,
        5,12,5,96,9,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,104,8,5,10,5,12,5,107,
        9,5,1,5,1,5,3,5,111,8,5,1,6,3,6,114,8,6,1,6,1,6,3,6,118,8,6,1,6,
        1,6,1,6,3,6,123,8,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,131,8,7,10,7,12,
        7,134,9,7,1,8,1,8,3,8,138,8,8,1,8,1,8,1,8,3,8,143,8,8,1,9,1,9,5,
        9,147,8,9,10,9,12,9,150,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,167,8,10,1,11,1,11,3,11,
        171,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,181,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,202,8,13,1,14,1,14,1,14,3,14,207,
        8,14,1,14,5,14,210,8,14,10,14,12,14,213,9,14,1,15,1,15,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,5,17,235,8,17,10,17,12,17,238,9,17,3,17,240,8,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,256,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,311,8,17,1,17,5,17,314,8,17,10,17,
        12,17,317,9,17,1,18,1,18,1,18,5,18,322,8,18,10,18,12,18,325,9,18,
        1,18,0,1,34,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,0,3,1,0,23,24,6,0,1,1,8,8,10,10,12,12,18,18,65,65,1,0,21,22,367,
        0,41,1,0,0,0,2,46,1,0,0,0,4,65,1,0,0,0,6,72,1,0,0,0,8,80,1,0,0,0,
        10,110,1,0,0,0,12,113,1,0,0,0,14,127,1,0,0,0,16,135,1,0,0,0,18,144,
        1,0,0,0,20,166,1,0,0,0,22,168,1,0,0,0,24,174,1,0,0,0,26,201,1,0,
        0,0,28,203,1,0,0,0,30,214,1,0,0,0,32,216,1,0,0,0,34,255,1,0,0,0,
        36,318,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,
        0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,
        1,1,0,0,0,46,47,5,3,0,0,47,50,5,65,0,0,48,49,5,7,0,0,49,51,5,65,
        0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,57,5,50,0,0,53,
        56,3,4,2,0,54,56,3,12,6,0,55,53,1,0,0,0,55,54,1,0,0,0,56,59,1,0,
        0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,
        5,51,0,0,61,3,1,0,0,0,62,64,3,32,16,0,63,62,1,0,0,0,64,67,1,0,0,
        0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,
        3,28,14,0,69,70,3,6,3,0,70,71,5,52,0,0,71,5,1,0,0,0,72,77,3,8,4,
        0,73,74,5,55,0,0,74,76,3,8,4,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,
        1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,77,1,0,0,0,80,86,5,65,0,0,
        81,84,5,45,0,0,82,85,3,34,17,0,83,85,3,10,5,0,84,82,1,0,0,0,84,83,
        1,0,0,0,85,87,1,0,0,0,86,81,1,0,0,0,86,87,1,0,0,0,87,9,1,0,0,0,88,
        89,5,50,0,0,89,94,3,34,17,0,90,91,5,55,0,0,91,93,3,34,17,0,92,90,
        1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,
        96,94,1,0,0,0,97,98,5,51,0,0,98,111,1,0,0,0,99,100,5,50,0,0,100,
        105,3,10,5,0,101,102,5,55,0,0,102,104,3,10,5,0,103,101,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,
        105,1,0,0,0,108,109,5,51,0,0,109,111,1,0,0,0,110,88,1,0,0,0,110,
        99,1,0,0,0,111,11,1,0,0,0,112,114,3,32,16,0,113,112,1,0,0,0,113,
        114,1,0,0,0,114,115,1,0,0,0,115,117,3,28,14,0,116,118,5,57,0,0,117,
        116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,65,0,0,120,
        122,5,48,0,0,121,123,3,14,7,0,122,121,1,0,0,0,122,123,1,0,0,0,123,
        124,1,0,0,0,124,125,5,49,0,0,125,126,3,18,9,0,126,13,1,0,0,0,127,
        132,3,16,8,0,128,129,5,52,0,0,129,131,3,16,8,0,130,128,1,0,0,0,131,
        134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,15,1,0,0,0,134,132,
        1,0,0,0,135,137,3,28,14,0,136,138,5,57,0,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,139,1,0,0,0,139,142,5,65,0,0,140,141,5,45,0,0,141,143,
        3,34,17,0,142,140,1,0,0,0,142,143,1,0,0,0,143,17,1,0,0,0,144,148,
        5,50,0,0,145,147,3,20,10,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,
        5,51,0,0,152,19,1,0,0,0,153,167,3,4,2,0,154,155,5,65,0,0,155,156,
        5,44,0,0,156,157,3,34,17,0,157,158,5,52,0,0,158,167,1,0,0,0,159,
        167,3,18,9,0,160,161,3,34,17,0,161,162,5,52,0,0,162,167,1,0,0,0,
        163,167,3,24,12,0,164,167,3,26,13,0,165,167,3,22,11,0,166,153,1,
        0,0,0,166,154,1,0,0,0,166,159,1,0,0,0,166,160,1,0,0,0,166,163,1,
        0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,21,1,0,0,0,168,170,5,15,
        0,0,169,171,3,34,17,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,
        0,0,0,172,173,5,52,0,0,173,23,1,0,0,0,174,175,5,9,0,0,175,176,3,
        34,17,0,176,177,5,13,0,0,177,180,3,18,9,0,178,179,5,6,0,0,179,181,
        3,18,9,0,180,178,1,0,0,0,180,181,1,0,0,0,181,25,1,0,0,0,182,183,
        5,14,0,0,183,184,5,65,0,0,184,185,5,44,0,0,185,186,3,34,17,0,186,
        187,7,0,0,0,187,188,3,34,17,0,188,189,5,5,0,0,189,190,3,18,9,0,190,
        202,1,0,0,0,191,192,5,14,0,0,192,193,3,28,14,0,193,194,5,65,0,0,
        194,195,5,45,0,0,195,196,3,34,17,0,196,197,7,0,0,0,197,198,3,34,
        17,0,198,199,5,5,0,0,199,200,3,18,9,0,200,202,1,0,0,0,201,182,1,
        0,0,0,201,191,1,0,0,0,202,27,1,0,0,0,203,211,3,30,15,0,204,206,5,
        46,0,0,205,207,5,58,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,
        1,0,0,0,208,210,5,47,0,0,209,204,1,0,0,0,210,213,1,0,0,0,211,209,
        1,0,0,0,211,212,1,0,0,0,212,29,1,0,0,0,213,211,1,0,0,0,214,215,7,
        1,0,0,215,31,1,0,0,0,216,217,7,2,0,0,217,33,1,0,0,0,218,219,6,17,
        -1,0,219,220,5,48,0,0,220,221,3,34,17,0,221,222,5,49,0,0,222,256,
        1,0,0,0,223,224,5,65,0,0,224,225,5,46,0,0,225,226,3,34,17,0,226,
        227,5,47,0,0,227,256,1,0,0,0,228,229,5,11,0,0,229,230,5,65,0,0,230,
        239,5,48,0,0,231,236,3,34,17,0,232,233,5,55,0,0,233,235,3,34,17,
        0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,
        0,237,240,1,0,0,0,238,236,1,0,0,0,239,231,1,0,0,0,239,240,1,0,0,
        0,240,241,1,0,0,0,241,256,5,49,0,0,242,243,5,11,0,0,243,244,5,65,
        0,0,244,245,5,46,0,0,245,246,3,34,17,0,246,247,5,47,0,0,247,256,
        1,0,0,0,248,256,5,65,0,0,249,256,5,58,0,0,250,256,5,59,0,0,251,256,
        5,16,0,0,252,256,5,17,0,0,253,256,5,61,0,0,254,256,5,19,0,0,255,
        218,1,0,0,0,255,223,1,0,0,0,255,228,1,0,0,0,255,242,1,0,0,0,255,
        248,1,0,0,0,255,249,1,0,0,0,255,250,1,0,0,0,255,251,1,0,0,0,255,
        252,1,0,0,0,255,253,1,0,0,0,255,254,1,0,0,0,256,315,1,0,0,0,257,
        258,10,28,0,0,258,259,5,28,0,0,259,314,3,34,17,29,260,261,10,27,
        0,0,261,262,5,29,0,0,262,314,3,34,17,28,263,264,10,26,0,0,264,265,
        5,30,0,0,265,314,3,34,17,27,266,267,10,25,0,0,267,268,5,31,0,0,268,
        314,3,34,17,26,269,270,10,24,0,0,270,271,5,32,0,0,271,314,3,34,17,
        25,272,273,10,23,0,0,273,274,5,34,0,0,274,314,3,34,17,24,275,276,
        10,22,0,0,276,277,5,35,0,0,277,314,3,34,17,23,278,279,10,21,0,0,
        279,280,5,36,0,0,280,314,3,34,17,22,281,282,10,20,0,0,282,283,5,
        37,0,0,283,314,3,34,17,21,284,285,10,19,0,0,285,286,5,38,0,0,286,
        314,3,34,17,20,287,288,10,18,0,0,288,289,5,39,0,0,289,314,3,34,17,
        19,290,291,10,17,0,0,291,292,5,40,0,0,292,314,3,34,17,18,293,294,
        10,16,0,0,294,295,5,41,0,0,295,314,3,34,17,17,296,297,10,15,0,0,
        297,298,5,43,0,0,298,314,3,34,17,16,299,300,10,14,0,0,300,301,5,
        44,0,0,301,314,3,34,17,15,302,303,10,12,0,0,303,304,5,54,0,0,304,
        314,5,65,0,0,305,306,10,11,0,0,306,307,5,54,0,0,307,308,5,65,0,0,
        308,310,5,48,0,0,309,311,3,36,18,0,310,309,1,0,0,0,310,311,1,0,0,
        0,311,312,1,0,0,0,312,314,5,49,0,0,313,257,1,0,0,0,313,260,1,0,0,
        0,313,263,1,0,0,0,313,266,1,0,0,0,313,269,1,0,0,0,313,272,1,0,0,
        0,313,275,1,0,0,0,313,278,1,0,0,0,313,281,1,0,0,0,313,284,1,0,0,
        0,313,287,1,0,0,0,313,290,1,0,0,0,313,293,1,0,0,0,313,296,1,0,0,
        0,313,299,1,0,0,0,313,302,1,0,0,0,313,305,1,0,0,0,314,317,1,0,0,
        0,315,313,1,0,0,0,315,316,1,0,0,0,316,35,1,0,0,0,317,315,1,0,0,0,
        318,323,3,34,17,0,319,320,5,55,0,0,320,322,3,34,17,0,321,319,1,0,
        0,0,322,325,1,0,0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,37,1,0,0,
        0,325,323,1,0,0,0,31,41,50,55,57,65,77,84,86,94,105,110,113,117,
        122,132,137,142,148,166,170,180,201,206,211,236,239,255,310,313,
        315,323
    ]

class OPLangParser ( Parser ):

    grammarFileName = "OPLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'\\'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", 
                     "'||'", "'!'", "'^'", "':='", "'='", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "';'", "':'", "'.'", "','", 
                     "'~'", "'&'" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "BACKSLASH", "EQ", "NEQ", "GT", 
                      "LT", "GTE", "LTE", "AND", "OR", "NOT", "CONCAT", 
                      "ASSIGN_OP", "ASSIGN", "LSB", "RSB", "LP", "RP", "LCB", 
                      "RCB", "SEMI", "COLON", "DOT", "COMMA", "TILDE", "AMPERSAND", 
                      "INT_LIT", "FLOAT_LIT", "ERROR_FLOAT", "STRING_LIT", 
                      "STRING_LITERAL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "IDENTIFIER", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_vardecl = 2
    RULE_varList = 3
    RULE_var = 4
    RULE_arrayInit = 5
    RULE_funcdecl = 6
    RULE_paramlist = 7
    RULE_param = 8
    RULE_block = 9
    RULE_stmt = 10
    RULE_return = 11
    RULE_ifstmt = 12
    RULE_forstmt = 13
    RULE_datatype = 14
    RULE_basetype = 15
    RULE_modifier = 16
    RULE_expr = 17
    RULE_arglist = 18

    ruleNames =  [ "program", "classdecl", "vardecl", "varList", "var", 
                   "arrayInit", "funcdecl", "paramlist", "param", "block", 
                   "stmt", "return", "ifstmt", "forstmt", "datatype", "basetype", 
                   "modifier", "expr", "arglist" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INT=10
    NEW=11
    STRING=12
    THEN=13
    FOR=14
    RETURN=15
    TRUE=16
    FALSE=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    WS=25
    LINE_COMMENT=26
    BLOCK_COMMENT=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    BACKSLASH=33
    EQ=34
    NEQ=35
    GT=36
    LT=37
    GTE=38
    LTE=39
    AND=40
    OR=41
    NOT=42
    CONCAT=43
    ASSIGN_OP=44
    ASSIGN=45
    LSB=46
    RSB=47
    LP=48
    RP=49
    LCB=50
    RCB=51
    SEMI=52
    COLON=53
    DOT=54
    COMMA=55
    TILDE=56
    AMPERSAND=57
    INT_LIT=58
    FLOAT_LIT=59
    ERROR_FLOAT=60
    STRING_LIT=61
    STRING_LITERAL=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    IDENTIFIER=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OPLangParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_program




    def program(self):

        localctx = OPLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 38
                self.classdecl()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(OPLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(OPLangParser.CLASS, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.IDENTIFIER)
            else:
                return self.getToken(OPLangParser.IDENTIFIER, i)

        def LCB(self):
            return self.getToken(OPLangParser.LCB, 0)

        def RCB(self):
            return self.getToken(OPLangParser.RCB, 0)

        def EXTENDS(self):
            return self.getToken(OPLangParser.EXTENDS, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.VardeclContext)
            else:
                return self.getTypedRuleContext(OPLangParser.VardeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(OPLangParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_classdecl




    def classdecl(self):

        localctx = OPLangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(OPLangParser.CLASS)
            self.state = 47
            self.match(OPLangParser.IDENTIFIER)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 48
                self.match(OPLangParser.EXTENDS)
                self.state = 49
                self.match(OPLangParser.IDENTIFIER)


            self.state = 52
            self.match(OPLangParser.LCB)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6558978) != 0) or _la==65:
                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 53
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 54
                    self.funcdecl()
                    pass


                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(OPLangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datatype(self):
            return self.getTypedRuleContext(OPLangParser.DatatypeContext,0)


        def varList(self):
            return self.getTypedRuleContext(OPLangParser.VarListContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ModifierContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ModifierContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_vardecl




    def vardecl(self):

        localctx = OPLangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 62
                self.modifier()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.datatype()
            self.state = 69
            self.varList()
            self.state = 70
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.VarContext)
            else:
                return self.getTypedRuleContext(OPLangParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_varList




    def varList(self):

        localctx = OPLangParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.var()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 73
                self.match(OPLangParser.COMMA)
                self.state = 74
                self.var()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(OPLangParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_var




    def var(self):

        localctx = OPLangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(OPLangParser.IDENTIFIER)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 81
                self.match(OPLangParser.ASSIGN)
                self.state = 84
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 16, 17, 19, 48, 58, 59, 61, 65]:
                    self.state = 82
                    self.expr(0)
                    pass
                elif token in [50]:
                    self.state = 83
                    self.arrayInit()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(OPLangParser.LCB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ExprContext,i)


        def RCB(self):
            return self.getToken(OPLangParser.RCB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def arrayInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ArrayInitContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ArrayInitContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_arrayInit




    def arrayInit(self):

        localctx = OPLangParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(OPLangParser.LCB)
                self.state = 89
                self.expr(0)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 90
                    self.match(OPLangParser.COMMA)
                    self.state = 91
                    self.expr(0)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.match(OPLangParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(OPLangParser.LCB)
                self.state = 100
                self.arrayInit()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 101
                    self.match(OPLangParser.COMMA)
                    self.state = 102
                    self.arrayInit()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 108
                self.match(OPLangParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datatype(self):
            return self.getTypedRuleContext(OPLangParser.DatatypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(OPLangParser.LP, 0)

        def RP(self):
            return self.getToken(OPLangParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(OPLangParser.BlockContext,0)


        def modifier(self):
            return self.getTypedRuleContext(OPLangParser.ModifierContext,0)


        def AMPERSAND(self):
            return self.getToken(OPLangParser.AMPERSAND, 0)

        def paramlist(self):
            return self.getTypedRuleContext(OPLangParser.ParamlistContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_funcdecl




    def funcdecl(self):

        localctx = OPLangParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21 or _la==22:
                self.state = 112
                self.modifier()


            self.state = 115
            self.datatype()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 116
                self.match(OPLangParser.AMPERSAND)


            self.state = 119
            self.match(OPLangParser.IDENTIFIER)
            self.state = 120
            self.match(OPLangParser.LP)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 267522) != 0) or _la==65:
                self.state = 121
                self.paramlist()


            self.state = 124
            self.match(OPLangParser.RP)
            self.state = 125
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ParamContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.SEMI)
            else:
                return self.getToken(OPLangParser.SEMI, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_paramlist




    def paramlist(self):

        localctx = OPLangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.param()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 128
                self.match(OPLangParser.SEMI)
                self.state = 129
                self.param()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datatype(self):
            return self.getTypedRuleContext(OPLangParser.DatatypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def AMPERSAND(self):
            return self.getToken(OPLangParser.AMPERSAND, 0)

        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_param




    def param(self):

        localctx = OPLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.datatype()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 136
                self.match(OPLangParser.AMPERSAND)


            self.state = 139
            self.match(OPLangParser.IDENTIFIER)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 140
                self.match(OPLangParser.ASSIGN)
                self.state = 141
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(OPLangParser.LCB, 0)

        def RCB(self):
            return self.getToken(OPLangParser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(OPLangParser.StmtContext,i)


        def getRuleIndex(self):
            return OPLangParser.RULE_block




    def block(self):

        localctx = OPLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(OPLangParser.LCB)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3171941512559714050) != 0) or _la==65:
                self.state = 145
                self.stmt()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(OPLangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(OPLangParser.VardeclContext,0)


        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(OPLangParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(OPLangParser.BlockContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(OPLangParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(OPLangParser.ForstmtContext,0)


        def return_(self):
            return self.getTypedRuleContext(OPLangParser.ReturnContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_stmt




    def stmt(self):

        localctx = OPLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(OPLangParser.IDENTIFIER)
                self.state = 155
                self.match(OPLangParser.ASSIGN_OP)
                self.state = 156
                self.expr(0)
                self.state = 157
                self.match(OPLangParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.expr(0)
                self.state = 161
                self.match(OPLangParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.ifstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.return_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(OPLangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(OPLangParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_return




    def return_(self):

        localctx = OPLangParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(OPLangParser.RETURN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & 19562648320344417) != 0):
                self.state = 169
                self.expr(0)


            self.state = 172
            self.match(OPLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(OPLangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(OPLangParser.ExprContext,0)


        def THEN(self):
            return self.getToken(OPLangParser.THEN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(OPLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(OPLangParser.ELSE, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_ifstmt




    def ifstmt(self):

        localctx = OPLangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(OPLangParser.IF)
            self.state = 175
            self.expr(0)
            self.state = 176
            self.match(OPLangParser.THEN)
            self.state = 177
            self.block()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 178
                self.match(OPLangParser.ELSE)
                self.state = 179
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(OPLangParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(OPLangParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ExprContext,i)


        def DO(self):
            return self.getToken(OPLangParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(OPLangParser.BlockContext,0)


        def TO(self):
            return self.getToken(OPLangParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(OPLangParser.DOWNTO, 0)

        def datatype(self):
            return self.getTypedRuleContext(OPLangParser.DatatypeContext,0)


        def ASSIGN(self):
            return self.getToken(OPLangParser.ASSIGN, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_forstmt




    def forstmt(self):

        localctx = OPLangParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(OPLangParser.FOR)
                self.state = 183
                self.match(OPLangParser.IDENTIFIER)
                self.state = 184
                self.match(OPLangParser.ASSIGN_OP)
                self.state = 185
                self.expr(0)
                self.state = 186
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 187
                self.expr(0)
                self.state = 188
                self.match(OPLangParser.DO)
                self.state = 189
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(OPLangParser.FOR)
                self.state = 192
                self.datatype()
                self.state = 193
                self.match(OPLangParser.IDENTIFIER)
                self.state = 194
                self.match(OPLangParser.ASSIGN)
                self.state = 195
                self.expr(0)
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.expr(0)
                self.state = 198
                self.match(OPLangParser.DO)
                self.state = 199
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basetype(self):
            return self.getTypedRuleContext(OPLangParser.BasetypeContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.LSB)
            else:
                return self.getToken(OPLangParser.LSB, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.RSB)
            else:
                return self.getToken(OPLangParser.RSB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.INT_LIT)
            else:
                return self.getToken(OPLangParser.INT_LIT, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_datatype




    def datatype(self):

        localctx = OPLangParser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.basetype()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 204
                self.match(OPLangParser.LSB)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==58:
                    self.state = 205
                    self.match(OPLangParser.INT_LIT)


                self.state = 208
                self.match(OPLangParser.RSB)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(OPLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(OPLangParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(OPLangParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(OPLangParser.STRING, 0)

        def VOID(self):
            return self.getToken(OPLangParser.VOID, 0)

        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_basetype




    def basetype(self):

        localctx = OPLangParser.BasetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_basetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 267522) != 0) or _la==65):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(OPLangParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(OPLangParser.FINAL, 0)

        def getRuleIndex(self):
            return OPLangParser.RULE_modifier




    def modifier(self):

        localctx = OPLangParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(OPLangParser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ExprContext,i)


        def RP(self):
            return self.getToken(OPLangParser.RP, 0)

        def IDENTIFIER(self):
            return self.getToken(OPLangParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(OPLangParser.LSB, 0)

        def RSB(self):
            return self.getToken(OPLangParser.RSB, 0)

        def NEW(self):
            return self.getToken(OPLangParser.NEW, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def INT_LIT(self):
            return self.getToken(OPLangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(OPLangParser.FLOAT_LIT, 0)

        def TRUE(self):
            return self.getToken(OPLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(OPLangParser.FALSE, 0)

        def STRING_LIT(self):
            return self.getToken(OPLangParser.STRING_LIT, 0)

        def NIL(self):
            return self.getToken(OPLangParser.NIL, 0)

        def ADD(self):
            return self.getToken(OPLangParser.ADD, 0)

        def SUB(self):
            return self.getToken(OPLangParser.SUB, 0)

        def MUL(self):
            return self.getToken(OPLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(OPLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(OPLangParser.MOD, 0)

        def EQ(self):
            return self.getToken(OPLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(OPLangParser.NEQ, 0)

        def GT(self):
            return self.getToken(OPLangParser.GT, 0)

        def LT(self):
            return self.getToken(OPLangParser.LT, 0)

        def GTE(self):
            return self.getToken(OPLangParser.GTE, 0)

        def LTE(self):
            return self.getToken(OPLangParser.LTE, 0)

        def AND(self):
            return self.getToken(OPLangParser.AND, 0)

        def OR(self):
            return self.getToken(OPLangParser.OR, 0)

        def CONCAT(self):
            return self.getToken(OPLangParser.CONCAT, 0)

        def ASSIGN_OP(self):
            return self.getToken(OPLangParser.ASSIGN_OP, 0)

        def DOT(self):
            return self.getToken(OPLangParser.DOT, 0)

        def arglist(self):
            return self.getTypedRuleContext(OPLangParser.ArglistContext,0)


        def getRuleIndex(self):
            return OPLangParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OPLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 219
                self.match(OPLangParser.LP)
                self.state = 220
                self.expr(0)
                self.state = 221
                self.match(OPLangParser.RP)
                pass

            elif la_ == 2:
                self.state = 223
                self.match(OPLangParser.IDENTIFIER)
                self.state = 224
                self.match(OPLangParser.LSB)
                self.state = 225
                self.expr(0)
                self.state = 226
                self.match(OPLangParser.RSB)
                pass

            elif la_ == 3:
                self.state = 228
                self.match(OPLangParser.NEW)
                self.state = 229
                self.match(OPLangParser.IDENTIFIER)
                self.state = 230
                self.match(OPLangParser.LP)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & 19562648320344417) != 0):
                    self.state = 231
                    self.expr(0)
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==55:
                        self.state = 232
                        self.match(OPLangParser.COMMA)
                        self.state = 233
                        self.expr(0)
                        self.state = 238
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 241
                self.match(OPLangParser.RP)
                pass

            elif la_ == 4:
                self.state = 242
                self.match(OPLangParser.NEW)
                self.state = 243
                self.match(OPLangParser.IDENTIFIER)
                self.state = 244
                self.match(OPLangParser.LSB)
                self.state = 245
                self.expr(0)
                self.state = 246
                self.match(OPLangParser.RSB)
                pass

            elif la_ == 5:
                self.state = 248
                self.match(OPLangParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 249
                self.match(OPLangParser.INT_LIT)
                pass

            elif la_ == 7:
                self.state = 250
                self.match(OPLangParser.FLOAT_LIT)
                pass

            elif la_ == 8:
                self.state = 251
                self.match(OPLangParser.TRUE)
                pass

            elif la_ == 9:
                self.state = 252
                self.match(OPLangParser.FALSE)
                pass

            elif la_ == 10:
                self.state = 253
                self.match(OPLangParser.STRING_LIT)
                pass

            elif la_ == 11:
                self.state = 254
                self.match(OPLangParser.NIL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 257
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 258
                        self.match(OPLangParser.ADD)
                        self.state = 259
                        self.expr(29)
                        pass

                    elif la_ == 2:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 260
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 261
                        self.match(OPLangParser.SUB)
                        self.state = 262
                        self.expr(28)
                        pass

                    elif la_ == 3:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 263
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 264
                        self.match(OPLangParser.MUL)
                        self.state = 265
                        self.expr(27)
                        pass

                    elif la_ == 4:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 266
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 267
                        self.match(OPLangParser.DIV)
                        self.state = 268
                        self.expr(26)
                        pass

                    elif la_ == 5:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 269
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 270
                        self.match(OPLangParser.MOD)
                        self.state = 271
                        self.expr(25)
                        pass

                    elif la_ == 6:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 272
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 273
                        self.match(OPLangParser.EQ)
                        self.state = 274
                        self.expr(24)
                        pass

                    elif la_ == 7:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 275
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 276
                        self.match(OPLangParser.NEQ)
                        self.state = 277
                        self.expr(23)
                        pass

                    elif la_ == 8:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 278
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 279
                        self.match(OPLangParser.GT)
                        self.state = 280
                        self.expr(22)
                        pass

                    elif la_ == 9:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 281
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 282
                        self.match(OPLangParser.LT)
                        self.state = 283
                        self.expr(21)
                        pass

                    elif la_ == 10:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 284
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 285
                        self.match(OPLangParser.GTE)
                        self.state = 286
                        self.expr(20)
                        pass

                    elif la_ == 11:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 287
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 288
                        self.match(OPLangParser.LTE)
                        self.state = 289
                        self.expr(19)
                        pass

                    elif la_ == 12:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 290
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 291
                        self.match(OPLangParser.AND)
                        self.state = 292
                        self.expr(18)
                        pass

                    elif la_ == 13:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 293
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 294
                        self.match(OPLangParser.OR)
                        self.state = 295
                        self.expr(17)
                        pass

                    elif la_ == 14:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 297
                        self.match(OPLangParser.CONCAT)
                        self.state = 298
                        self.expr(16)
                        pass

                    elif la_ == 15:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 299
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 300
                        self.match(OPLangParser.ASSIGN_OP)
                        self.state = 301
                        self.expr(15)
                        pass

                    elif la_ == 16:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 302
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 303
                        self.match(OPLangParser.DOT)
                        self.state = 304
                        self.match(OPLangParser.IDENTIFIER)
                        pass

                    elif la_ == 17:
                        localctx = OPLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 305
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 306
                        self.match(OPLangParser.DOT)
                        self.state = 307
                        self.match(OPLangParser.IDENTIFIER)
                        self.state = 308
                        self.match(OPLangParser.LP)
                        self.state = 310
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & 19562648320344417) != 0):
                            self.state = 309
                            self.arglist()


                        self.state = 312
                        self.match(OPLangParser.RP)
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OPLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(OPLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(OPLangParser.COMMA)
            else:
                return self.getToken(OPLangParser.COMMA, i)

        def getRuleIndex(self):
            return OPLangParser.RULE_arglist




    def arglist(self):

        localctx = OPLangParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr(0)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 319
                self.match(OPLangParser.COMMA)
                self.state = 320
                self.expr(0)
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 11)
         




