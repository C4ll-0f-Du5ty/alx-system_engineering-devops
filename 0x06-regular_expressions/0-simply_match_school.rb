#!/usr/bin/env ruby
# Making my own Expression!

i = 0
k = ""
while ARGV[i]
    ARGV[i].split.each do |word|
        if word == "School"
            k += "School"
        end
    end
    i += 1
end
puts k
