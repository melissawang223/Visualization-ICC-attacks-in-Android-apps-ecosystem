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
packagename('com.umoni.nocrash'),
conponentname('com.umoni.nocrash.AppActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.umoni.nocrash'),
conponentname('com.umeng.message.RegistrationReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('com.umoni.nocrash'),
conponentname('com.umeng.message.RegistrationReceiver'),
action('android.intent.action.PACKAGE_REMOVED'),
),
component(
packagename('com.umoni.nocrash'),
conponentname('com.umeng.message.RegistrationReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('com.umoni.nocrash'),
conponentname('com.umeng.message.RegistrationReceiver'),
action('android.intent.action.PACKAGE_REMOVED'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
