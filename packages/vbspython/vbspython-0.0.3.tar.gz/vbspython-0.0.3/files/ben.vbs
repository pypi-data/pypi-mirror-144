txt=Inputbox("Hello!","Hi!")
a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - Len(wscript.scriptname) - 6)
Set fleobj = CreateObject("Scripting.FileSystemObject").OpenTextFile(a & "var.txt",2)
fleobj.WriteLine(txt)
fleobj.close
Set fleobj = Nothing
