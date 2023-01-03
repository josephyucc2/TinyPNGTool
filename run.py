import tinify
import os
tinify.key = "9P8Qd9xYvP9bgpSsJwNtY51YLYZWkMmS"
rootdir = "D:\共享彩金換皮\出圖_共享财金_跨年"
dstdir = "D:\共享彩金換皮\compressed"
for root, subdirs, files in os.walk(rootdir):
    for file in files:
        print(file)
        if "png" in file or "jpg" in file:
            filePath = os.path.join(root, file)
            print(filePath)
            source = tinify.from_file(filePath)
            dstPath = root.replace(rootdir, dstdir)
            os.makedirs(dstPath, exist_ok=True)
            source.to_file(os.path.join(dstPath, file))
