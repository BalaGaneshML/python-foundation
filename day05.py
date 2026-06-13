class MLModel:
    model_count=0
    def __init__(self,name,version,accuracy):
        self.name=name
        self.version=version
        self.accuracy=accuracy
        MLModel.model_count+=1
    def display_info(self):
        print("Model Name:",self.name)
        print("Version:",self.version)
        print("Accuracy:",self.accuracy)
    @classmethod
    def get_model_count(cls):
        return f"Total Number of Models Present: {MLModel.model_count}"
    def update_accuracy(self,new_accuracy):
        if 0<=new_accuracy<=1:
            self.accuracy=new_accuracy
        else:
            print("The acuuracy must between 0 and 1")

    @classmethod
    def from_dict(cls,data_dict):
        required_keys=["name","version","accuracy"]
        for key in required_keys:
            if key not in data_dict:
                raise ValueError(f"Missing required key: {key}")
        name=data_dict["name"]
        version=data_dict["version"]
        accuracy=data_dict["accuracy"]
        return cls(name,version,accuracy)
    
    @classmethod
    def from_csv_string(cls,csv_string):
        values=csv_string.split(",")
        if len(values)!=3:
            raise ValueError("CSV String must contain exactly 3 values: name,version,accuracy")
        name=values[0]
        version=int(values[1])
        accuracy=float(values[2])
        return cls(name,version,accuracy)
    
    @staticmethod
    def validate_accuracy(value):
        if 0<=value<=1:
            return True
        return False
    
    @staticmethod
    def validate_version(version):
        if version>0:
            return True
        return False

class ClassificationModel(MLModel):
    def __init__(self, name, version, accuracy,num_classes):
        super().__init__(name, version, accuracy)
        self.num_classes=num_classes

    def display_info(self):
        super().display_info()
        print("Number of Classes:",self.num_classes)

class RegressionModel(MLModel):
    def __init__(self, name, version, accuracy,prediction_range):
        super().__init__(name, version, accuracy)
        self.prediction_range=prediction_range

    def display_info(self):
        super().display_info()
        print("prediction_range:",self.prediction_range)

    def is_in_range(self,prediction):
        if self.prediction_range[0]<=prediction<=self.prediction_range[1]:
            return True
        return False
        
model1=MLModel("InferIQ",1,0.95)
model2=MLModel("InferIA",2,0.96)
model3=MLModel("InferID",3,0.97)
model4=MLModel("InferIF",4,0.98)
model5=MLModel("InferIG",5,0.99)

reg=RegressionModel("pricepredictor",1,0.89,(0,1000000))
#RegressionModel.display_info(reg)
#print(reg.is_in_range(500000))
#print(reg.is_in_range(2000000))




class ComputeResource:
    total_resources = 0

    def __init__(self, resource_id, location):
        self.resource_id = resource_id
        self.location = location

        ComputeResource.total_resources += 1

    def display_info(self):
        print("Resource ID :", self.resource_id)
        print("Location :", self.location)

    def get_resource_type(self):
        return "ComputeResource"
    
    @classmethod
    def from_dict(cls, data):
        required_keys = ["resource_id", "location"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
        resource_id = data["resource_id"]
        location = data["location"]
        return cls(resource_id, location)


class Server(ComputeResource):

    def __init__(self, resource_id, location,
                 ip_address, operating_system):

        super().__init__(resource_id, location)

        self.ip_address = ip_address
        self.operating_system = operating_system

    def display_info(self):
        super().display_info()

        print("IP Address :", self.ip_address)
        print("Operating System :", self.operating_system)

    def get_resource_type1(self):
        return "Server"
    
    @classmethod
    def from_dict(cls, data):
        required_keys = ["resource_id", "location", "ip_address", "operating_system"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
        resource_id = data["resource_id"]
        location = data["location"]
        ip_address = data["ip_address"]
        operating_system = data["operating_system"]
        return cls(resource_id, location, ip_address, operating_system)


class GPUServer(Server):

    def __init__(self, resource_id, location,
                 ip_address, operating_system,
                 gpu_model, vram_gb):

        super().__init__(
            resource_id,
            location,
            ip_address,
            operating_system
        )

        self.gpu_model = gpu_model
        self.vram_gb = vram_gb

    def display_info(self):
        super().display_info()

        print("GPU Model :", self.gpu_model)
        print("VRAM (GB) :", self.vram_gb)

    @classmethod
    def from_dict(cls, data):
        required_keys = ["resource_id", "location", "ip_address", "operating_system", "gpu_model", "vram_gb"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
        resource_id = data["resource_id"]
        location = data["location"]
        ip_address = data["ip_address"]
        operating_system = data["operating_system"]
        gpu_model = data["gpu_model"]
        vram_gb = data["vram_gb"]
        return cls(resource_id, location, ip_address, operating_system, gpu_model, vram_gb)

    def get_resource_type2(self):
        return "GPU Server"



resource = ComputeResource("CR001", "Chennai")

server = Server(
    "SR001",
    "Bangalore",
    "192.168.1.10",
    "Linux"
)

gpu_server = GPUServer(
    "GPU001",
    "Hyderabad",
    "192.168.1.20",
    "Ubuntu",
    "NVIDIA A100",
    80
)


print("=== GPUServer Information ===")
gpu_server.display_info()


print("\n=== Resource Types ===")
print(resource.get_resource_type())
print(server.get_resource_type1())
print(gpu_server.get_resource_type2())


print("\n=== isinstance Check ===")
print(isinstance(gpu_server, ComputeResource))


print("\n=== Total Resources ===")
print(ComputeResource.total_resources)



#Version 1: Using super() everywhere

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")


class Labrador(Dog):
    def speak(self):
        super().speak()
        print("Labrador says woof")


# Testing
lab = Labrador()
lab.speak()

#Version 2: Labrador does NOT call super()
class Animal1:
    def speak(self):
        print("Animal speaks")


class Dog1(Animal1):
    def speak(self):
        super().speak()
        print("Dog barks")


class Labrador1(Dog1):
    def speak(self):
        print("Labrador says woof")


# Testing
lab = Labrador1()
lab.speak()



from datetime import datetime
class LoggableMixin:
    def log_created(self):
        timestamp = datetime.now()

        print(
            f"Object created: "
            f"{self.__class__.__name__} "
            f"at {timestamp}"
        )

    def log_action(self, action):
        print(
            f"Action performed: "
            f"{action} "
            f"on {self.__class__.__name__}"
        )

    def log_destroyed(self):
        print(
            f"Object destroyed: "
            f"{self.__class__.__name__}"
        )


class LoggableMLModel(MLModel, LoggableMixin):

    def __init__(self, name, version, accuracy):
        super().__init__(name, version, accuracy)

        # Log immediately after creation
        self.log_created()

    def update_and_log(self, new_accuracy):
        self.update_accuracy(new_accuracy)

        self.log_action(
            f"accuracy updated to {new_accuracy}"
        )


# ===================================
# Testing
# ===================================

lm = LoggableMLModel(
    "FraudDetector",
    1,
    0.95
)

print("\nUpdating Accuracy...")
lm.update_and_log(0.97)

print("\nDestroying Object...")
lm.log_destroyed()

print("\nInstance Checks")
print(isinstance(lm, MLModel))
print(isinstance(lm, LoggableMixin))




from abc import ABC, abstractmethod



class BasePredictor(ABC):

    @abstractmethod
    def predict(self, data):
        pass

    def validate_input(self, data):
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")


class SimpleClassifier(BasePredictor):

    def predict(self, data):
        self.validate_input(data)

        return "Predicted class: 0"


class SimpleRegressor(BasePredictor):

    def predict(self, data):
        self.validate_input(data)

        return float(sum(data) / len(data))


class BrokenModel(BasePredictor):
    pass


# ===================================
# Testing
# ===================================

print("=== SimpleClassifier ===")
classifier = SimpleClassifier()

print(classifier.predict([1, 2, 3]))


print("\n=== SimpleRegressor ===")
regressor = SimpleRegressor()

print(regressor.predict([1, 2, 3]))


print("\n=== BasePredictor Error Test ===")
try:
    predictor = BasePredictor()
except TypeError as e:
    print("Error:", e)


print("\n=== BrokenModel Error Test ===")
try:
    broken = BrokenModel()
except TypeError as e:
    print("Error:", e)