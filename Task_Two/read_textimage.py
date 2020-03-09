import cv2
import pytesseract
import re
import pandas as pd

img = cv2.imread(r"C:\Users\inankum29\Desktop\TASK2.png")

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\inankum29\Downloads\tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe'
text = pytesseract.image_to_string(img)
ab= text.split('\n')
#removing empty elements
list_filter = []
for element in ab:
    result = re.search(r"[a-zA-z0-9]+", str(element))
    if(result!=None):
        #print(element) 
        list_filter.append(element.replace("|", '').replace('\\',''))
        
#Tokenizing more than 6th eleemnt in list
list_filter = [str(list_filter[i]).split(' ') if(i>6) else [(list_filter[i])] for i in range(len(list_filter)) ]
for i in range(len(list_filter)):
    if('' in list_filter[i] and (i>6 and i!=8)):
        list_filter[i].remove('')
    
list_filter[7][4] =    list_filter[7][4]   +  " " +list_filter[8][0]
list_filter.remove(list_filter[8])
print((list_filter))
my_df = pd.DataFrame(list_filter)
my_df.to_csv(r"C:\Users\inankum29\Desktop\my_csv.csv", index=False, header=False)
