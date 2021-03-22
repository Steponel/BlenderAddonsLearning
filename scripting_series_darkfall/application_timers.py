# import bpy
#
#
# def in_5_seconds():
#     print("This Works!")
#     bpy.ops.mesh.primitive_cube_add()
#
#
# # 添加一个将在指定的秒数之后被调用的新函数。该函数没有参数，预期返回None或float。如果返回None，计时器将被取消注册。返回的数字指定函数被再次调用之前的延迟时间。functools.partial可用于指定某些参数。
# bpy.app.timers.register(in_5_seconds, first_interval=5)

import bpy

# 全局变量
# https://punchagan.muse-amuse.in/blog/python-globals/
# https://blog.csdn.net/JackLang/article/details/81294208
counter = 0
loc = 0


def run_10_times():
    global loc
    bpy.ops.mesh.primitive_cube_add(location=(0, loc, 0))
    global counter
    counter += 1
    loc += 1
    print(counter)

    # 返回再次调用的延迟时间
    if counter == 10:
        return None
    return 0.5


bpy.app.timers.register(run_10_times)
