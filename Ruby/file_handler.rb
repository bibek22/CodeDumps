file_handler = File.new("random.txt", 'w')
file_handler.puts("Random text").to_s

file_handler.close

data = File.read('random.txt')
puts "Data from the file: " + data

load "new.rb"
load "intro.rb"
