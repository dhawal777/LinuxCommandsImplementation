import os
import linecache
import sys
import stat
import subprocess as sp
import difflib
# from termcolor import colored, cprint 
# curr_path=os.path.dirname(os.path.realpath(__file__));
sp.call('clear',shell=True)
while 1:
    def cd(path):
       if os.path.isdir(path):
           if os.access(path, os.W_OK):
                 os.chdir(path)
           else:
               print "Permission Denied"
       else:
           print "Enter Valid Directory"
           
           
        #  global curr_path=
    # def ls():
    #     list1=os.listdir(".")
    #     for i in list1:
    #        print i;
    def ls(path): 
        if len(path)>1:
             if os.path.isdir(path):
                if os.access(path, os.R_OK):
                        list1=os.listdir(path[1])
                        for i in list1:
                            print i;
                else:
                    print "Permission Denied"
             else:
                 print "Enter valid Directory"
                 
        else:
            if os.access(".", os.R_OK):
                list1=os.listdir(".")
                for i in list1:
                    print i
        

    def pwd():

        dir_path = os.path.dirname(os.path.realpath(__file__));
        print curr_path

    
           
        


    # def sed():



    # def awk():



    def touch(path, times=None):
        for i in range(1,len(path)):
            fname=path[i]
            result = fname.rfind('/')
            if(result!=-1):
                dir1 = os.path.dirname(fname)
                if os.path.isdir(dir1):
                    if os.access(dir1, os.W_OK):
                        with open(fname, 'a'):
                            os.utime(fname, times)
                    else:
                        print "permission denied"  
                else:
                    print "Please enter a valid Directory"  
            else:
                with open(fname, 'a'):
                        os.utime(fname, times)
            #file access and modified time
            #
    

    def isreadable(filepath):
        st = os.stat(filepath)
        return bool(st.st_mode & stat.S_IRGRP)

    def tail(path):
        for i in range(1,len(path)):
            fname=path[i]
            if(os.path.isfile(fname)):
                if(isreadable(fname)):
                    tot_lines = len(open(fname).readlines())
                    if tot_lines<=10:
                        for i in range(1, tot_lines+1):
                                print linecache.getline(fname,i),
                    else:
                        for i in range(tot_lines -10+1,tot_lines+1):
                                print linecache.getline(fname,i),
                    # use line cache module to read the lines
                    
                else:
                    print "File not Readable"
            else:
                print "Not a valid file path"
            print


    def head(path):
        #print fname
        for i in range(1,len(path)):
            fname=path[i]
            if(os.path.isfile(fname)):

                if(isreadable(fname)):
                    
                    tot_lines = len(open(fname).readlines())
                    #print tot_lines
                    if tot_lines<=10:
                        for i in range(1, tot_lines+1):
                                print linecache.getline(fname,i),
                    else:
                        for i in range(1,11):
                                print linecache.getline(fname,i),
                else:
                    print "File not Readable"
            else:
                print "Not a valid file path"
            print
    # def tr():



    def diff(fname1,fname2):
        # for line in difflib.unified_diff(lines1, lines2, fromfile=fname1, tofile=fname2, lineterm='', n=0):
        #         print line
        if(os.path.isfile(fname1) and os.path.isfile(fname2)):
                if(isreadable(fname1) and isreadable(fname2)):
                    with open(fname1,'r') as f:
                        line1=f.readlines()
                    with open(fname2,'r') as f:
                        line2=f.readlines()
                    # line3=list(set(line1)-set(line2))
                    # line4=list(set(line2)-set(line1))
                    for i in line1:
                        if i not in line2:
                            print i
                    print"---------------"   
                    for i in line2:
                        if i not in line1:
                            print i
                else:
                    if(isreadable(fname1)):
                           print "File2 not readable"
                    else:
                           print "File1 not readable"
        else:
             if(os.path.isfile(fname1)):
                    print "File2 path not valid"
             else:
                    print "File1 path not valid"
        
        # with open(fname1, 'r') as hosts0:
        #     with open(fname2, 'r') as hosts1:
        #         diff = difflib.unified_diff(
        #             hosts0.readlines(),
        #             hosts1.readlines(),
        #             fromfile='hosts0',
        #             tofile='hosts1',
        #         )
        #         for line in diff:
        #             sys.stdout.write(line)
    def tr(s1,s2):
        dict1={}
        count1=0
        for i,j in zip(s1,s2):
            dict1[i]=j
            count1=count1+1
            # print i,j
        if(len(s1)>len(s2)):
            for i in range(count1,len(s1)):
                dict1[s1[i]]=s2[len(s2)-1]
                # print s1[i],dict1[s1[i]]
        print "press @ to quit tr"
        while(1):
            a=raw_input()
            if(a=="@"):
                break
            else:
                for i in a:
                    if(i in dict1):
                        sys.stdout.write(dict1[i])
                    else:
                        sys.stdout.write(i)
            print 
    def prRed(skk): sys.stdout.write("\033[91m{}\033[00m" .format(skk)) 
    def grep(s1,s2):
            x=0
            CRED = '\033[91m'
            x=s2.find(s1)
            if(x!=-1):
                while(x!=-1):
                    
                    s4=s2[x:x+len(s1)]
                    sys.stdout.write(s2[:x])
                    s2=s2[x+len(s1):]
                    
                    prRed(s4)
                    # print(CRED +s5
                    x=s2.find(s1)
                    # grep(s1,s2)
                sys.stdout.write(s2) 
    def sed(s1,rep,s2):
            x=0
            # CRED = '\033[91m'
            x=s2.find(s1)
            if(x!=-1):
                while(x!=-1):
                    
                    s4=s2[x:x+len(s1)]
                    sys.stdout.write(s2[:x])
                    sys.stdout.write(rep)
                    s2=s2[x+len(s1):]
                    
                    # prRed(s4)
                    # print(CRED +s5
                    x=s2.find(s1)
                    # grep(s1,s2)
                sys.stdout.write(s2) 
               
                
                   
        
        
    print "                      Python Shell                            " 
    print "Enter The Command"   
    comm=raw_input()
    if comm=="":
        print "Invalid Command"
    else:
        command=comm.split()
        if(command[0]=="head"):

            head(command);

        if(command[0]=="tail"):

            tail(command);

        if(command[0]=="diff"):

            diff(command[1],command[2]);

        if(command[0]=="cd"):

            cd(command[1]);

        if(command[0]=="tr"):

            tr(command[1],command[2]);

        if(command[0]=="pwd"):

            pwd();

        if(command[0]=="grep"):
            # print "dha"
            # flag=0
            # s1=""
            # s2=""
            # for i in range(1,len(command)):
            #        if(command[i]=="@"):
            #          #print "i  am here" 
            #          flag=1
            #        elif(flag==0):
            #          s1=s1+command[i]+" "
            #        else:
            #          s2=s2+command[i]+" "

            
            # print s1
            # print s2   
            try:
                # print comm
                input1=comm.split("<<<")
                input2=input1[0].strip()
                input3=input1[1].strip()
                input4=input2.split('"')
                input5=input3.split('"')
                # print input4[1]
                # print input5[1]
                grep(input4[1],input5[1])
            except:
                print "Invalid Syntax for grep@sorry!!"
             
                  
            

        if(command[0]=="sed"):
                input1=comm.split("<<<")
                input2=input1[0].strip()
                input3=input1[1].strip()
                input4=input2.split('"')
                input6=input4[1].split('/');
                # print input6[0],input6[1]
                input5=input3.split('"')
                # print input5[1]
                sed(input6[0],input6[1],input5[1]);

        if(command[0]=="touch"):

            touch(command,None)

        if(command[0]=="ls"):
            ls(command);
        if(command[0]=="exit"):
            break;


