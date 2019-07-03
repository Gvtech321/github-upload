import mmap
import contextlib
import openpyxl

wb = openpyxl.load_workbook("C:\\Users\\uv015815\\Desktop\\Doc workshop step2.xlsx")
sheet=wb.active
maxRow= sheet.max_row
#print (maxRow)
with open("C:\\Users\\uv015815\\Downloads\\clinicalcoding_file2.txt", "r") as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
       
        pcode=input("Enter the Proprietary Read Code for which you want Corresponding SNOMED Code :")
        pcode=pcode.encode('utf8')
        print (pcode)

     
        
        while True:
           
           #if m.find(pcode) !=-1:
        
           i= m.find(pcode)
           #print (i)
           if m.find(pcode) ==-1:
            break
           m.seek(i)
           line = m.readline()
           #print (line)
           last=line.split(b",")
           x=last[-8]
           first=last[0]
           declast=first.decode('utf-8')
           declast= declast.replace('"','')
           depcode=pcode.decode('utf-8')
           
           #print (declast)
           #print (depcode)

           if declast ==depcode:
            y=x.split(b"\r\n")
         
            z=str(y[0],'utf-8')
            a=z.replace('"','')
            print ("Match Found Corresponding SNOMED CODE is " +str(a))
            print('found in file 1')

           else:
            y=x.split(b"\r\n")
         
            z=str(y[0],'utf-8')
            a=z.replace('"','')
            print ("Exact match is not found but partial match is found in File 2:" +str(declast))


            
        

    with open("C:\\Users\\uv015815\\Downloads\\clinicalcoding_file1.txt", "r") as f:
     with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
       # print ('First 10 bytes via read :', m.read(10))
        
        #print ('2nd   10 bytes via read :', m.read(10))
        if m.find(pcode) !=-1:
           i= m.find(pcode)
           m.seek(i)
           line = m.readline()
           last=line.split(b",")
           x=last[-8]
           first=last[0]
           declast=first.decode('utf-8')
           declast= declast.replace('"','')
           depcode=pcode.decode('utf-8')
           
           #print (declast)
           #print (depcode)

           if (declast ==depcode):
            y=x.split(b"\r\n")
         
            z=str(y[0],'utf-8')
            a=z.replace('"','')
            print ("Match Found Corresponding SNOMED CODE is " +str(a))
            print('found in file 2')

           else:
            y=x.split(b"\r\n")
         
            z=str(y[0],'utf-8')
            a=z.replace('"','')
            print ("Exact match is not found but partial match is found in File 2:" +str(declast))
            
        else:
           print('not found in file 2')



