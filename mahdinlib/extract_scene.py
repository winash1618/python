import inspect
import itertools as it
import os
import platform
import subprocess as sp
import sys
import traceback

from mahdinlib.scene.scene import Scene
import mahdinlib.constants

def is_child_scene(obj, module):
    # the function check conditions that must be
    # satisfied by the object in the given module
    # codition 1 : return false if obj is not a class
    # condition 2 : return false if obj is not a 
    # subclass of Scene class
    # condition 3 : return false if obj class is same 
    # as Scene class
    # condition 4 : return false if obj class is not 
    # 
    # if it survives above 4 if condtions we get return 
    # as True Which is what we want.
    if not inspect.isclass(obj):
        return False
    if not issubclass(obj, Scene):
        print(obj, Scene)
        return False
    if obj == Scene:
        return False
    if not obj.__module__.startswith(module.__name__):
        return False
    print(obj)
    return True

def get_scene_classes_from_module(module):
    if hasattr(module, "SCENES_IN_ORDER"):
        # it check if module or (test.py) has 
        # attribute "SCENES_IN_ORDER"
        return module.SCENES_IN_ORDER
    else:
        # Else return classes in the module or (test.py) 
        # that if it gives is_child_scene() as true
        # print(inspect.getmembers(module,False))
        return [
            member[1]
            for member in inspect.getmembers(
                module,
                lambda x: is_child_scene(x, module)
            )
        ]


def main(config):
    # here module is config["module"] which contain
    # <module 'test' from 'test.py'>
    module = config["module"]
    # all_scene_classes contain list of classes in 
    # test.py [<class 'test.testproblem'>, <class 'test.testproblem1'>,...]
    all_scene_classes = get_scene_classes_from_module(module)

if __name__ == "__main__":
    main()