import lxml.etree
import lxml.builder
E = lxml.builder.ElementMaker()
ROOT = E.root
DOC = E.doc
component = E.component
packagename = E.packagename
conponentname = E.conponentname
action = E.action
the_doc = ROOT( 
DOC(component(
packagename('livio.pack.lang.en_US'),
conponentname('livio.pack.lang.en_US.DictionaryView'),
action('android.intent.action.MAIN'),
),
component(
packagename('livio.pack.lang.en_US'),
conponentname('livio.pack.lang.en_US.DictionarySearch'),
action('android.intent.action.SEARCH'),
),
component(
packagename('livio.pack.lang.en_US'),
conponentname('livio.pack.lang.en_US.DictionarySearch'),
action('android.intent.action.SEARCH'),
),
component(
packagename('livio.pack.lang.en_US'),
conponentname('livio.pack.lang.en_US.BasicWidget'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('livio.pack.lang.en_US'),
conponentname('livio.pack.lang.en_US.BasicWidgetXL'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
