import CList
import sys
class Color_code:
    def make_html(material, fn):
        u = "./html/"+fn+".html"
        file = open(u, "x", encoding="UTF-8")
        tag = "<tr>"
        for y in range(len(material)):
            tag += "<td style=\"background-color:rgb"+str(material[y])+"\"></td>"
            if y%20 == 19:
                tag += "</tr><tr>"
        tag += "</tr>"
        template = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>%s</title>
                <meta charset="UTF-8">
                <style>
                    table, td, tr {
                    border : none;
                    border-collapse : collapse;
                }
                td{
                    width: 100px;
                    height: 100px;
                }
                </style>
            </head>
            <body>
                <table>
                    %s
                </table>
            </body>
        </html>
        """%(fn, tag)
        file.write(template)
        file.close()

    def make_code():
        sen = input("Do you want to import File? else Write Contents[Y/N]")
        sen = sen.lower()
        if sen == "y":
            fir = input("Enter Path What you wrote : ")
            url = input("Enter CodeFile name what you want : ")
            f = open(fir, 'r', encoding="UTF-8")
            fs = f.read()
            f.close()
        elif sen == "n":
            fs = input("Enter Contents : \n")
            url = input("Enter CodeFile name what you want : ")
        else:
            sys.exit()
        
        fir_ls = list(fs)
        result = []
        for x in range(len(fir_ls)):
            now  = fir_ls[x]
            if now.isnumeric():
                result.append(CList.nums_c[now])
            elif now.isalpha():
                if now.isupper():
                    result.append(CList.upkeys_c[now])
                elif now.islower():
                    result.append(CList.keys_c[now])
            else:
                if now in CList.es_c:
                    result.append(CList.es_c[now])
                else:
                    result.append((255, 255, 255))
        Color_code.make_html(result, url)
    
    def read_code():
        us = input("Enter Path CodeFile : ")
        fil = open(us, 'r', encoding="UTF-8")
        l_s = []
        materials = fil.read()
        st = materials.find("<table>")
        en = materials.find("</table>")
        materials = materials[st:en]
        while materials.find("rgb") != -1:
            ist = materials.find("rgb")
            ie = materials.find(")")
            l_s.append(materials[ist+3:ie+1])
            materials = materials[ie+2:en]
        fil.close()
        for z in range(len(l_s)):
            le = l_s[z].find(',')
            iet = (l_s[z][1:le])
            if iet == '10': #숫자
                m = l_s[z]
                a = int(m[-3:-1])
                l_s[z] = str(a//10)
            elif iet == '50': #소문자
                k = list(CList.keys_c.keys()) 
                v = list(CList.keys_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break               
            elif iet == '80': #대문자
                k = list(CList.upkeys_c.keys()) 
                v = list(CList.upkeys_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break 
            elif iet == '120': #특수기호
                k = list(CList.es_c.keys()) 
                v = list(CList.es_c.values())
                for t in range(len(v)):
                    if str(v[t]) == l_s[z]:
                        l_s[z] = k[t]
                        break 
        
        pdf = "".join(l_s)
        fl = open('recorded.txt', 'x', encoding="UTF-8")
        fl.write(pdf)
        fl.close()
        print(pdf)

    def main():
        print("Hello, I'm RGB color coder")
        print("Now choose one between write mode and read mode", end="")
        intro = input("[W/R]")
        if intro.lower() == "w":
            Color_code.make_code()
        elif intro.lower() == "r":
            Color_code.read_code()
        else:
            sys.exit()
        
Color_code.main()
