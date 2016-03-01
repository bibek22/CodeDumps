def add_nums(n1, n2)
    return n1.to_i+n2.to_i
end

puts add_nums(2,3)

x = 1
y = 2
def change_x(x)
    x = 4  # variables are local to the functions.
    y = x
    puts "from func:  y = " + y.to_s
end

change_x(x)
puts x
puts y


# try and except blocks equivalent:
# begin and rescue blocks :DD
begin
    puts (3 / 0)
rescue
    puts "can not devide by zero!"
end

age = 12
def check_age(age)
    raise ArgumentError, "Enter positive number, idiota!" unless age > 0
end

puts "checking age \n\n"
check_age(-1)

