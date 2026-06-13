
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

model1=MLModel("InferIQ",1,0.95)
model2=MLModel("InferIA",2,0.96)
model3=MLModel("InferID",3,0.97)
model4=MLModel("InferIF",4,0.98)
model5=MLModel("InferIG",5,0.99)

#model1.display_info()
#print(model4.get_model_count())
#model1.update_accuracy(0.97)
#model1.display_info()
#print(MLModel.model_count)
#print(model1.model_count)


class ServerNode:
    active_server_count=0
    def __init__(self,ip_address,cpu_percentage,status):
        self.ip_address=ip_address
        self.cpu_percentage=cpu_percentage
        self.status=status
        if status=="active":
            ServerNode.active_server_count+=1
    
    def activate(self):
        if self.status=="idle":
            self.status="active"
            ServerNode.active_server_count+=1
    def deactivate(self):
        if self.status=="active":
            self.status="idle"
            if ServerNode.active_server_count>0:
                ServerNode.active_server_count-=1

    def display_info_1(self):
        print("ip_address:",self.ip_address)
        print("cpu_percentage:",self.cpu_percentage)
        print("status:",self.status)
    @classmethod
    def get_active_count(cls):
        return f"Total Number of active server Present: {ServerNode.active_server_count}"

    
            



server1=ServerNode(1234,0.87,"active")
server2=ServerNode(12378,0.77,"idle")
server3=ServerNode(12365,0.97,"active")
server4=ServerNode(12398,0.98,"idle")
server5=ServerNode(12376,0.93,"active")

#print(ServerNode.active_server_count)
#server3.deactivate()
#print(ServerNode.active_server_count)
#server2.activate()
#print(ServerNode.active_server_count)



class DataPipeline:
    all_pipeline_names=[]
    def __init__(self,pipeline_name,steps,status):
        self.pipeline_name=pipeline_name
        self.steps=steps
        self.status=status
        DataPipeline.all_pipeline_names.append(self.pipeline_name)
    
    def add_step(self,step_name):
        self.steps.append(step_name)

    def remove_step(self,step_name):
        if step_name in self.steps:
            self.steps.remove(step_name)

    def display_info_2(self):
        print("Pipeline name:",self.pipeline_name)
        print("steps:",self.steps)
        print("status:",self.status)

    @classmethod
    def show_all_pipelines(cls):
        print("All Pipelines Created:")
        for name in cls.all_pipeline_names:
            print(name)

pipeline1=DataPipeline("Recovery Pipeline",[],"Running")
pipeline2=DataPipeline("Training Pipeline",[],"Idle")
pipeline3=DataPipeline("Deplyment Pipeline",[],"Completed")

#DataPipeline.show_all_pipelines()

#pipeline1.add_step("Extract Data")
#pipeline1.add_step("Transform Data")
#pipeline1.display_info_2()

#pipeline1.remove_step("Extract Data")
#pipeline1.display_info_2()




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



class BugDemo:
    count=0
    names=[]
    def __init__(self):
        BugDemo.count+=1
        BugDemo.names.append("instance")

bug1=BugDemo()
bug2=BugDemo()
bug3=BugDemo()

#print(BugDemo.count)
#print(BugDemo.names)

class FixedDemo:
    def __init__(self):
        self.names=[]
        self.names.append("instance")

fixed1=FixedDemo()
fixed2=FixedDemo()
fixed3=FixedDemo()

#print(fixed1.names)
#print(fixed2.names)
#print(fixed3.names)


#Explanation:
#BugDemo.names is defined as a class variable
#since lists are mutable, all objects shares same list
#But, In FixedDemo creats self.names inside __init__,
#so each object gets its own seperate list
#use class variables for data meant to be shared by all objects
#use instance variables for data unique to each object


class LimitedResource:
    max_intances=3
    current_intances=0
    def __init__(self,name):
        if LimitedResource.current_intances>=LimitedResource.max_intances:
            raise RuntimeError("Maximum instance limit of 3 reached"
                               "\n Cannot Create more LimitedResouce objects")
        self.name=name
        LimitedResource.current_intances+=1
    def release(self):
        if LimitedResource.current_intances>0:
            LimitedResource.current_intances-=1
    def display_info(self):
        print("Resource Name:",self.name)
        
r1=LimitedResource("Resorce 1")
r2=LimitedResource("Resorce 2")
r3=LimitedResource("Resorce 3")

print(LimitedResource.current_intances)
try:
    r4=LimitedResource("Resorce 4")
except RuntimeError as e:
    print("Error:",e)
r2.release()
print(LimitedResource.current_intances)

try:
    r5=LimitedResource("Resorce 5")
except RuntimeError as e:
    print("Error:",e)
print(LimitedResource.current_intances)