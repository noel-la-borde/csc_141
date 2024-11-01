# Multiple Modules

from admin_privileges import Admin

admin_user = Admin("Noel", "La Borde", 23, "Computer Science")
admin_user.privileges.show_privileges()

# For this exercise I had to create two different files to store different classes. 
# The importatiomn of Admin in admin_privileges does work. 
