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



def prompt_user_for_choice(scene_classes):

    num_to_class = {}
    for count, scene_class in zip(it.count(1), scene_classes):
        name = scene_class.__name__
        print("%d: %s" % (count, name))
        num_to_class[count] = scene_class
    try:
        user_input = input(mahdinlib.constants.CHOOSE_NUMBER_MESSAGE)
        return [
            num_to_class[int(num_str)]
            for num_str in user_input.split(",")
        ]
    except KeyError:
        print(mahdinlib.constants.INVALID_NUMBER_MESSAGE)
        sys.exit(2)
        user_input = input(mahdinlib.constants.CHOOSE_NUMBER_MESSAGE)
        return [
            num_to_class[int(num_str)]
            for num_str in user_input.split(",")
        ]
    except EOFError:
        sys.exit(1)

def get_scenes_to_render(scene_classes, config):
    # the function returns the scene_classes to render
    # if result == []
        # if len(scene_classes) == 1 it returns the that scene_class
        # if len(scene_classes) > 1 it invokes prompt_user_for_choice(scene_classes)
        # funciton and make us to choose which scence_class to render
    # else return results
    if len(scene_classes) == 0:
        print(manimlib.constants.NO_SCENE_MESSAGE)
        return []
    if config["write_all"]:
        return scene_classes
    result = []
    for scene_name in config["scene_names"]:
        found = False
        for scene_class in scene_classes:
            if scene_class.__name__ == scene_name:
                result.append(scene_class)
                found = True
                break
        if not found and (scene_name != ""):
            print(
                manimlib.constants.SCENE_NOT_FOUND_MESSAGE.format(
                    scene_name
                ),
                file=sys.stderr
            )
    if result:
        return result
    return [scene_classes[0]] if len(scene_classes) == 1 else prompt_user_for_choice(scene_classes)

     
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
    # below line contains the scene_classes_to_render 
    # 1: testproblem
    # 2: testproblem1
    # Choose number corresponding to desired scene/arguments.
    # (Use comma separated list for multiple entries)
    # Choice(s): 1
    #scene_classes_to_render = [<class 'test.testproblem'>]
    scene_classes_to_render = get_scenes_to_render(all_scene_classes, config)
    print(scene_classes_to_render)

    

if __name__ == "__main__":
    main()