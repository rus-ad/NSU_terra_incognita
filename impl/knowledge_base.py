from servives.knowledge_base import IKnowledgeBase
from servives.algorithms.prima import Prima

class KnowledgeBase(IKnowledgeBase):
    def __init__(self, obj_dict):
        self.__obj_dict = obj_dict

    def find_obj(self, obj_name):
        if obj_name in self.__obj_dict:
            return self.__obj_dict[obj_name]
        return None

def make_objects_dict_impl(obj_list):
    obj_dict = dict()
    for obj in obj_list:
        obj_dict[obj.get_name()] = obj
    return obj_dict

def make_algorithm_dict():
    return make_objects_dict_impl([ 
         Prima("Prima", "Implementations of a variant of Prim's algorithm")J
        ])