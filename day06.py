class MLModel:
    model_count=0
    def __init__(self,name,version,accuracy):
        self.name=name
        self.version=version
        self.accuracy=accuracy
        self.performance_history=[self.accuracy]
        MLModel.model_count+=1
    def display_info(self):
        print("Model Name:",self.name)
        print("Version:",self.version)
        print("Accuracy:",self.accuracy)
    @classmethod
    def get_model_count(cls):
        return f"Total Number of Models Present: {MLModel.model_count}"
    def update_accuracy(self,new_accuracy):
        self.accuracy=new_accuracy
        self.performance_history.append(self._accuracy)


    
    def __str__(self):
        return f"MLModel:{self.name} (v{self.version}) - Accuracy: {self.accuracy}"
    
    def __repr__(self):
        return f"MLModel(name='{self.name}', version={self.version}, accuracy={self.accuracy})"
    
    def __eq__(self,other):
        if isinstance(other,MLModel):
            return self.name==other.name and self.version==other.version
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other,MLModel):
            return self.accuracy < other.accuracy
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other,MLModel):
            return self.accuracy > other.accuracy
        return NotImplemented
    
    def __iter__(self):
        self._index=0
        return self
    
    def __next__(self):
        if self._index<len(self.performance_history):
            value=self.performance_history[self._index]
            self._index+=1
            return value
        else:
            raise StopIteration
        
    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self,value):
        if not (0<=value<=1):
            raise ValueError(f"Accuracy must be between 0 and 1.Got: {value}")
        self._accuracy=value


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
    

        
model1=MLModel("InferIQ",1,0.90)
model2=MLModel("InferIA",2,0.96)
model3=MLModel("InferIQ",1,0.97)
model4=MLModel("InferIF",4,0.98)
model5=MLModel("InferIG",5,0.99)

models=[MLModel("modelE",1,0.76),
        MLModel("modelA",1,0.95),
        MLModel("modelC",1,0.82),
        MLModel("modelB",1,0.88),
        MLModel("InferIG",1,0.71)]

sorted_models=sorted(models)
#for m in sorted_models:
    #print(m)



reg=RegressionModel("pricepredictor",1,0.89,(0,1000000))
#print(model1)
#print(repr(model1))
#print(model1==model2)
#print(model1==model3)
#print(model1>model2)
#print(model1<model3)

model1.update_accuracy(0.92)
model1.update_accuracy(0.95)
model1.update_accuracy(0.97)

#print("Performance History:")
#for score in model1:
    #print(score)

#print("Second loop:")
#for score in model1:
    #print(score)

# print(model1.accuracy)
# try:
#     bad_model=MLModel("BadModel",1,5.0)
# except ValueError as e:
#     print("Caught during creation:",e)
# model1.accuracy=0.88
# print(model1.accuracy)
# try:
#     model1.accuracy=2.0
# except ValueError as e:
#     print("Caught during creation:",e)
# print(model1.accuracy)
# model1.update_accuracy(0.97)
# print(model1.accuracy)
# try:
#     model1.update_accuracy(-0.5)
# except ValueError as e:
#     print("Caught during creation:",e)
# print(model1.accuracy)







class ModelVersion:
    highest_score_ever=0
    def __init__(self,version_number,creation_date,performance_score):
        self.version_number=version_number
        self.creation_date=creation_date
        self.performance_score=performance_score
        if performance_score > ModelVersion.highest_score_ever:
            ModelVersion.highest_score_ever=performance_score

    def display_version(self):
        print("version_number:",self.version_number)
        print("creation_dat:",self.creation_date)
        print("performance_score:",self.performance_score)

    @classmethod
    def get_highest_score(cls):
        return f"The Highest Score Ever is = {ModelVersion.highest_score_ever}"
    
    @property
    def is_top_performer(self):
        return self.performance_score >=0.90
    
    @property
    def score_category(self):
        if self.performance_score >=0.90:
            return "Excellent"
        elif self.performance_score >=0.75:
            return "Good"
        elif self.performance_score >=0.55:
            return "Average"
        else:
            return "Poor"
    
model1=ModelVersion(1,"3/1/2025",0.82)
model2=ModelVersion(2,"3/2/2025",0.91)
model3=ModelVersion(3,"3/3/2025",0.87)
model4=ModelVersion(4,"3/4/2025",0.95)
model5=ModelVersion(5,"3/5/2025",0.89)


#model1.display_version()
#print(ModelVersion.get_highest_score())
model6=ModelVersion(6,"3/6/2025",0.93)
#print(ModelVersion.get_highest_score())
model7=ModelVersion(7,"3/7/2025",0.98)
#print(ModelVersion.get_highest_score())    

#print(model1.is_top_performer)
#print(model1.score_category)
#print(model7.is_top_performer)
#print(model7.score_category)

#try:
    #model1.is_top_performer=True
#except AttributeError as e:
    #print("Correctly Blocked:",e)





