#!/usr/bin/env ruby

input_string = ARGV[0]

if input_string.nil?
  puts "Usage: ./2-repetition_token_1.rb <input_string>"
  exit 1
end

puts input_string.scan(/hbt+n/).join
