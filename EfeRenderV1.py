import subprocess

print("EfeRenderV1\n")
print("[0] Clear All Directories")
print("[1] Convert Video to Frames")
print("[2] Convert Audio to File")
print("[3] Convert Frames to Video")
print("[4] Convert Frames and Audio to Video\n")

ModeSelection = input("Selection> ")

if ModeSelection != '0' and ModeSelection != '2':
    print("EfeRenderV1\n")
    print("Which Render Quality you Want?\n")
    print("[0] Low")
    print("[1] High\n")
    RenderQuality = input("Selection> ")

if ModeSelection != '0' and ModeSelection != '2':
    if ModeSelection == '1' and RenderQuality == '0': subprocess.call([r'.\scripts\cvtfl.bat']) 
    if ModeSelection == '3' and RenderQuality == '0': subprocess.call([r'.\scripts\cftvl.bat'])
    if ModeSelection == '4' and RenderQuality == '0': subprocess.call([r'.\scripts\cfaatvwal.bat'])
    if ModeSelection == '1' and RenderQuality == '1': subprocess.call([r'.\scripts\cvtfh.bat'])
    if ModeSelection == '3' and RenderQuality == '1': subprocess.call([r'.\scripts\cftvh.bat'])
    if ModeSelection == '4' and RenderQuality == '1': subprocess.call([r'.\scripts\cfaatvwah.bat'])

if ModeSelection == '0': subprocess.call([r'.\scripts\caf.bat'])
if ModeSelection == '2': subprocess.call([r'.\scripts\cvta.bat'])