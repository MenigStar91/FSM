import subprocess
import glob 


cppfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
inputfile = glob.glob(r'documents/input' + '**/*.v')[0]
outputfile = "documents/output/"
print(cppfile)
print(inputfile)

subprocess.call(["g++",cppfile, "-o", "fsm"])
subprocess.call(["./fsm.exe",  inputfile, outputfile])
print('done')