first_name = "Bibek"
last_name = "Gautam"

full_name = first_name + last_name
middle_name = nil
full_name = first_name + middle_name.to_s + last_name

puts full_name.include?("Sam")  # prints false

puts "Vowels : " + full_name.count("aeiou").to_s
puts "Consonants : " + full_name.count("^aeiou").to_s
puts full_name.start_with?("bib")

# index is the index of the position of first char in the first match of the argument.
puts "Index: " + full_name.index('gautam').to_s

# case change
puts full_name.upcase
puts full_name.downcase
puts full_name.swapcase
puts full_name.swapcase

# stripping whitespace from right and left and both
full_name = "       " + full_name + " "
print full_name.lstrip
print "l \n"
puts full_name.rstrip
puts full_name.strip

# string formating kinda
full_name = first_name + middle_name.to_s + last_name
puts full_name.rjust(15, '.')
puts full_name.ljust(15, '.')
puts full_name.center(15, '.')

puts full_name.chop # gets rid of last character
puts full_name.chomp  # chops newline if exists
puts full_name.chomp('am')  # chops the argument from the end of string.


puts full_name.delete('a')
name_array = full_name.split(//)
puts name_array

name_array = full_name.split(/ /)
puts name_array
