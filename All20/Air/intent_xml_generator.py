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
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.view.SDWebView'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.view.SDWebView'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.el'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.bb'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.el'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.v'),
action('"android.app.action.ADD_DEVICE_ADMIN"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.third.bind.p'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.bb'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.u'),
action('"android.settings.WIFI_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND_MULTIPLE"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.view.SDWebView'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.ProcessManagerActivity'),
action('"android.settings.APPLICATION_DETAILS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.push.MsgDialog2Activity'),
action('"android.intent.action.CALL"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.aw'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.third.bind.p'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.push.MsgDialog2Activity'),
action('"android.intent.action.CALL"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.bb'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.main.UsbApConnectionActivity'),
action('"android.settings.WIRELESS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND_MULTIPLE"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.bb'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.gf'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.el'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.main.UsbApConnectionActivity'),
action('"android.settings.WIRELESS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.gf'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.u'),
action('"android.settings.WIFI_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.v'),
action('"android.app.action.ADD_DEVICE_ADMIN"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.push.MsgDialog2Activity'),
action('"android.intent.action.CALL"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.ProcessManagerActivity'),
action('"android.settings.APPLICATION_DETAILS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.ProcessManagerActivity'),
action('"android.settings.APPLICATION_DETAILS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.aw'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.third.bind.p'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND_MULTIPLE"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.gf'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.u'),
action('"android.settings.WIFI_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.u'),
action('"android.settings.WIFI_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.view.SDWebView'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.v'),
action('"android.app.action.ADD_DEVICE_ADMIN"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.main.UsbApConnectionActivity'),
action('"android.settings.WIRELESS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.el'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.v'),
action('"android.app.action.ADD_DEVICE_ADMIN"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND_MULTIPLE"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.third.bind.p'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.aw'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.push.MsgDialog2Activity'),
action('"android.intent.action.CALL"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.aw'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.AboutActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.gf'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.main.UsbApConnectionActivity'),
action('"android.settings.WIRELESS_SETTINGS"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.FileManagerActivity'),
action('"android.intent.action.SEND"'),
),
intent(
intentname('com.sand.airdroid'),
sender('com.sand.airdroid.ProcessManagerActivity'),
action('"android.settings.APPLICATION_DETAILS_SETTINGS"'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('intent.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
