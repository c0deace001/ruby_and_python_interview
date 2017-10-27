#!/usr/bin/ruby
############################################################################
#///////////////////////////////////////////////////////////////////////////////
#/// @file      ./splitfiles.rb
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

inputFilesDir="./data"
outputFilesDir="./output"
hexid_weseek='c0deace001'

puts "inputFilesDir=#{inputFilesDir}"
puts "outputFilesDir=#{outputFilesDir}"
puts "hexid_weseek=#{hexid_weseek}"

class MultiFileLog
  def initialize(outputdir , format1 = '%s%sout_%03d.txt' )
    @sprintfFormat = format1
    @outdir = outputdir
    @localLinesPerFile=100
    @lineCount=0
    @outputFileNumber=0
  end
  def getOutputFileName
     @outputFileNumber = @lineCount.to_i / @localLinesPerFile.to_i
     fOutName=sprintf(@sprintfFormat,@outdir,File::SEPARATOR,@outputFileNumber.to_i )
     @lineCount = @lineCount.to_i+1
     return fOutName  ;   
  end
end

mylog = MultiFileLog.new( outputFilesDir )

inputFileNumber=0
while 1==1 do
     fname=sprintf("%s%s%02d.txt",inputFilesDir,File::SEPARATOR,inputFileNumber)
     puts "fname=#{fname}"
     
     if File::exist?(fname) then
     
     File.open(fname, "r") do |fh|
         while(line = fh.gets) != nil
             lineChomped=line.chomp
             if lineChomped.length > 0 then
                if lineChomped.match(hexid_weseek) then
                  myOutputFileName=mylog.getOutputFileName()
                  puts "in #{myOutputFileName}:     \"#{lineChomped}\"" ;
                  
                  File.open(myOutputFileName, "a+") do |fh|
                    fh.write( lineChomped + "\n" );
                  end

                end
             end        
         end
     end
     
     else
       puts "No more files to process."
       exit
     end

     inputFileNumber+=1
end

