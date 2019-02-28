def cube_volume(x):
    if not float(x) or not int(x):
        return (-1)
    else:
        return (x*x*x)



def main():

    side_in_cm = 5.0
    volume_of_cube = cube_volume(side_in_cm)
    print("Volume of a cube is: ", volume_of_cube)

main()