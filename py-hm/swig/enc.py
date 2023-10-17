import sys
import os
import hevc


if __name__ == '__main__':
    cTAppEncTop=hevc.TAppEncTop()
    print("\n" )
    print("HM software: Encoder Version [{}] (including RExt)", hevc.NV_VERSION )
    print()
    cTAppEncTop.create()
    try:
        print(sys.argv)
        b=[s.encode() for s in sys.argv]
        #print(b[1:])
        #a=["-c","/home/media/422/Kimono1_1920x1080_30.yuv","-wdt","1920"]
        #b=[s.encode() for s in a]
        if not cTAppEncTop.parseCfg(b):
            print("cTAppEncTop.destroy()")
            cTAppEncTop.destroy()
        else:
            print("test try")
    except Exception: 
        print("输入不合法")
    
    cTAppEncTop.encode()
    cTAppEncTop.destroy()