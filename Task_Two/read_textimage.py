import cv2
import pytesseract
import re
def preprocess(text):
    

img = cv2.imread(r"C:\Users\inankum29\Desktop\TASK2.png")

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\inankum29\Downloads\tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe'
text = pytesseract.image_to_string(img)
ab= text.split('\n')
#removing empty elements
list_filter = []
for element in ab:
    result = re.search(r"[a-zA-z0-9]+", str(element))
    if(result!=None):
        print(element) 
        list_filter.append(element.replace("|", '').replace('\\',''))
        
dfObj = pd.DataFrame(list_filter)      
dfObj.to_csv("texract.csv")  
        
        