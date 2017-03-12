import sys, os, json, time
import os.path as op
from zipfile import ZipFile as __zipFile
from zipfile import ZIP_DEFLATED


def zipFolder(source_folder, out_file_path):
    zout =  __zipFile(out_file_path, "w", ZIP_DEFLATED)
    source_list = []
    target_list = []
    for root, dirs, files in os.walk(source_folder):
        for f in files:
            source_list.append( op.join(root, f) )
            target_list.append( op.join( op.split(source_folder)[-1], f) )

    for source, target in zip(source_list, target_list):
        zout.write(source, target)
    zout.close()
    
    
def main():
    outFolder = r"D:\Construct 2\my_data\C2RexDoc\repo"
    
    for arg in sys.argv[1:]:
        if not op.isdir(arg):
            continue
      
        (head, pluginName) = op.split(arg)
        (head, category) = op.split(head)
        
        print category + ":" + pluginName
        zipFolder(arg, op.join(outFolder , pluginName+".7z"))
      
        data= {
          "category": category,
          "name": pluginName,
          "timestamp": int(round(time.time() * 1000))
        }
        fp = open(op.join(outFolder , pluginName+".json"), 'w')
        json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': ')  )
        fp.close()
  
    os.system('python "' + op.join(outFolder, "repo.py")+'"') 
      
# -----------------------------------------------------------------------------  
try:
    main()
except Exception, e: 
    print e

raw_input()
