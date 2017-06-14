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
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.free.HomeFree'),
action('android.intent.action.MAIN'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetConfigureActivityCompact'),
action('android.appwidget.action.APPWIDGET_CONFIGURE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetConfigureActivityHorizontal'),
action('android.appwidget.action.APPWIDGET_CONFIGURE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetConfigureActivityVertical'),
action('android.appwidget.action.APPWIDGET_CONFIGURE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderCompact'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderCompact'),
action('android.appwidget.action.APPWIDGET_ENABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderCompact'),
action('android.appwidget.action.APPWIDGET_DELETED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderCompact'),
action('android.appwidget.action.APPWIDGET_DISABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderHorz'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderHorz'),
action('android.appwidget.action.APPWIDGET_ENABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderHorz'),
action('android.appwidget.action.APPWIDGET_DELETED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderHorz'),
action('android.appwidget.action.APPWIDGET_DISABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderVert'),
action('android.appwidget.action.APPWIDGET_UPDATE'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderVert'),
action('android.appwidget.action.APPWIDGET_ENABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderVert'),
action('android.appwidget.action.APPWIDGET_DELETED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.WidgetProviderVert'),
action('android.appwidget.action.APPWIDGET_DISABLED'),
),
component(
packagename('ch.smalltech.battery.free'),
conponentname('ch.smalltech.battery.core.widgets.BootCompletedReceiver'),
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
