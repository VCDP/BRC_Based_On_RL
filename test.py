import sys

sys.path.append('/home/media/RL/repo/HM/lib/umake/gcc-8.3/x86_64/release/')

print('/home/media/RL/repo/HM/lib/umake/gcc-8.3/x86_64/release/' in sys.path)

import PyUtilities as util

print(util.InputColourSpaceConversion.IPCOLOURSPACE_UNCHANGED)
print(util.InputColourSpaceConversion.IPCOLOURSPACE_YCbCrtoYCrCb)

print(util.ChromaFormat.CHROMA_400.value)
print(util.ChromaFormat.CHROMA_444.value)

print(util.ComponentID.COMPONENT_Y.value)
print(util.ComponentID.COMPONENT_Cb.value)

print(util.ChannelType.CHANNEL_TYPE_LUMA)
print(util.ChannelType.CHANNEL_TYPE_CHROMA)

print("******************test obj_TComPicYuv***************")

obj_TComPicYuv = util.TComPicYuv();
print(obj_TComPicYuv.pbtest(8));

print("******************test obj_TVideoIOYuv***************")
obj_TVideoIOYuv = util.TVideoIOYuv();
print(obj_TVideoIOYuv.pbtest(8));

print("******************test obj_TEncCfg***************")
obj_TEncCfg = util.TEncCfg();
print(obj_TEncCfg.pbtest(8));

cfg = util.TEncCfg()
knee_info = util.TEncCfg.TEncSEIKneeFunctionInformation()
knee_info.m_kneeFunctionId = 0
knee_info.m_kneeFunctionCancelFlag = False
knee_info.m_kneeFunctionPersistenceFlag = True
knee_info.m_inputDRange = 255
knee_info.m_inputDispLuminance = 200
knee_info.m_outputDRange = 255
knee_info.m_outputDispLuminance = 255
knee_point1 = util.TEncCfg.TEncSEIKneeFunctionInformation.KneePointPair(100, 101)
knee_point2 = util.TEncCfg.TEncSEIKneeFunctionInformation.KneePointPair(200, 201)
#print(knee_point1)
knee_info.m_kneeSEIKneePointPairs=[knee_point1,knee_point2]#这里可以赋值，但不可以append，不知道原因是什么:经过测试，这个list原本是不可变的，不能用append，但是可以用+[]和=[]来赋值,这个问题有点奇怪，暂时不理他。
#print(type(knee_info.m_kneeSEIKneePointPairs))
#print(len(knee_info.m_kneeSEIKneePointPairs))

item_type=type(knee_point1)
for item_in_list in knee_info.m_kneeSEIKneePointPairs:
    if type(item_in_list)!=item_type:
        print("项",knee_point1,"与列表中的其他类型不兼容")
        break
    else:
        print("项",knee_point1,"与列表中的其他类型兼容")

#print("append 0 : ",len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs.append(knee_point2)
#print("append 1 失效了: ", len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs.append(util.TEncCfg.TEncSEIKneeFunctionInformation.KneePointPair(200, 201))
#print("append 2 失效了: ", len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs = knee_info.m_kneeSEIKneePointPairs + [knee_point2]
print("append 3 可行: ", len(knee_info.m_kneeSEIKneePointPairs))
#print("islist : ", isinstance(knee_info.m_kneeSEIKneePointPairs,list))
#print("istuple : ", isinstance(knee_info.m_kneeSEIKneePointPairs,tuple))
print(knee_info.m_kneeFunctionId)
print(knee_info.m_kneeFunctionCancelFlag)
print(knee_info.m_kneeFunctionPersistenceFlag)
print(knee_info.m_inputDRange)
print(knee_info.m_inputDispLuminance)
print(knee_info.m_outputDRange)
print(knee_info.m_outputDispLuminance)
print(len(knee_info.m_kneeSEIKneePointPairs))
print(knee_info.m_kneeSEIKneePointPairs[0].inputKneePoint)
print(knee_info.m_kneeSEIKneePointPairs[0].outputKneePoint)


print("******************test obj_TEncTop***************")
obj_TEncTop = util.TEncTop();
print(obj_TEncTop.pbtest(8));

top = util.TEncTop()
knee_info = util.TEncTop.TEncSEIKneeFunctionInformation()
knee_info.m_kneeFunctionId = 0
knee_info.m_kneeFunctionCancelFlag = False
knee_info.m_kneeFunctionPersistenceFlag = True
knee_info.m_inputDRange = 255
knee_info.m_inputDispLuminance = 200
knee_info.m_outputDRange = 255
knee_info.m_outputDispLuminance = 255
knee_point1 = util.TEncTop.TEncSEIKneeFunctionInformation.KneePointPair(100, 101)
knee_point2 = util.TEncTop.TEncSEIKneeFunctionInformation.KneePointPair(200, 201)
#print(knee_point1)
knee_info.m_kneeSEIKneePointPairs=[knee_point1,knee_point2]#这里可以赋值，但不可以append，不知道原因是什么:经过测试，这个list原本是不可变的，不能用append，但是可以用+[]和=[]来赋值,这个问题有点奇怪，暂时不理他。
#print(type(knee_info.m_kneeSEIKneePointPairs))
#print(len(knee_info.m_kneeSEIKneePointPairs))

item_type=type(knee_point1)
for item_in_list in knee_info.m_kneeSEIKneePointPairs:
    if type(item_in_list)!=item_type:
        print("项",knee_point1,"与列表中的其他类型不兼容")
        break
    else:
        print("项",knee_point1,"与列表中的其他类型兼容")

#print("append 0 : ",len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs.append(knee_point2)
#print("append 1 失效了: ", len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs.append(util.TEncCfg.TEncSEIKneeFunctionInformation.KneePointPair(200, 201))
#print("append 2 失效了: ", len(knee_info.m_kneeSEIKneePointPairs))
knee_info.m_kneeSEIKneePointPairs = knee_info.m_kneeSEIKneePointPairs + [knee_point2]
print("append 3 可行: ", len(knee_info.m_kneeSEIKneePointPairs))
#print("islist : ", isinstance(knee_info.m_kneeSEIKneePointPairs,list))
#print("istuple : ", isinstance(knee_info.m_kneeSEIKneePointPairs,tuple))
print(knee_info.m_kneeFunctionId)
print(knee_info.m_kneeFunctionCancelFlag)
print(knee_info.m_kneeFunctionPersistenceFlag)
print(knee_info.m_inputDRange)
print(knee_info.m_inputDispLuminance)
print(knee_info.m_outputDRange)
print(knee_info.m_outputDispLuminance)
print(len(knee_info.m_kneeSEIKneePointPairs))
print(knee_info.m_kneeSEIKneePointPairs[0].inputKneePoint)
print(knee_info.m_kneeSEIKneePointPairs[0].outputKneePoint)


