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
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.SplashActivity_'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.FileManagerActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.MobileInfoActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.ProcessManagerActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.AppManagerActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.main.MainTabsActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.main.MainTabsActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.ServerStateActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.PushService'),
action('android.intent.action.BOOT_COMPLETED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.PushService'),
action('android.intent.action.BOOT_COMPLETED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.AppMngReceiver'),
action('android.intent.action.PACKAGE_ADDED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.AppMngReceiver'),
action('android.intent.action.PACKAGE_REMOVED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.WebServerWidget'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.WebServerWidget'),
action('android.net.wifi.WIFI_STATE_CHANGED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.google.analytics.tracking.android.CampaignTrackingReceiver'),
action('com.android.vending.INSTALL_REFERRER'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.NetworkAndAlarmReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.NetworkAndAlarmReceiver'),
action('android.provider.Telephony.SMS_RECEIVED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.NetworkAndAlarmReceiver'),
action('android.net.conn.CONNECTIVITY_CHANGE'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.NetworkAndAlarmReceiver'),
action('android.provider.Telephony.SMS_RECEIVED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.push.DeviceAdminComponent'),
action('android.app.action.DEVICE_ADMIN_ENABLED'),
),
component(
packagename('com.sand.airdroid'),
conponentname('com.sand.airdroid.LocalConnectionStateReceiver'),
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
