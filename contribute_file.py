import os
import shutil

def cp(source,target):
    try:
        shutil.copy(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
def run():
    src_file = ["表1-5-3","表1-5-4"];
    target_dir = "res"
    for root, dirs, files in os.walk(target_dir):
        for dir in dirs:
            path = target_dir+"/"+dir+"/"
            for file in src_file:
                cp(file+".xlsx",path+"("+dir+").xlsx")
    print("完毕")
run()
