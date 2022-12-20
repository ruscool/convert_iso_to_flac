# import os
#
# import isoparser
#
# os.chdir(r'/home/rusdev/Music/BARBRA/')
# path = os.getcwd()
# print(path)
# isoFile = f'{path}/Barbara.iso'
# print(isoFile)
# parseIso = isoparser.parse(isoFile)
# for file in parseIso.root.children:
import isoparser

iso = isoparser.parse("~/Music/BARBRA/Barbara.iso")

print(iso.record("boot", "grub").children)
print(iso.record("boot", "grub", "grub.cfg").content)