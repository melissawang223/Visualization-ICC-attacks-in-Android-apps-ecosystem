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
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.Main'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.devhd.feedly'),
conponentname('homewidget.FeedlyWidgetConfigure'),
action('android.appwidget.action.APPWIDGET_CONFIGURE'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.widget.FeedlyWidgetConfigure'),
action('android.appwidget.action.APPWIDGET_CONFIGURE'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.widget.FeedlyWidgetProvider'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.widget.FeedlyWidgetProvider'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.devhd.feedly.widget.FeedlyWidgetProvider_4_1'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.devhd.feedly'),
conponentname('com.google.android.apps.analytics.AnalyticsReceiver'),
action('com.android.vending.INSTALL_REFERRER'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
