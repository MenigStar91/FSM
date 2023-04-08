import subprocess 
subprocess.call(["g++",r"documents\generator\fsm_2modules.cpp", "-o", "fsm"])
subprocess.call(["./fsm.exe",  r"documents\input\uploadfile.v"])