from parsley import makeGrammar, termMaker as t

namedconf = r"""
name = <letterOrDigit+>

statement = (spaces? name:n spaces? '{'
         statement_content:c
         spaces? '}' spaces?
             -> t.Element(n.lower(), c))

directive = spaces? name:d spaces? ';' spaces? -> d

statement_content = (directive | statement)*
"""

NamedConf = makeGrammar(namedconf, globals(), name="TinyHTML")

c = NamedConf(r"""
options {
    mydirective;
    listen {
        listendirective;
    }
}
""")

print 'STATEMENT', c.statement()
