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
packagename('com.magicfluids.demo'),
conponentname('com.magicfluids.MainActivity'),
action('android.intent.action.MAIN'),
),
component(
packagename('com.magicfluids.demo'),
conponentname('com.magicfluids.NewWallpaperService'),
action('android.service.wallpaper.WallpaperService'),
),
)
)
print lxml.etree.tostring(the_doc, pretty_print=True)
# Open a file
fo = open('actions.txt', 'wb')
fo.write( lxml.etree.tostring(the_doc, pretty_print=True));
# Close opend file
fo.close()
