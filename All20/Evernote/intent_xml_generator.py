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
intentname('com.evernote'),
sender('com.evernote.ui.NoteListFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteViewFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.client.EvernoteService'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.f'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.client.EvernoteService'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.f'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.jc'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.RESPONSE_CODE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.f'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.PURCHASE_STATE_CHANGED"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingService'),
action('"com.android.vending.billing.MarketBillingService.BIND"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.PURCHASE_STATE_CHANGED"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.RESPONSE_CODE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.f'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingService'),
action('"com.android.vending.billing.MarketBillingService.BIND"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteViewFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.PURCHASE_STATE_CHANGED"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingService'),
action('"com.android.vending.billing.MarketBillingService.BIND"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.client.EvernoteService'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteViewFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.jc'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingService'),
action('"com.android.vending.billing.MarketBillingService.BIND"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.jc'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteListFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteListFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.PURCHASE_STATE_CHANGED"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.RESPONSE_CODE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.jc'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteViewFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.billing.BillingReceiver'),
action('"com.android.vending.billing.RESPONSE_CODE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.client.EvernoteService'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.evernote'),
sender('com.evernote.ui.NoteListFragment'),
action('"com.android.launcher.action.INSTALL_SHORTCUT"'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('intent.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
