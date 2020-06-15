# Generated from Enquestes.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("t\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\2\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\6\3&\n")
        buf.write("\3\r\3\16\3\'\3\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\4")
        buf.write("\3\4\7\4\64\n\4\f\4\16\4\67\13\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\6\6C\n\6\r\6\16\6D\3\6\7\6H\n\6\f\6")
        buf.write("\16\6K\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t_\n\t\f\t\16\tb\13\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\6\13n\n\13")
        buf.write("\r\13\16\13o\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22")
        buf.write("\24\2\2\2r\2\27\3\2\2\2\4\37\3\2\2\2\6/\3\2\2\2\b:\3\2")
        buf.write("\2\2\nI\3\2\2\2\fL\3\2\2\2\16S\3\2\2\2\20[\3\2\2\2\22")
        buf.write("c\3\2\2\2\24i\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\5\24\13\2\34\35\7\2\2\3\35\3\3\2\2\2\36 \5\6\4\2\37")
        buf.write("\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2")
        buf.write("\2#%\5\b\5\2$&\5\f\7\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2")
        buf.write("\'(\3\2\2\2(,\3\2\2\2)+\5\16\b\2*)\3\2\2\2+.\3\2\2\2,")
        buf.write("*\3\2\2\2,-\3\2\2\2-\5\3\2\2\2.,\3\2\2\2/\60\7\23\2\2")
        buf.write("\60\61\7\21\2\2\61\65\7\3\2\2\62\64\7\23\2\2\63\62\3\2")
        buf.write("\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2")
        buf.write("\2\2\67\65\3\2\2\289\7\20\2\29\7\3\2\2\2:;\7\23\2\2;<")
        buf.write("\7\21\2\2<=\7\4\2\2=>\5\n\6\2>\t\3\2\2\2?@\7\22\2\2@B")
        buf.write("\7\21\2\2AC\7\23\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3")
        buf.write("\2\2\2EF\3\2\2\2FH\7\17\2\2G?\3\2\2\2HK\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\7\23\2\2MN\7\21")
        buf.write("\2\2NO\7\5\2\2OP\7\23\2\2PQ\7\t\2\2QR\7\23\2\2R\r\3\2")
        buf.write("\2\2ST\7\23\2\2TU\7\21\2\2UV\7\7\2\2VW\7\23\2\2WX\7\f")
        buf.write("\2\2XY\5\20\t\2YZ\7\r\2\2Z\17\3\2\2\2[`\5\22\n\2\\]\7")
        buf.write("\16\2\2]_\5\22\n\2^\\\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3")
        buf.write("\2\2\2a\21\3\2\2\2b`\3\2\2\2cd\7\n\2\2de\7\22\2\2ef\7")
        buf.write("\16\2\2fg\7\23\2\2gh\7\13\2\2h\23\3\2\2\2ij\7\23\2\2j")
        buf.write("k\7\21\2\2km\7\6\2\2ln\7\23\2\2ml\3\2\2\2no\3\2\2\2om")
        buf.write("\3\2\2\2op\3\2\2\2pq\3\2\2\2qr\7\b\2\2r\25\3\2\2\2\13")
        buf.write("\31!\',\65DI`o")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PREGUNTA'", "'RESPOSTA'", "'ITEM'", 
                     "'ENQUESTA'", "'ALTERNATIVA'", "'END'", "'->'", "'('", 
                     "')'", "'['", "']'", "','", "';'", "'?'", "':'" ]

    symbolicNames = [ "<INVALID>", "PREGUNTA", "RESPOSTA", "ITEM", "ENQUESTA", 
                      "ALTERNATIVA", "END", "FLETXA", "OP", "CP", "OC", 
                      "CC", "COMA", "PUNTICOMA", "INTERROGANT", "DOSPUNTS", 
                      "NUM", "ID", "WS" ]

    RULE_r = 0
    RULE_tanda = 1
    RULE_pregunta = 2
    RULE_resposta = 3
    RULE_opcions = 4
    RULE_item = 5
    RULE_alternativa = 6
    RULE_implicacio = 7
    RULE_implicacions = 8
    RULE_enquesta = 9

    ruleNames =  [ "r", "tanda", "pregunta", "resposta", "opcions", "item", 
                   "alternativa", "implicacio", "implicacions", "enquesta" ]

    EOF = Token.EOF
    PREGUNTA=1
    RESPOSTA=2
    ITEM=3
    ENQUESTA=4
    ALTERNATIVA=5
    END=6
    FLETXA=7
    OP=8
    CP=9
    OC=10
    CC=11
    COMA=12
    PUNTICOMA=13
    INTERROGANT=14
    DOSPUNTS=15
    NUM=16
    ID=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def tanda(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.TandaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.TandaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_r

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = EnquestesParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 20
                    self.tanda()

                else:
                    raise NoViableAltException(self)
                self.state = 23 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 25
            self.enquesta()
            self.state = 26
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TandaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resposta(self):
            return self.getTypedRuleContext(EnquestesParser.RespostaContext,0)


        def pregunta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.PreguntaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.PreguntaContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemContext,i)


        def alternativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlternativaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlternativaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_tanda

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanda" ):
                return visitor.visitTanda(self)
            else:
                return visitor.visitChildren(self)




    def tanda(self):

        localctx = EnquestesParser.TandaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tanda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 28
                    self.pregunta()

                else:
                    raise NoViableAltException(self)
                self.state = 31 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 33
            self.resposta()
            self.state = 35 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 34
                    self.item()

                else:
                    raise NoViableAltException(self)
                self.state = 37 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 39
                    self.alternativa() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreguntaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def DOSPUNTS(self):
            return self.getToken(EnquestesParser.DOSPUNTS, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def INTERROGANT(self):
            return self.getToken(EnquestesParser.INTERROGANT, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_pregunta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPregunta" ):
                return visitor.visitPregunta(self)
            else:
                return visitor.visitChildren(self)




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pregunta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(EnquestesParser.ID)
            self.state = 46
            self.match(EnquestesParser.DOSPUNTS)
            self.state = 47
            self.match(EnquestesParser.PREGUNTA)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.ID:
                self.state = 48
                self.match(EnquestesParser.ID)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(EnquestesParser.INTERROGANT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def DOSPUNTS(self):
            return self.getToken(EnquestesParser.DOSPUNTS, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def opcions(self):
            return self.getTypedRuleContext(EnquestesParser.OpcionsContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResposta" ):
                return visitor.visitResposta(self)
            else:
                return visitor.visitChildren(self)




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(EnquestesParser.ID)
            self.state = 57
            self.match(EnquestesParser.DOSPUNTS)
            self.state = 58
            self.match(EnquestesParser.RESPOSTA)
            self.state = 59
            self.opcions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.NUM)
            else:
                return self.getToken(EnquestesParser.NUM, i)

        def DOSPUNTS(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.DOSPUNTS)
            else:
                return self.getToken(EnquestesParser.DOSPUNTS, i)

        def PUNTICOMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PUNTICOMA)
            else:
                return self.getToken(EnquestesParser.PUNTICOMA, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcions" ):
                return visitor.visitOpcions(self)
            else:
                return visitor.visitChildren(self)




    def opcions(self):

        localctx = EnquestesParser.OpcionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opcions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.NUM:
                self.state = 61
                self.match(EnquestesParser.NUM)
                self.state = 62
                self.match(EnquestesParser.DOSPUNTS)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.match(EnquestesParser.ID)
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==EnquestesParser.ID):
                        break

                self.state = 68
                self.match(EnquestesParser.PUNTICOMA)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def DOSPUNTS(self):
            return self.getToken(EnquestesParser.DOSPUNTS, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def FLETXA(self):
            return self.getToken(EnquestesParser.FLETXA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnquestesParser.ID)
            self.state = 75
            self.match(EnquestesParser.DOSPUNTS)
            self.state = 76
            self.match(EnquestesParser.ITEM)
            self.state = 77
            self.match(EnquestesParser.ID)
            self.state = 78
            self.match(EnquestesParser.FLETXA)
            self.state = 79
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def DOSPUNTS(self):
            return self.getToken(EnquestesParser.DOSPUNTS, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def OC(self):
            return self.getToken(EnquestesParser.OC, 0)

        def implicacio(self):
            return self.getTypedRuleContext(EnquestesParser.ImplicacioContext,0)


        def CC(self):
            return self.getToken(EnquestesParser.CC, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativa" ):
                return visitor.visitAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_alternativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(EnquestesParser.ID)
            self.state = 82
            self.match(EnquestesParser.DOSPUNTS)
            self.state = 83
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 84
            self.match(EnquestesParser.ID)
            self.state = 85
            self.match(EnquestesParser.OC)
            self.state = 86
            self.implicacio()
            self.state = 87
            self.match(EnquestesParser.CC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicacions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ImplicacionsContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ImplicacionsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.COMA)
            else:
                return self.getToken(EnquestesParser.COMA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_implicacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicacio" ):
                return visitor.visitImplicacio(self)
            else:
                return visitor.visitChildren(self)




    def implicacio(self):

        localctx = EnquestesParser.ImplicacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicacio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.implicacions()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.COMA:
                self.state = 90
                self.match(EnquestesParser.COMA)
                self.state = 91
                self.implicacions()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicacionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(EnquestesParser.OP, 0)

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COMA(self):
            return self.getToken(EnquestesParser.COMA, 0)

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def CP(self):
            return self.getToken(EnquestesParser.CP, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_implicacions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicacions" ):
                return visitor.visitImplicacions(self)
            else:
                return visitor.visitChildren(self)




    def implicacions(self):

        localctx = EnquestesParser.ImplicacionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicacions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(EnquestesParser.OP)
            self.state = 98
            self.match(EnquestesParser.NUM)
            self.state = 99
            self.match(EnquestesParser.COMA)
            self.state = 100
            self.match(EnquestesParser.ID)
            self.state = 101
            self.match(EnquestesParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def DOSPUNTS(self):
            return self.getToken(EnquestesParser.DOSPUNTS, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquesta" ):
                return visitor.visitEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(EnquestesParser.ID)
            self.state = 104
            self.match(EnquestesParser.DOSPUNTS)
            self.state = 105
            self.match(EnquestesParser.ENQUESTA)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.match(EnquestesParser.ID)
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

            self.state = 111
            self.match(EnquestesParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





