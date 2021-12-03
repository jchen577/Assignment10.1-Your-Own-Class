Class Documentation
This code includes a ‘person’ class that takes in a name, health, and if they are an enemy or not. The class includes the ability to get each of the said variables as well as the class variable named ‘location’, which is always set to Earth. The person class allows you to make a person object with health that you can use to battle other person class objects. 

Class Variables
The only class variable in the person class is ‘location’. The location variable is always defaultly set to Earth but can be changed using the change_location() method. 

Data Variables
Name: The name is basically what the person will be referred to as and can be accessed with the get_name() method
Health: The health variable is how much damage the person object can take before they die
Enemy: The enemy variable is to determine if the person object is going against you or with you

Methods
get_name(): This method requires no input and is needed to access the name of the person object when outside of the class itself. It returns the name of the object in a string form.

get_health(): This method also requires no input and is needed to access the person’s health when outside of the class. It returns the health of the person as an integer.

get_enemy(): This method requires no input and is used to access the person’s boolean enemy variable when outside of the class. It returns whether or not the person is an enemy as a boolean variable.

damage(): This method takes in an integer and subtracts the integer from the health of the person object. If the person’s health reaches 0, the method also tells us that the player died, otherwise it returns the person’s health left in a string

get_location(): This method requires no input and is used to get the private class variable __location__. It returns the location of the person as a string.

change_location(): This method requires a string input and replaces the previous location with the inputted string. It has no return value and it only changes the location for the singular person object.

stats(): This method requires no input and is used to display all of the variables of the person object. It returns the variables of the person object formatted in a string.

hit(): This method requires another person object as its input as it is the object that will potentially lose health. The method first checks whether the other person is an enemy and if it isn’t, then it returns a string. It then checks if the random number generated is even and if it is, the person object hits for damage between 0 to 10. If the number is odd, the person object is instead hit for damage between 0 to 10. For both of these results the method returns a string telling how much health is left for each respective person.

befriend(): This method does not require any sort of input. This method first rolls a random number between 0 and 10 and if the number is 3, the current person’s enemy data variable is changed to False ‘befriending’ them. If the person is already not an enemy, the method returns a string stating so. Otherwise, the method returns a string stating whether or not the person has been befriended or not. 

Demo Program
The demo program uses a majority of the methods stated and creates 2 person objects to work with. It demonstrates the hit() method to show the change in health. It then displays the 1st person object’s data variables one by one to return the values of them. The program then uses the stats() method to display all of the variables in the 2nd person object to show the difference between printing individually and using the stats() method. Then the program demonstrates the befriend() method followed by a demonstration of the location changing using the change_location() method.

Instructions
Download the file, read the README, hit run and see the prints.
