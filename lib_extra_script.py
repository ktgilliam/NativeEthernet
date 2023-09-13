Import('env')
from os.path import join, realpath

print("###################################")
print("###################################")
print("###################################")
print("###################################")
print("TEST!!!!!!!!!!!!!!!!!!!!!")
print("###################################")
print("###################################")
print("###################################")
print("###################################")


#
# Private flags (only for the current "SomeLib" source files)
#
# for item in env.get("CCFLAGS", []):
#     print("#################"+item)
#     # if isinstance(item, tuple) and item[0] == "HAL":
#     #     env.Append(CPPPATH=[realpath(join("hal", item[1]))])
#     #     env.Replace(SRC_FILTER=["+<*>", "-<hal*>", "+<hal/%s>" % item[1]])
#     #     break

# for lb in env.GetLibBuilders():
#     lb.env.Append(CCFLAGS=[])
#     # lb.env.Append(CPPDEFINES=[("TEST_LIBDEPS", 1)])
#     if lb.name == "NativeEthernet":
#         lb.env.Append(CPPDEFINES=[("OW_PIN", 13)])