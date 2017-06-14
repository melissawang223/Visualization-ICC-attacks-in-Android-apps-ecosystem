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
packagename('com.evernote'),
conponentname('ui.HomeActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NoteListActivity'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NoteListActivity'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NoteListActivity'),
action('android.intent.action.SEARCH'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NoteViewAloneActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NoteViewAloneActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NewNoteActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NewNoteActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NewNoteActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.NewNoteActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.helper.URIBrokerActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.billing.LaunchBillingActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.EvernoteWidgetProvider'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.ui.EvernoteWidgetWSnippetProvider'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.BootReceiver'),
action('android.intent.action.BOOT_COMPLETED'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.billing.BillingReceiver'),
action('com.android.vending.billing.IN_APP_NOTIFY'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.billing.BillingReceiver'),
action('com.android.vending.billing.RESPONSE_CODE'),
),
component(
packagename('com.evernote'),
conponentname('com.evernote.billing.BillingReceiver'),
action('com.android.vending.billing.PURCHASE_STATE_CHANGED'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
