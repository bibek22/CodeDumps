numbers = [1,2,3,4,5, 6]

for number in numbers
    puts "#{number}, "
end

groceries = ['banana', 'sweet potatoes', 'pasta']

for item in groceries
    puts "have to buy #{item} right now."
end

# another way to do the same way.
groceries.each do |item|
    puts "Have to get some #{item}"
end
