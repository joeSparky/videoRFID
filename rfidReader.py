#!/usr/bin/python3.5
import struct
import time, os
import sys, argparse
import subprocess
import select

class rfidReader():      

 # key definitions
 def toAscii(self, x):
  return {
   2:'1',
   3:'2',
   4:'3',
   5:'4',
   6:'5',
   7:'6',
   8:'7',
   9:'8',
   10:'9',
   11:'0',
  }.get(x,' ')

 # number of keycodes
 NUMCODES = 8
 FORMAT = 'llHHI'
 EVENT_SIZE = struct.calcsize(FORMAT)

 # path (string) to the event file, 
 # digits (string) that we're looking for from the RF ID reader
 def __init__(self, path):
  self.in_file = open(path, "rb")
  # list of keycodes we've received so far
  self.receivedList = ""

 def get(self, digits):
  #print("in rfidReader, will be looking for:"+digits)

  while True:
   # get the ins and outs
   self.ins, self.outs, self.errors = select.select([self.in_file], [], [],0)
   #print("after select, ins size of "+str(len(self.ins)))
   if len(self.ins) == 0:
    return "not yet"
   while True:
    #print("ins size:"+str(len(self.ins)))
    event = self.in_file.read(self.EVENT_SIZE)
    if event:
     #print("event:"+str(event))
     (tv_sec, tv_usec, type, code, value) = struct.unpack(self.FORMAT, event)
     #print("code:"+str(code))
     #print("code after dictionary:" + str(self.toAscii(code)))
     # key pressed
     if type == 1 and value == 1:
      #print "Event type %u, code %u, value %u at %d.%d" % (type, code, value, tv_sec, tv_usec)
      #print("code:"+str(code))
      #print("code after dictionary:" + str(self.toAscii(code)))
      # if this code is the enter key and we don't have NUMCODES digits yet
      if code==28:
       if len(self.receivedList) < self.NUMCODES:
        #print("starting over "+self.receivedList)
        # didn't get NUMCODES character before the enter key. start over.
        self.receivedList = ""
      else:
       # add this code to the received list
       self.receivedList+=self.toAscii(code)
       #print("after append, receivedList:"+self.receivedList)
       if len(self.receivedList) >= self.NUMCODES:
        #print("receivedList size "+str(len(self.receivedList)))
        #print("digits:"+digits)
        #print("digit size:"+str(len(digits)))
        if digits == self.receivedList:
         self.receivedList = ""
         return "right"
        else:
         # start over
         #print("receivedList:"+self.receivedList)
         #print("digits:"+str(digits))
         self.receivedList = ""
         return "wrong"
