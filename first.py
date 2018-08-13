import second
import json

def main():
    second.second_print();

    import types
    if type(second.fib()) == types.GeneratorType:
        counter = 0
        for n in second.fib():
            if counter == 10:
                break
            print n
            counter = counter + 1

    float_array = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    print(second.comprehension(float_array))

    if second.countArgs(1,2,3,4) == 1:
        print "good"
    if second.countArgs(1,2,3,4,5) == 2:
        print "better"
    if second.isMagic(1,2,3,magicnumber=6) == False:
        print "Great"
    if second.isMagic(1,2,3,magicnumber=7) == True:
        print "Awesome!"

    aSet = set(['Jake','John','Eric'])
    bSet = set(['John','Jill'])
    print aSet.difference(bSet)
    print aSet.symmetric_difference(bSet)
    print aSet.intersection(bSet)
    print aSet.union(bSet)

    salaries = '{"Alfred":300,"Jane":400}'
    new_salaries = second.add_employee(salaries, "Me",800)
    decoded_salaries = json.loads(new_salaries)
    print(decoded_salaries["Alfred"])
    print(decoded_salaries["Jane"])
    print(decoded_salaries["Me"])

main()
