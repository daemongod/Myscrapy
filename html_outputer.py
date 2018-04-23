# coding:utf8
class HtmlOutputer(object):

    def __init__(self):
        self.datas=[]

    def collect_date(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("</table>")
        count = 0
        for data in self.datas:

            print (type(data))

            fout.write("<tr>")
            fout.write("<td>%d</td>" % count)
            fout.write("<td>%s</td>" % data[0].encode('utf-8'))
            fout.write("<td>%s</td>" % data[1].encode('utf-8'))
            fout.write("<td>%s</td>" % data[2].encode('utf-8'))
            fout.write("</tr>")
            count += 1

        fout.write("</body>")
        fout.write("</html>")

        fout.close()