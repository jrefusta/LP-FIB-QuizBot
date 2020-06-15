// Generated from Enquestes.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class EnquestesParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PREGUNTA=1, RESPOSTA=2, ITEM=3, ENQUESTA=4, ALTERNATIVA=5, END=6, FLETXA=7, 
		OP=8, CP=9, OC=10, CC=11, COMA=12, PUNTICOMA=13, INTERROGANT=14, DOSPUNTS=15, 
		NUM=16, ID=17, WS=18;
	public static final int
		RULE_r = 0, RULE_tanda = 1, RULE_pregunta = 2, RULE_resposta = 3, RULE_opcions = 4, 
		RULE_item = 5, RULE_alternativa = 6, RULE_implicacio = 7, RULE_implicacions = 8, 
		RULE_enquesta = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"r", "tanda", "pregunta", "resposta", "opcions", "item", "alternativa", 
			"implicacio", "implicacions", "enquesta"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'PREGUNTA'", "'RESPOSTA'", "'ITEM'", "'ENQUESTA'", "'ALTERNATIVA'", 
			"'END'", "'->'", "'('", "')'", "'['", "']'", "','", "';'", "'?'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PREGUNTA", "RESPOSTA", "ITEM", "ENQUESTA", "ALTERNATIVA", "END", 
			"FLETXA", "OP", "CP", "OC", "CC", "COMA", "PUNTICOMA", "INTERROGANT", 
			"DOSPUNTS", "NUM", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Enquestes.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public EnquestesParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RContext extends ParserRuleContext {
		public EnquestaContext enquesta() {
			return getRuleContext(EnquestaContext.class,0);
		}
		public TerminalNode EOF() { return getToken(EnquestesParser.EOF, 0); }
		public List<TandaContext> tanda() {
			return getRuleContexts(TandaContext.class);
		}
		public TandaContext tanda(int i) {
			return getRuleContext(TandaContext.class,i);
		}
		public RContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_r; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterR(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitR(this);
		}
	}

	public final RContext r() throws RecognitionException {
		RContext _localctx = new RContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_r);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(21); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(20);
					tanda();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(23); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(25);
			enquesta();
			setState(26);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TandaContext extends ParserRuleContext {
		public RespostaContext resposta() {
			return getRuleContext(RespostaContext.class,0);
		}
		public List<PreguntaContext> pregunta() {
			return getRuleContexts(PreguntaContext.class);
		}
		public PreguntaContext pregunta(int i) {
			return getRuleContext(PreguntaContext.class,i);
		}
		public List<ItemContext> item() {
			return getRuleContexts(ItemContext.class);
		}
		public ItemContext item(int i) {
			return getRuleContext(ItemContext.class,i);
		}
		public List<AlternativaContext> alternativa() {
			return getRuleContexts(AlternativaContext.class);
		}
		public AlternativaContext alternativa(int i) {
			return getRuleContext(AlternativaContext.class,i);
		}
		public TandaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tanda; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterTanda(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitTanda(this);
		}
	}

	public final TandaContext tanda() throws RecognitionException {
		TandaContext _localctx = new TandaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tanda);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(29); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(28);
					pregunta();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(31); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(33);
			resposta();
			setState(35); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(34);
					item();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(37); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(42);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(39);
					alternativa();
					}
					} 
				}
				setState(44);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreguntaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public TerminalNode DOSPUNTS() { return getToken(EnquestesParser.DOSPUNTS, 0); }
		public TerminalNode PREGUNTA() { return getToken(EnquestesParser.PREGUNTA, 0); }
		public TerminalNode INTERROGANT() { return getToken(EnquestesParser.INTERROGANT, 0); }
		public PreguntaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pregunta; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterPregunta(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitPregunta(this);
		}
	}

	public final PreguntaContext pregunta() throws RecognitionException {
		PreguntaContext _localctx = new PreguntaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_pregunta);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(ID);
			setState(46);
			match(DOSPUNTS);
			setState(47);
			match(PREGUNTA);
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(48);
				match(ID);
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
			match(INTERROGANT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RespostaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(EnquestesParser.ID, 0); }
		public TerminalNode DOSPUNTS() { return getToken(EnquestesParser.DOSPUNTS, 0); }
		public TerminalNode RESPOSTA() { return getToken(EnquestesParser.RESPOSTA, 0); }
		public OpcionsContext opcions() {
			return getRuleContext(OpcionsContext.class,0);
		}
		public RespostaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_resposta; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterResposta(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitResposta(this);
		}
	}

	public final RespostaContext resposta() throws RecognitionException {
		RespostaContext _localctx = new RespostaContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_resposta);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(ID);
			setState(57);
			match(DOSPUNTS);
			setState(58);
			match(RESPOSTA);
			setState(59);
			opcions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpcionsContext extends ParserRuleContext {
		public List<TerminalNode> NUM() { return getTokens(EnquestesParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(EnquestesParser.NUM, i);
		}
		public List<TerminalNode> DOSPUNTS() { return getTokens(EnquestesParser.DOSPUNTS); }
		public TerminalNode DOSPUNTS(int i) {
			return getToken(EnquestesParser.DOSPUNTS, i);
		}
		public List<TerminalNode> PUNTICOMA() { return getTokens(EnquestesParser.PUNTICOMA); }
		public TerminalNode PUNTICOMA(int i) {
			return getToken(EnquestesParser.PUNTICOMA, i);
		}
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public OpcionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opcions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterOpcions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitOpcions(this);
		}
	}

	public final OpcionsContext opcions() throws RecognitionException {
		OpcionsContext _localctx = new OpcionsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_opcions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NUM) {
				{
				{
				setState(61);
				match(NUM);
				setState(62);
				match(DOSPUNTS);
				setState(64); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(63);
					match(ID);
					}
					}
					setState(66); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ID );
				setState(68);
				match(PUNTICOMA);
				}
				}
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public TerminalNode DOSPUNTS() { return getToken(EnquestesParser.DOSPUNTS, 0); }
		public TerminalNode ITEM() { return getToken(EnquestesParser.ITEM, 0); }
		public TerminalNode FLETXA() { return getToken(EnquestesParser.FLETXA, 0); }
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitItem(this);
		}
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_item);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(ID);
			setState(75);
			match(DOSPUNTS);
			setState(76);
			match(ITEM);
			setState(77);
			match(ID);
			setState(78);
			match(FLETXA);
			setState(79);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AlternativaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public TerminalNode DOSPUNTS() { return getToken(EnquestesParser.DOSPUNTS, 0); }
		public TerminalNode ALTERNATIVA() { return getToken(EnquestesParser.ALTERNATIVA, 0); }
		public TerminalNode OC() { return getToken(EnquestesParser.OC, 0); }
		public ImplicacioContext implicacio() {
			return getRuleContext(ImplicacioContext.class,0);
		}
		public TerminalNode CC() { return getToken(EnquestesParser.CC, 0); }
		public AlternativaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alternativa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterAlternativa(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitAlternativa(this);
		}
	}

	public final AlternativaContext alternativa() throws RecognitionException {
		AlternativaContext _localctx = new AlternativaContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_alternativa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(ID);
			setState(82);
			match(DOSPUNTS);
			setState(83);
			match(ALTERNATIVA);
			setState(84);
			match(ID);
			setState(85);
			match(OC);
			setState(86);
			implicacio();
			setState(87);
			match(CC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImplicacioContext extends ParserRuleContext {
		public List<ImplicacionsContext> implicacions() {
			return getRuleContexts(ImplicacionsContext.class);
		}
		public ImplicacionsContext implicacions(int i) {
			return getRuleContext(ImplicacionsContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(EnquestesParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(EnquestesParser.COMA, i);
		}
		public ImplicacioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implicacio; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterImplicacio(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitImplicacio(this);
		}
	}

	public final ImplicacioContext implicacio() throws RecognitionException {
		ImplicacioContext _localctx = new ImplicacioContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_implicacio);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			implicacions();
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(90);
				match(COMA);
				setState(91);
				implicacions();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImplicacionsContext extends ParserRuleContext {
		public TerminalNode OP() { return getToken(EnquestesParser.OP, 0); }
		public TerminalNode NUM() { return getToken(EnquestesParser.NUM, 0); }
		public TerminalNode COMA() { return getToken(EnquestesParser.COMA, 0); }
		public TerminalNode ID() { return getToken(EnquestesParser.ID, 0); }
		public TerminalNode CP() { return getToken(EnquestesParser.CP, 0); }
		public ImplicacionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implicacions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterImplicacions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitImplicacions(this);
		}
	}

	public final ImplicacionsContext implicacions() throws RecognitionException {
		ImplicacionsContext _localctx = new ImplicacionsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_implicacions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(OP);
			setState(98);
			match(NUM);
			setState(99);
			match(COMA);
			setState(100);
			match(ID);
			setState(101);
			match(CP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EnquestaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public TerminalNode DOSPUNTS() { return getToken(EnquestesParser.DOSPUNTS, 0); }
		public TerminalNode ENQUESTA() { return getToken(EnquestesParser.ENQUESTA, 0); }
		public TerminalNode END() { return getToken(EnquestesParser.END, 0); }
		public EnquestaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enquesta; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterEnquesta(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitEnquesta(this);
		}
	}

	public final EnquestaContext enquesta() throws RecognitionException {
		EnquestaContext _localctx = new EnquestaContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_enquesta);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(ID);
			setState(104);
			match(DOSPUNTS);
			setState(105);
			match(ENQUESTA);
			setState(107); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(106);
				match(ID);
				}
				}
				setState(109); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(111);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24t\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3"+
		"\2\6\2\30\n\2\r\2\16\2\31\3\2\3\2\3\2\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\6"+
		"\3&\n\3\r\3\16\3\'\3\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\4\3\4\7\4\64"+
		"\n\4\f\4\16\4\67\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\6\6C\n\6"+
		"\r\6\16\6D\3\6\7\6H\n\6\f\6\16\6K\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t_\n\t\f\t\16\tb\13\t\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\6\13n\n\13\r\13\16\13o\3\13\3\13"+
		"\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2r\2\27\3\2\2\2\4\37\3\2\2\2\6"+
		"/\3\2\2\2\b:\3\2\2\2\nI\3\2\2\2\fL\3\2\2\2\16S\3\2\2\2\20[\3\2\2\2\22"+
		"c\3\2\2\2\24i\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27"+
		"\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34\5\24\13\2\34\35\7\2\2\3\35"+
		"\3\3\2\2\2\36 \5\6\4\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2"+
		"\"#\3\2\2\2#%\5\b\5\2$&\5\f\7\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2"+
		"\2\2(,\3\2\2\2)+\5\16\b\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\5\3"+
		"\2\2\2.,\3\2\2\2/\60\7\23\2\2\60\61\7\21\2\2\61\65\7\3\2\2\62\64\7\23"+
		"\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2"+
		"\2\67\65\3\2\2\289\7\20\2\29\7\3\2\2\2:;\7\23\2\2;<\7\21\2\2<=\7\4\2\2"+
		"=>\5\n\6\2>\t\3\2\2\2?@\7\22\2\2@B\7\21\2\2AC\7\23\2\2BA\3\2\2\2CD\3\2"+
		"\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FH\7\17\2\2G?\3\2\2\2HK\3\2\2\2IG\3"+
		"\2\2\2IJ\3\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\7\23\2\2MN\7\21\2\2NO\7\5\2\2"+
		"OP\7\23\2\2PQ\7\t\2\2QR\7\23\2\2R\r\3\2\2\2ST\7\23\2\2TU\7\21\2\2UV\7"+
		"\7\2\2VW\7\23\2\2WX\7\f\2\2XY\5\20\t\2YZ\7\r\2\2Z\17\3\2\2\2[`\5\22\n"+
		"\2\\]\7\16\2\2]_\5\22\n\2^\\\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\21"+
		"\3\2\2\2b`\3\2\2\2cd\7\n\2\2de\7\22\2\2ef\7\16\2\2fg\7\23\2\2gh\7\13\2"+
		"\2h\23\3\2\2\2ij\7\23\2\2jk\7\21\2\2km\7\6\2\2ln\7\23\2\2ml\3\2\2\2no"+
		"\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2qr\7\b\2\2r\25\3\2\2\2\13\31!\'"+
		",\65DI`o";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}