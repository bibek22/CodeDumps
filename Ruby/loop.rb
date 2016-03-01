x = 1

loop do  # basically like a for loop ?!
    x += 1

    next unless (x % 2) == 0
    puts x

    break if x >= 10
end

# While loop
puts "following if any is from inside the while loop."
y = 1
while y <= 10
y += 1  # the indent level doesn't matter. just a thing to know.
    next unless (y % 2) ==0
    puts y
end


# until loop.
a = 1
puts "this if from ultil loop"
until a > 10
    a += 1

    next unless (a % 2) == 0
        puts a
end
