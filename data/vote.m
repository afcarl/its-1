function voted = vote (gray)
voted = zeros (size (gray));
for i = 2:size (gray, 1) - 1
    for j = 2:size (gray, 2)-1
        for x = i-1:i+1
            for y = j-1:j+1
                if gray(x, y) > gray (i,j)
                    voted (x, y) = voted (x, y) + 1;
                end
            end
        end
    end
end
voted = voted > 3;        
end