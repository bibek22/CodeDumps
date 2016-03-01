age = 5
=begin
Comparasions: == != < > >= <=
Logical: && || !  and or not
=end

if (age <= 5) && (age >=3)
    puts "You are probably 5.\n\n"
elsif (age > 6.to_s)
    puts 'you are mre than 6. damn. lol'
else
    puts "you just got purred!"
end

# some weird comparator in ruby
# Gives 1 if first is greater than second
# gives 0 if they are equal
# and gives -1 if the first one is small.

puts "3 <=> 6 = " + (3 <=> 6).to_s

# another intersting
unless age > 6
    puts "You're basically a kid. wait some 13 more years."
else
    puts "your kinda grown up!"
end


# Switches
puts "which language do you speak?"
greeting = gets.chomp

case greeting
when "french" , "French"
    puts "bonjour"
when "spanish" , "Spanish"
    puts "hola"
else
    puts "hello!"
end


# some handy operator:
puts (age > 50)? "You're old." : "Young!"
