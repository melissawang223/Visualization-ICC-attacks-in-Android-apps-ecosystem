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
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsAuthAccountActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.util.WLAppRate'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLStartViewActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsAuthAccountActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLStartViewActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLFragmentActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLStartViewActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.util.WLAppRate'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsAuthAccountActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsAuthAccountActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLFragmentActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLStartViewActivity'),
action('"android.media.action.IMAGE_CAPTURE"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLFragmentActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.util.WLAppRate'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.util.WLAppRate'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.WLFragmentActivity'),
action('"android.intent.action.VIEW"'),
),
intent(
intentname('com.wunderkinder.wunderlistandroid'),
sender('com.wunderkinder.wunderlistandroid.activity.settings.WLSettingsSupportActivity'),
action('"android.intent.action.VIEW"'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('intent.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
