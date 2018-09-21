def weight_on_planets():
   # write your code here
	
	earthWeight = float(input("What do you weigh on earth? "))
	marsWeight = earthWeight*0.38
	jupiterWeight = earthWeight*2.34
	print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(marsWeight, jupiterWeight))

   
   
if __name__ == '__main__':
   weight_on_planets()
