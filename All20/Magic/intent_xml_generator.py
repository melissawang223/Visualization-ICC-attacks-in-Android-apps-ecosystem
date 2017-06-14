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
intentname('com.magicfluids.demo'),
sender('com.magicfluids.GLES20Renderer'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.GLES20Renderer'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.LIVE_WALLPAPER_CHOOSER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.GLES20Renderer'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.CHANGE_LIVE_WALLPAPER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.CHANGE_LIVE_WALLPAPER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.LIVE_WALLPAPER_CHOOSER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.CHANGE_LIVE_WALLPAPER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.CHANGE_LIVE_WALLPAPER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.GLES20Renderer'),
action('"android.intent.action.MEDIA_SCANNER_SCAN_FILE"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.LIVE_WALLPAPER_CHOOSER"'),
),
intent(
intentname('com.magicfluids.demo'),
sender('com.magicfluids.MainActivity'),
action('"android.service.wallpaper.LIVE_WALLPAPER_CHOOSER"'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('intent.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
