while True:
    print('''Enter the following numbers to particular programs:
      1:args mean median mode range variance std. deviation
      2:kwargs ML config builder
      3:map functions
      4:List comprehension filter
      5:filter functions
      6:list and dict comprehensions
      7:function Pipeline
      ''')
    choice= int(input("Enter the Value: "))  
    if choice==1:
        def calculate_stats(*numbers):
            number_sorted=sorted(numbers)
            length=len(number_sorted)
            mean=(sum(number_sorted))/length
            if length%2==1:
                median=number_sorted[length//2]
            else:
                median=(number_sorted[length//2-1]+number_sorted[length//2])/2
            #mode can be calculated by this method too
            #mode=max(numbers, key=numbers.count)
            freq={}
            for i in numbers:
                freq[i]=numbers.count(i)
            max_frq=0
            mode=0
            for key in freq:
                if freq[key]>max_frq:
                    max_frq=freq[key]
                    mode=key
            Maximum_value=max(number_sorted)
            minimum_value=min(number_sorted)
            range_1=Maximum_value-minimum_value
            squared_diff=list(map(lambda x:(x-mean)**2,numbers))
            total=sum(squared_diff)
            variance= total/len(numbers)
            std_deviation=variance**0.5
            print(mean)
            print(median)
            print(mode)
            print(range_1)
            print(variance)
            print(std_deviation)
        calculate_stats(5,3,8,3,9,3,7,1)
        
    elif choice==2:    
        def build_model_config(**settings):
            if "model_name" not in settings:
                raise ValueError("model_name is required")
            if "version" not in settings:
                raise ValueError("version is required")
            settings["timestamp"]="2025-06-09"
            return settings
        
        config1=build_model_config(
            model_name="InferIQ",
            version=1,
            accuracy=0.95
        )
        

        config2=build_model_config(
            model_name="InferIQ",
            version=2,
            batch_size=32)

        def merged_config(config1,config2):
            merged={}
            for key,value in config1.items():
                merged[key]=value
            for key,value in config2.items():
                merged[key]=value
            return merged
        final_config=merged_config(config1,config2)
        print(final_config)
    

    elif choice==3:
        Celsius_temperature=[0,20,37,100,-10,25,36.6]
        fahrenheit=list(map(lambda x:((x*9/5)+32),Celsius_temperature))
        print(fahrenheit)
        student_list=['bala','ganesh','raj','arun','jegan']
        capital=list(map(lambda x:x.upper(),student_list))
        print(capital)


    elif choice==4:
        result=[x**2 for x in range(1,101) if x%2==0 and x**2>200]

        #first result
        print("First Result:",result[0])

        #second result
        print("total values:",len(result))
    

    elif choice==5:
         students = [
    ('bala',91.2),
    ('ganesh',49.0),
    ('raj',78.4),
    ('arun',63.0),
    ('jegan',61.0)
         ] 

         result_1=list(filter(lambda x:x[1]>70,students))
         high=f"Students Scored Above 70 marks:{result_1} "
         print(high)

         result_2=list(filter(lambda x:x[1]<55,students))
         low=f"Students Scored below 55 marks:{result_2} "
         print(low)

         start_with_a=list(filter(lambda x:x[0].startswith("a"),students))
         start=f"Starts with A:{start_with_a}"
         print(start)
    

    elif choice==6:
        my_list=[n**2 for n in range(1,51) if n%2==0 and n**2>100]
        print(my_list)

        students=['bala','ganesh','raj','arun','jegan']
        averages=[91.2,49.0,78.4,63.0,61.0]
        my_dict={student:average for student,average in zip (students,averages)}
        print(my_dict)

        words=["apple","cat","banana","dog","orange","pen"]
        result=[word.upper() for word in words if len(word)>4]
        print(result)
    

    elif choice==7:
        def clean_data(data):
            return[x for x in data if 0 <=x<= 100]
        
        def normalize_data(data):
            return[x/100 for x in data]
        
        def compute_final_score(data):
            return (sum(data) / len(data)) *100
        
        def format_score(score):
            score=round(score,2)
            return f"Final Score: {score} out of 100"
        
        def run_pipeline(raw_data):
            cleaned=clean_data(raw_data)
            normalized=normalize_data(cleaned)
            final_score=compute_final_score(normalized)
            formatted_score=format_score(final_score)
            return formatted_score
        
        raw_data=[85,-5,92,150,78,63,0,88]
        result=run_pipeline(raw_data)
        print(result)
    
    else:
        print("Invalid Choice")