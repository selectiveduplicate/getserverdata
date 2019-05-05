import os
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
from xml.sax.saxutils import quoteattr as xml_quoteattr


# set up server
class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    # generate list of directories and subdirectories as XML structure
    def genListOfDirs(path):
        # <dir> tag, with name attribute denoting name of the directories and subdirectories
        result = '<dir name=%s>\n' % xml_quoteattr(os.path.basename(path))
        for item in os.listdir(path):
            itempath = os.path.join(path, item)
            if os.path.isdir(itempath):
                result += '\n'.join('  ' + line for line in     # recursion to get subdirectories
                                    genListOfDirs(os.path.join(path, item)).split('\n'))
            elif os.path.isfile(itempath):
                result += '  <file name=%s />\n' % xml_quoteattr(item)
        # close dir tag
        result += '</dir>'
        return result

    # create XML file
    myfile = open("directory_structure.xml", "w")  
    myfile.write('<dirstructure>\n' + genListOfDirs(os.getcwd()) +
                 '\n</dirstructure>')
    myfile.close()

    test(CORSRequestHandler, HTTPServer, port=int(8000))
