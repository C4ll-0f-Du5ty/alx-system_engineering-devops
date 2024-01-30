#!/usr/bin/env ruby
# Making my own Expression!

i = 0
while ARGV[i]
    ARGV[i].split.each do |word|
        if word == "School"
            print "School"
        end
    end
    i += 1
end
puts ""
