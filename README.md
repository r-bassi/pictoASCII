# pictoASCII
Turn your images into ASCII text representations with this python script  

# Dependencies  
Make sure you are on python3 and have [Pillow](https://pypi.org/project/Pillow/) installed  

# Instructions  
- Place your image into the folder that contains pictoASCII.py  
- Open your command terminal and use the cd command to navigate to the folder  
- Enter the following command:  
    `$ python3 -m pictoASCII.py -scale pixelNumber imageFile.jpg outputFile.txt`     
    - pixelNumber is the length of characters you want to scale the image to
    - imageFile is the name of your image file
    - outputFile is the name of the file you want to save the ASCII representation to
- Example input:  
`$ python3 -m pictoASCII -scale 100 r-bassi.png r-bassi.txt`
- If it does not work, try the command using just python instead of python3

#### Done!
Your image file is now saved as text in the output file that you specified. Enjoy!
