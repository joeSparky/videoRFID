#!/usr/bin/python
import os, sys
class Paths:
    flowers = []
    retries = []
    remedial = []
    # rfid of each flower
    ids = []
    #def __init__(self):
    
    def get(self):
        usbFound = False
        for (dirpath, dirnames, filenames) in os.walk("/media/pi/POLLEN/presentation"):
            usbFound = True;
            for(f) in filenames:
                if f == "intro.mp4":
                    if 'intro' in locals():
                        print("intro.mp4 found in "+intro+ " and "+dirpath)
                        sys.exit()
                    intro = dirpath+"/"+f
                    continue
                if f == "conclusion.mp4":
                    if 'conclusion' in locals():
                        print("conclusion.mp4 found in "+conclusion+" and "+dirpath)
                        sys.exit()
                    conclusion = dirpath+"/"+f
                    continue
                if f.startswith('flower.mp4',0,10):
                    self.flowers.append(dirpath+"/"+f)
                    continue
                if f.startswith('retry.mp4',0,9):
                    self.retries.append(dirpath+"/"+f)
                    continue
                if f.startswith('remedial.mp4',0,12):
                    self.remedial.append(dirpath+"/"+f)
                    continue
                if f.startswith('rfid',0,4):
                    with open(dirpath+"/"+f) as reader:
                        self.ids.append(reader.readline())
                        continue
                print("ignoring "+f)
        
        if not usbFound:
            print ("did not find a USB drive with a volume name of POLLEN with a directory of 'presentation'")
            sys.exit()
        if not 'intro' in locals():
            print("did not find 'intro.mp4' in the presentation directory")
            sys.exit()
        if not 'conclusion' in locals():
            print("did not find 'conclusion.mp4' in the presentation directory")
            sys.exit()
    
        if len(self.flowers) != len(self.retries):    
            print("There are "+str(len(self.flowers))+" flowers but "+str(len(self.retries))+" retries.")
            sys.exit()
            
        if len(self.flowers) != len(self.remedial):    
            print("There are "+str(len(self.flowers))+" flowers but "+str(len(self.remedial))+" remedial.")
            sys.exit()
            
        if len(self.flowers) != len(self.ids):    
            print("There are "+str(len(self.flowers))+" flowers but "+str(len(self.ids))+" rf ids.")
            sys.exit()

        #for (f) in self.flowers:
        #    print("working with "+f)
        return intro, self.flowers, self.retries, self.remedial, self.ids, conclusion

