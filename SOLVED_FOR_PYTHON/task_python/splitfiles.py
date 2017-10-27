#!/usr/bin/python
###########################################################################
#///////////////////////////////////////////////////////////////////////////////
#/// @file      ./splitfiles.py
#/// @version   $Id$
#/// @brief     This source contains...
#///
#///           
#/// @author    Boris Tkachenko
#/// @date      Creation Date: 22/10/2017
#///
#/// Copyright 2015 Unknown Inc., Unknown City, CA
#///
#///////////////////////////////////////////////////////////////////////////////
#
import StringIO 
import os.path
import re

inputFilesDir="./data"
outputFilesDir="./output"
hexid_weseek='c0deace001'

print "inputFilesDir=" , inputFilesDir
print "outputFilesDir=" , outputFilesDir 
print "hexid_weseek=" , hexid_weseek

class MultiFileLog :
    """
       Class that keeps number of the output file flipping forward
    """

    def __init__(self):
        self.sprintfFormat = "%s/out_%03d.txt"
        self.outdir = outputFilesDir
        self.localLinesPerFile=100
        self.lineCount=0
        self.outputFileNumber=0

    def __init__( self , inOutputFileDir , inLocalLinesPerFile , inSprintfFormat ):
        self.sprintfFormat = inSprintfFormat
        self.outdir = inOutputFileDir
        self.localLinesPerFile=inLocalLinesPerFile
        self.lineCount=0
        self.outputFileNumber=0
       
    def getOutputFileName( self ):
        buf = StringIO.StringIO()
        self.outputFileNumber = self.lineCount / self.localLinesPerFile
        buf.write(self.sprintfFormat % ( self.outdir , self.outputFileNumber ))
        self.lineCount = self.lineCount + 1
        return buf.getvalue()

    def dump( self ):
        print "self.sprintfFormat = %s" % ( self.sprintfFormat )
        print "self.outdir = %s" % ( self.outdir )
        print "self.localLinesPerFile = %d" % ( self.localLinesPerFile )
        print "self.lineCount = %d" % ( self.lineCount )
        print "self.outputFileNumber = %s" %  ( self.outputFileNumber )

def formatInputFileName( i ):
        buf = StringIO.StringIO()
        buf.write( "%s/%02d.txt" % ( inputFilesDir , i ))
        return buf.getvalue()

def appendLineToFile( aFileName , aLine  ): 
        f = open( aFileName , "a+" )
        f.write( aLine );
        f.write( '\n' );
        f.close()
 
if __name__ == '__main__' :
   a = MultiFileLog( outputFilesDir , 100  , "%s/out_%03d.txt" ) ;
   a.dump();
   i_FileNumber_start=0
   i_FileNumber_end=1000
   i_FileNumber_step=1
   for i_FileNumber in range(i_FileNumber_start,i_FileNumber_end,i_FileNumber_step):
       fileInName=formatInputFileName( i_FileNumber )
       if os.path.isfile( fileInName ) :
           print "Processing %s" % (  fileInName  )
           for line in open(fileInName,'r').readlines():
               lineChomped = line.rstrip( '\n' )
               if re.match( ".*" + hexid_weseek + ".*" , lineChomped ):
                   outFnAmE1 = a.getOutputFileName()
                   print "%s ==> %s   %s" % (  fileInName , outFnAmE1 , lineChomped ) 
                   appendLineToFile( outFnAmE1 , lineChomped )     
       else:
           break
    
print "Ok.Done."





