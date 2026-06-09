while True:
    print('''Enter the following numbers to particular programs:
      1:Student Report
      2:Temperature Converter
      3:Word Frequency Counter
      4:Unique Word Finder
      5:String Reverser
      6:Shopping Bill Calculator
      ''')

    choice= int(input("Enter the Value: "))
    if choice==1:
        name=input("Enter the Student Name: ")
        greet=f"Hello, {name}"
        print(greet)
        mark1=float(input("Enter mark 1: "))
        mark2=float(input("Enter mark 2: "))
        mark3=float(input("Enter mark 3: "))
        mark4=float(input("Enter mark 4: "))
        mark5=float(input("Enter mark 5: "))
        avg=(mark1+mark2+mark3+mark4+mark5)/5
        average=f"Average Value: {avg}"
        print(average)
        if avg>= 85:
            print("Grade: A")
        elif avg>= 70:
            print("Grade: B")
        elif avg>= 55:
            print("Grade: C")
        else:
            print("Grade: F")


    elif choice==2:
        print('''Conversion Type:
            1:C to F
            2:F to C
            ''')
        conversion_type=int(input("Enter (1/2): "))
        values=float(input("Enter the Value:"))
        if conversion_type==1:
            fahrenheit=(values*9/5)+32
            result_1=f"fahrenheit = {fahrenheit}"
            print(result_1)
        elif conversion_type==2:
            celsius=(values-32)*5/9
            result_2=f"Celsius = {celsius}"
            print(result_2)


    elif choice==3:
        user_input=input("Enter the Sentence: ")
        lowercase=user_input.lower()
        stt=lowercase.split()
        word={}
        for i in stt:
            if i in word:
                word[i]+=1
            else:
                word[i]=1
        sort_1= sorted(
            word.items(),
            key=lambda item:item[1],
            reverse=True
            )
        print("\nWord Frequency:")
        for x,y in sort_1:
            print(x, ":", y)

            
    elif choice==4:
        user_input=input("Enter the Sentence: ")
        lowercase=user_input.lower()
        split=lowercase.split()
        lenn=len(split)
        set_conversion=set(split)
        length=len(set_conversion)
        l=f"There are {length} Unique Words in {lenn} Word Paragraph"
        print(l)
        word={}
        for d in split:
            if d in word:
                word[d]+=1
            else:
                word[d]=1
        print("Duplicated Words: ")
        for c,v in word.items():
            if v>1:
                print(c)


    elif choice==5:
        word=input("Enter the Sentence:")
        split=word.split()
        v1=[]
        for i in split:
            v1.append(i[::-1])
        res1=" ".join(v1)
        slice=split[::-1]
        res2=" ".join(slice)
        word_2=[]
        for i in slice:
            word_2.append(i[::-1])
        res3=" ".join(word_2)
        print("\nVersion 1 - Reverse Letters only: ")
        print(res1)
        print("\nVersion 2 - Reverse words order only: ")
        print(res2)
        print("\nVersion 3 - Reverse Both: ")
        print(res3)


    elif choice==6:
        item=[("Rice 1Kg",60.0),("Milk 500ml",28.0),("Bread",45.0),("Eggs 6pcs",72.0),("Oil 1L",130.0)]
        sort= sorted(
        item,
        key=lambda item:item[1],
        reverse=True
        )
        subtotal =0
        for name,price in sort:
            print(name, ":", price)
            subtotal +=price 
        if subtotal>500:
            discount=subtotal*0.10
        else:
            discount=0
        sub=subtotal-discount
        print("subtotal= ",sub)
        gst=sub*0.18
        print("GST= ",gst)
        grandtotal=sub+gst
        print("Grand Total= ",grandtotal)

    else:
        print("Invalid Choice") 