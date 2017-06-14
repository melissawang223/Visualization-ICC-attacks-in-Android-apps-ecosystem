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
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.MainActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.EDIT'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.EDIT'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.EDIT'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.EDIT'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.activity.PhotoViewActivity'),
action('android.intent.action.SEND_MULTIPLE'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.b.BR'),
action('com.android.vending.billing.IN_APP_NOTIFY'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.b.BR'),
action('com.android.vending.billing.RESPONSE_CODE'),
),
component(
packagename('com.iudesk.android.photo.editor'),
conponentname('app.b.BR'),
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
