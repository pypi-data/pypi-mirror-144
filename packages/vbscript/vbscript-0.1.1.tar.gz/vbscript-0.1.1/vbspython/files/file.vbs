all_vars = "["
Set oShell = CreateObject ("WScript.Shell")
Set out = oShell.Exec("cmd.exe /C help")
all = out.StdOut.ReadAll
all_vars = all_vars + """""""" & all & """""""" & ","
all_vars = all_vars + "]"
a = Left(wscript.scriptfullname, Len(wscript.scriptfullname) - Len(wscript.scriptname) - 6)
Set fleobj = CreateObject("Scripting.FileSystemObject").OpenTextFile(a & "var.txt",2)
fleobj.WriteLine(all_vars)
fleobj.close
Set fleobj = Nothing
