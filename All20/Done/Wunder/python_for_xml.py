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
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('activity.WLSlideShowActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('activity.WLMainFragmentActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('activity.WLMainFragmentActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('activity.WLMainFragmentActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('activity.WLMainFragmentActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('widget.oldversion.WLWidgetProviderOld'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('widget.newversion.WLWidgetProviderNew'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.wunderkinder.wunderlistandroid'),
conponentname('receiver.WLConnectivityReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
