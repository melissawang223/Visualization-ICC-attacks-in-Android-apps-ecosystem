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
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.main.MainActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.memboost.onetapboost.OneTapBoostActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.fileclean.residual.ResidualFileCleanActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.boostbox.BoostBoxActivity'),
action('android.intent.action.VIEW'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.base.androidsettings.auto.AutoExecutorAccessibilityService'),
action('android.accessibilityservice.AccessibilityService'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.BootReceiver'),
action('android.intent.action.BOOT_COMPLETED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.BootReceiver'),
action('android.intent.action.ACTION_SHUTDOWN'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.BootReceiver'),
action('android.intent.action.DATE_CHANGED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.ConnectivityChangeReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.ConnectivityChangeReceiver'),
action('android.net.wifi.WIFI_STATE_CHANGED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.ConnectivityChangeReceiver'),
action('android.intent.action.ANY_DATA_STATE'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.AppChangeReceiver'),
action('android.intent.action.PACKAGE_REMOVED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.AppChangeReceiver'),
action('android.intent.action.PACKAGE_ADDED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.UserPresentReceiver'),
action('android.intent.action.USER_PRESENT'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.UserPresentReceiver'),
action('android.intent.action.DOWNLOAD_COMPLETE'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.utils.component.UserPresentReceiver'),
action('android.intent.action.DOWNLOAD_NOTIFICATION_CLICKED'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.publish.gp.GooglePlayReceiver'),
action('com.android.vending.INSTALL_REFERRER'),
),
component(
packagename('mobi.uclean.boost'),
conponentname('com.ucweb.master.widget.UCleanWidget'),
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
