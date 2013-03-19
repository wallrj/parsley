from parsley import makeGrammar, termMaker as t

namedconf = r"""
name = <letterOrDigit+>

statement = (spaces? name:n spaces? '{'
         statement_content:c
         spaces? '}' spaces?
             -> t.Element(n.lower(), c))

directive = spaces? name:k spaces? quotedString?:v spaces?';' spaces? -> (k, v)

statement_content = (directive | statement)*

quotedString = (('"' | '\''):q <(~exactly(q) anything)*>:xs exactly(q))
                     -> xs
"""

NamedConf = makeGrammar(namedconf, globals(), name="TinyHTML")

c = NamedConf(r"""
options {
    mydirective "mydirectiveval";
    listen {
        listendirective 'foobar';
        lonedirective;
    }
}
""")

print 'STATEMENT', c.statement()
