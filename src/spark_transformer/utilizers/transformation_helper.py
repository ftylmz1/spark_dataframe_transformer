import json
import jsonpickle


class TransformationHelper:

    def get_transformations_from_json_file(self, path):
        return jsonpickle.decode(json.dumps(json.loads(open(path, 'r').read())))


    def create_sample_conf_file(self):

        from tranformations.drop import Drop
        from tranformations.hash import Hash

        hash_column = Hash('surname')
        drop_column = Drop('name')

        transformation_list = [hash_column, drop_column]
        transformation_list_pickled = jsonpickle.encode(transformation_list)
