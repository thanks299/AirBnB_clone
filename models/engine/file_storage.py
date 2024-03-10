#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class provides methods for serializing instances to a JSON file
    and deserializing a JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: Dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        ser_dict = FileStorage.__objects
        obj_dict = {obj: ser_dict[obj].to_dict() for obj in ser_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects.
        If the JSON file (__file_path) exists, loads the data and creates
        instances of the corresponding classes. Otherwise, does nothing.
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj_id, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    if class_name not in globals():
                        # If the class is not in globals, you may want to handle this case
                        continue
                    model_class = globals()[class_name]
                    self.new(model_class(**obj_data))
        except FileNotFoundError:
            pass
