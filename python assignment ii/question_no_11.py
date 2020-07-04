"""slice extension from filename
"""
# when an extension is fixed characters i.e. 3
def print_name_only(fullFileName):
    filename = fullFileName[:-4]
    print("Filename: ",filename)
    extension = fullFileName[-3:]
    print("Extension: ",extension)

print_name_only("abc.def")
print("=="*30)

# when an arbitrary extension is used
import os 

def arbitrary_extension(filename):
    fileName, fileExtension = os.path.splitext(filename)
    print("Filename: ",fileName)
    print("Extension: ",fileExtension)

arbitrary_extension("abc.def")
print()
arbitrary_extension("abc.defg")
print()
arbitrary_extension("abc.defgh")