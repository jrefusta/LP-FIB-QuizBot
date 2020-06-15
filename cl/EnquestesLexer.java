// Generated from Enquestes.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class EnquestesLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PREGUNTA=1, RESPOSTA=2, ITEM=3, ENQUESTA=4, ALTERNATIVA=5, END=6, FLETXA=7, 
		OP=8, CP=9, OC=10, CC=11, COMA=12, PUNTICOMA=13, INTERROGANT=14, DOSPUNTS=15, 
		NUM=16, ID=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PREGUNTA", "RESPOSTA", "ITEM", "ENQUESTA", "ALTERNATIVA", "END", "FLETXA", 
			"OP", "CP", "OC", "CC", "COMA", "PUNTICOMA", "INTERROGANT", "DOSPUNTS", 
			"NUM", "ID", "WS"
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


	public EnquestesLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Enquestes.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24z\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b"+
		"\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\21\6\21l\n\21\r\21\16\21m\3\22\3\22\7\22r\n\22\f\22\16\22u\13"+
		"\22\3\23\3\23\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13"+
		"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\6\3\2\62;\4\2C\\c|"+
		"\6\2\62;C\\c|\u0082\u0101\5\2\13\f\16\17\"\"\2{\2\3\3\2\2\2\2\5\3\2\2"+
		"\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3"+
		"\2\2\2\5\60\3\2\2\2\79\3\2\2\2\t>\3\2\2\2\13G\3\2\2\2\rS\3\2\2\2\17W\3"+
		"\2\2\2\21Z\3\2\2\2\23\\\3\2\2\2\25^\3\2\2\2\27`\3\2\2\2\31b\3\2\2\2\33"+
		"d\3\2\2\2\35f\3\2\2\2\37h\3\2\2\2!k\3\2\2\2#o\3\2\2\2%v\3\2\2\2\'(\7R"+
		"\2\2()\7T\2\2)*\7G\2\2*+\7I\2\2+,\7W\2\2,-\7P\2\2-.\7V\2\2./\7C\2\2/\4"+
		"\3\2\2\2\60\61\7T\2\2\61\62\7G\2\2\62\63\7U\2\2\63\64\7R\2\2\64\65\7Q"+
		"\2\2\65\66\7U\2\2\66\67\7V\2\2\678\7C\2\28\6\3\2\2\29:\7K\2\2:;\7V\2\2"+
		";<\7G\2\2<=\7O\2\2=\b\3\2\2\2>?\7G\2\2?@\7P\2\2@A\7S\2\2AB\7W\2\2BC\7"+
		"G\2\2CD\7U\2\2DE\7V\2\2EF\7C\2\2F\n\3\2\2\2GH\7C\2\2HI\7N\2\2IJ\7V\2\2"+
		"JK\7G\2\2KL\7T\2\2LM\7P\2\2MN\7C\2\2NO\7V\2\2OP\7K\2\2PQ\7X\2\2QR\7C\2"+
		"\2R\f\3\2\2\2ST\7G\2\2TU\7P\2\2UV\7F\2\2V\16\3\2\2\2WX\7/\2\2XY\7@\2\2"+
		"Y\20\3\2\2\2Z[\7*\2\2[\22\3\2\2\2\\]\7+\2\2]\24\3\2\2\2^_\7]\2\2_\26\3"+
		"\2\2\2`a\7_\2\2a\30\3\2\2\2bc\7.\2\2c\32\3\2\2\2de\7=\2\2e\34\3\2\2\2"+
		"fg\7A\2\2g\36\3\2\2\2hi\7<\2\2i \3\2\2\2jl\t\2\2\2kj\3\2\2\2lm\3\2\2\2"+
		"mk\3\2\2\2mn\3\2\2\2n\"\3\2\2\2os\t\3\2\2pr\t\4\2\2qp\3\2\2\2ru\3\2\2"+
		"\2sq\3\2\2\2st\3\2\2\2t$\3\2\2\2us\3\2\2\2vw\t\5\2\2wx\3\2\2\2xy\b\23"+
		"\2\2y&\3\2\2\2\5\2ms\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}