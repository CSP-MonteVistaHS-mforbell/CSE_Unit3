"""
This program is intended as a tracer round for the flow of control as a user
of a social media account makes, deletes, and edits posts. For testing,
a user should be able to enter their user name, change which user name they
are currently using, add a post using their current user name, remove a post
made under their current user name, edit a post made under their current user 
name, print the contents of the list of posts, or quit the program.
"""

'''This line of code tells the Python interpreter that it needs to reference the 
post.py file in order to run the rest of the code in this file.'''
from CSE_322_post import Post

'''Initialize a list to store the post messages'''
post_list =[]

# code to get the user name they want to use

# code to welcome user to the program 

"""Store initial user input in a variable identified by user_input (you may need this in your while loop also)"""

user_input = raw_input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")

'''This while loop ensures that the program will continue executing statements
 at the next indentation level until the user types "quit" in response to the 
 prompt.'''
while user_input != "quit":

    #code for adding a post here
    
    #code for removing a post here
    
    #code for changing the current user here
    
    #code to display all posts, you can use the code in comments below (delete the quotations for the code to be active)
    """
	# this for loop will print the index of the element in the list
	# and the element itself
    index = 0
    for post in post_list:
        print (str(index)+ ":" +  str(post))
        index += 1
    """
    #code to inform the user that their input was not valid here
    
    # code that will allow the user to make a new selection

# Code to say goodbye to current user