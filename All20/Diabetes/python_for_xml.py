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
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.activities.IntroActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.activities.ShareActivity'),
action('android.intent.action.SEND'),
),
component(
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.receiver.ConfigChangedReceiver'),
action('android.intent.action.LOCALE_CHANGED'),
),
component(
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.receiver.ConfigChangedReceiver'),
action('android.intent.action.TIME_SET'),
),
component(
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.receiver.ConfigChangedReceiver'),
action('android.intent.action.TIMEZONE_CHANGED'),
),
component(
packagename('com.squaremed.diabetesconnect.android'),
conponentname('com.squaremed.diabetesconnect.android.services.NotificationAlarmSetter'),
action('android.intent.action.BOOT_COMPLETED'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
