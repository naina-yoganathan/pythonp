path = "/home/apple/Downloads/story.txt"
folders = path.split("/")

filename = folders[len(folders)-1]
print( "filename = ", filename)

extension = filename.split(".")[-1]
print ( "extension name = ", extension)

dir = "/".join(folders[:-1])
print ( "directory name = ", dir)


# expected o/p
# filename = story.txt
# ext name = txt
# dir name = /home/apple/Downloads