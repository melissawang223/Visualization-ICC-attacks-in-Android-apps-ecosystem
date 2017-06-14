import lxml.etree
import lxml.builder
E = lxml.builder.ElementMaker()
ROOT = E.root
DOC = E.doc
intent = E.intent
sender = E.sender
action = E.action
intentname = E.intentname
the_doc = ROOT( 
DOC(intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.k'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.MainActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.k'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.AdsActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.k'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.MainActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.MainActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.k'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.AdsActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.MainActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.AdsActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('tntstudio.supercompass'),
sender('tntstudio.supercompass.AdsActivity'),
action('"android.intent.action.VIEW"'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('intent.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
