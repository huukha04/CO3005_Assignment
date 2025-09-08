# Generated from c:\Users\khahu\Desktop\CO3005_ASS\oplang-compiler\src\grammar\OPLang copy.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0171\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u00f8\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u00ff\n")
        buf.write("\34\3\35\3\35\3\35\5\35\u0104\n\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\6*\u011f\n*\r*\16*\u0120\3+\6+\u0124\n+")
        buf.write("\r+\16+\u0125\3+\3+\7+\u012a\n+\f+\16+\u012d\13+\5+\u012f")
        buf.write("\n+\3+\3+\5+\u0133\n+\3+\6+\u0136\n+\r+\16+\u0137\5+\u013a")
        buf.write("\n+\3,\3,\3,\3,\7,\u0140\n,\f,\16,\u0143\13,\3,\3,\3-")
        buf.write("\3-\7-\u0149\n-\f-\16-\u014c\13-\3.\6.\u014f\n.\r.\16")
        buf.write(".\u0150\3.\3.\3/\3/\7/\u0157\n/\f/\16/\u015a\13/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\7\60\u0162\n\60\f\60\16\60\u0165")
        buf.write("\13\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\u0163\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("\3\2\r\7\2\'\',-//\61\61^^\4\2>>@@\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\2\u0184")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3g\3")
        buf.write("\2\2\2\5o\3\2\2\2\7u\3\2\2\2\t{\3\2\2\2\13\u0084\3\2\2")
        buf.write("\2\r\u0087\3\2\2\2\17\u008c\3\2\2\2\21\u0094\3\2\2\2\23")
        buf.write("\u009a\3\2\2\2\25\u009d\3\2\2\2\27\u00a1\3\2\2\2\31\u00a5")
        buf.write("\3\2\2\2\33\u00ac\3\2\2\2\35\u00b1\3\2\2\2\37\u00b5\3")
        buf.write("\2\2\2!\u00bc\3\2\2\2#\u00c1\3\2\2\2%\u00c7\3\2\2\2\'")
        buf.write("\u00cc\3\2\2\2)\u00d0\3\2\2\2+\u00d5\3\2\2\2-\u00db\3")
        buf.write("\2\2\2/\u00e2\3\2\2\2\61\u00e5\3\2\2\2\63\u00ec\3\2\2")
        buf.write("\2\65\u00f7\3\2\2\2\67\u00fe\3\2\2\29\u0103\3\2\2\2;\u0105")
        buf.write("\3\2\2\2=\u0107\3\2\2\2?\u0109\3\2\2\2A\u010b\3\2\2\2")
        buf.write("C\u010d\3\2\2\2E\u010f\3\2\2\2G\u0111\3\2\2\2I\u0113\3")
        buf.write("\2\2\2K\u0115\3\2\2\2M\u0117\3\2\2\2O\u0119\3\2\2\2Q\u011b")
        buf.write("\3\2\2\2S\u011e\3\2\2\2U\u0123\3\2\2\2W\u013b\3\2\2\2")
        buf.write("Y\u0146\3\2\2\2[\u014e\3\2\2\2]\u0154\3\2\2\2_\u015d\3")
        buf.write("\2\2\2a\u016b\3\2\2\2c\u016d\3\2\2\2e\u016f\3\2\2\2gh")
        buf.write("\7d\2\2hi\7q\2\2ij\7q\2\2jk\7n\2\2kl\7g\2\2lm\7c\2\2m")
        buf.write("n\7p\2\2n\4\3\2\2\2op\7d\2\2pq\7t\2\2qr\7g\2\2rs\7c\2")
        buf.write("\2st\7m\2\2t\6\3\2\2\2uv\7e\2\2vw\7n\2\2wx\7c\2\2xy\7")
        buf.write("u\2\2yz\7u\2\2z\b\3\2\2\2{|\7e\2\2|}\7q\2\2}~\7p\2\2~")
        buf.write("\177\7v\2\2\177\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081")
        buf.write("\u0082\7w\2\2\u0082\u0083\7g\2\2\u0083\n\3\2\2\2\u0084")
        buf.write("\u0085\7f\2\2\u0085\u0086\7q\2\2\u0086\f\3\2\2\2\u0087")
        buf.write("\u0088\7g\2\2\u0088\u0089\7n\2\2\u0089\u008a\7u\2\2\u008a")
        buf.write("\u008b\7g\2\2\u008b\16\3\2\2\2\u008c\u008d\7g\2\2\u008d")
        buf.write("\u008e\7z\2\2\u008e\u008f\7v\2\2\u008f\u0090\7g\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\u0092\7f\2\2\u0092\u0093\7u\2\2\u0093")
        buf.write("\20\3\2\2\2\u0094\u0095\7h\2\2\u0095\u0096\7n\2\2\u0096")
        buf.write("\u0097\7q\2\2\u0097\u0098\7c\2\2\u0098\u0099\7v\2\2\u0099")
        buf.write("\22\3\2\2\2\u009a\u009b\7k\2\2\u009b\u009c\7h\2\2\u009c")
        buf.write("\24\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f")
        buf.write("\u00a0\7v\2\2\u00a0\26\3\2\2\2\u00a1\u00a2\7p\2\2\u00a2")
        buf.write("\u00a3\7g\2\2\u00a3\u00a4\7y\2\2\u00a4\30\3\2\2\2\u00a5")
        buf.write("\u00a6\7u\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7t\2\2\u00a8")
        buf.write("\u00a9\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7i\2\2\u00ab")
        buf.write("\32\3\2\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7j\2\2\u00ae")
        buf.write("\u00af\7g\2\2\u00af\u00b0\7p\2\2\u00b0\34\3\2\2\2\u00b1")
        buf.write("\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\36\3\2\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7")
        buf.write("\u00b8\7v\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7p\2\2\u00bb \3\2\2\2\u00bc\u00bd\7v\2\2\u00bd")
        buf.write("\u00be\7t\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\"\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7c\2\2\u00c3")
        buf.write("\u00c4\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("$\3\2\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9\7q\2\2\u00c9")
        buf.write("\u00ca\7k\2\2\u00ca\u00cb\7f\2\2\u00cb&\3\2\2\2\u00cc")
        buf.write("\u00cd\7p\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7n\2\2\u00cf")
        buf.write("(\3\2\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7j\2\2\u00d2")
        buf.write("\u00d3\7k\2\2\u00d3\u00d4\7u\2\2\u00d4*\3\2\2\2\u00d5")
        buf.write("\u00d6\7h\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7n\2\2\u00da,\3\2\2\2\u00db")
        buf.write("\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7c\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7e\2\2\u00e1")
        buf.write(".\3\2\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\60\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7q\2\2\u00e7")
        buf.write("\u00e8\7y\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7q\2\2\u00eb\62\3\2\2\2\u00ec\u00ed\t\2\2\2\u00ed")
        buf.write("\64\3\2\2\2\u00ee\u00ef\7#\2\2\u00ef\u00f8\7?\2\2\u00f0")
        buf.write("\u00f1\7?\2\2\u00f1\u00f8\7?\2\2\u00f2\u00f3\7@\2\2\u00f3")
        buf.write("\u00f8\7?\2\2\u00f4\u00f5\7>\2\2\u00f5\u00f8\7?\2\2\u00f6")
        buf.write("\u00f8\t\3\2\2\u00f7\u00ee\3\2\2\2\u00f7\u00f0\3\2\2\2")
        buf.write("\u00f7\u00f2\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f7\u00f6\3")
        buf.write("\2\2\2\u00f8\66\3\2\2\2\u00f9\u00fa\7(\2\2\u00fa\u00ff")
        buf.write("\7(\2\2\u00fb\u00fc\7~\2\2\u00fc\u00ff\7~\2\2\u00fd\u00ff")
        buf.write("\7#\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fb\3\2\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff8\3\2\2\2\u0100\u0104\7`\2\2\u0101")
        buf.write("\u0102\7<\2\2\u0102\u0104\7?\2\2\u0103\u0100\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0104:\3\2\2\2\u0105\u0106\7]\2\2\u0106")
        buf.write("<\3\2\2\2\u0107\u0108\7_\2\2\u0108>\3\2\2\2\u0109\u010a")
        buf.write("\7*\2\2\u010a@\3\2\2\2\u010b\u010c\7+\2\2\u010cB\3\2\2")
        buf.write("\2\u010d\u010e\7}\2\2\u010eD\3\2\2\2\u010f\u0110\7\177")
        buf.write("\2\2\u0110F\3\2\2\2\u0111\u0112\7=\2\2\u0112H\3\2\2\2")
        buf.write("\u0113\u0114\7<\2\2\u0114J\3\2\2\2\u0115\u0116\7\60\2")
        buf.write("\2\u0116L\3\2\2\2\u0117\u0118\7.\2\2\u0118N\3\2\2\2\u0119")
        buf.write("\u011a\7\u0080\2\2\u011aP\3\2\2\2\u011b\u011c\7(\2\2\u011c")
        buf.write("R\3\2\2\2\u011d\u011f\t\4\2\2\u011e\u011d\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121T\3\2\2\2\u0122\u0124\t\4\2\2\u0123\u0122\3\2\2")
        buf.write("\2\u0124\u0125\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u012e\3\2\2\2\u0127\u012b\7\60\2\2\u0128")
        buf.write("\u012a\t\4\2\2\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012f\3")
        buf.write("\2\2\2\u012d\u012b\3\2\2\2\u012e\u0127\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0139\3\2\2\2\u0130\u0132\t\5\2\2\u0131")
        buf.write("\u0133\t\6\2\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0135\3\2\2\2\u0134\u0136\t\4\2\2\u0135\u0134\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0130\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013aV\3\2\2\2\u013b\u0141\7$\2\2\u013c")
        buf.write("\u0140\n\7\2\2\u013d\u013e\7^\2\2\u013e\u0140\t\b\2\2")
        buf.write("\u013f\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0143\3")
        buf.write("\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7$\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u014a\t\t\2\2\u0147\u0149\t\n\2\2\u0148")
        buf.write("\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014bZ\3\2\2\2\u014c\u014a\3\2\2")
        buf.write("\2\u014d\u014f\t\13\2\2\u014e\u014d\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\b.\2\2\u0153\\\3\2\2\2\u0154")
        buf.write("\u0158\7%\2\2\u0155\u0157\n\f\2\2\u0156\u0155\3\2\2\2")
        buf.write("\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c")
        buf.write("\b/\2\2\u015c^\3\2\2\2\u015d\u015e\7\61\2\2\u015e\u015f")
        buf.write("\7,\2\2\u015f\u0163\3\2\2\2\u0160\u0162\13\2\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\7,\2\2\u0167\u0168\7\61\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\b\60\2\2\u016a`\3\2\2\2\u016b\u016c")
        buf.write("\13\2\2\2\u016cb\3\2\2\2\u016d\u016e\13\2\2\2\u016ed\3")
        buf.write("\2\2\2\u016f\u0170\13\2\2\2\u0170f\3\2\2\2\23\2\u00f7")
        buf.write("\u00fe\u0103\u0120\u0125\u012b\u012e\u0132\u0137\u0139")
        buf.write("\u013f\u0141\u014a\u0150\u0158\u0163\3\b\2\2")
        return buf.getvalue()


class OPLangddLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    NEW = 11
    STRING = 12
    THEN = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    ARITH_OP = 25
    REL_OP = 26
    LOGIC_OP = 27
    OTHER_OP = 28
    LSB = 29
    RSB = 30
    LP = 31
    RP = 32
    LCB = 33
    RCB = 34
    SEMI = 35
    COLON = 36
    DOT = 37
    COMMA = 38
    TILDE = 39
    AMPERSAND = 40
    INT_LIT = 41
    FLOAT_LIT = 42
    STRING_LIT = 43
    IDENTIFIER = 44
    CHARACTER_SET = 45
    LINE_COMMENT = 46
    BLOCK_COMMENT = 47
    ERROR_CHAR = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", "'.'", 
            "','", "'~'", "'&'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "ARITH_OP", "REL_OP", "LOGIC_OP", "OTHER_OP", "LSB", 
            "RSB", "LP", "RP", "LCB", "RCB", "SEMI", "COLON", "DOT", "COMMA", 
            "TILDE", "AMPERSAND", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "IDENTIFIER", "CHARACTER_SET", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "ARITH_OP", "REL_OP", 
                  "LOGIC_OP", "OTHER_OP", "LSB", "RSB", "LP", "RP", "LCB", 
                  "RCB", "SEMI", "COLON", "DOT", "COMMA", "TILDE", "AMPERSAND", 
                  "INT_LIT", "FLOAT_LIT", "STRING_LIT", "IDENTIFIER", "CHARACTER_SET", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "OPLang copy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


