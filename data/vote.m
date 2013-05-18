function voted = vote (grid)
voted = zeros (size (grid));
for i = 2:size (grid, 1) - 1
    for j = 2:size (grid, 2)-1
%         if grid (i, j) < 3
%             continue;
%         end
        max = 0;
        x = 0;
        y = 0;
        second = 0;
        sx = 0;
        sy = 0;
        
        if grid (i-1, j) > max
            second = max;
            sx = x;
            sy = y;
            max = grid (i - 1, j);
            x = i - 1;
            y = j;
        end
        if grid (i, j - 1) > max
            second = max;
            sx = x;
            sy = y;
            max = grid (i, j - 1);
            x = i;
            y = j - 1;
        end
        if grid (i + 1, j) > max
            second = max;
            sx = x;
            sy = y;
            max = grid (i + 1, j);
            x = i + 1;
            y = j;
        end
        if grid (i, j + 1) > max
            second = max;
            sx = x;
            sy = y;
            max = grid (i, j + 1);
            x = i;
            y = j + 1;
        end
        if max > grid (i, j) * 1.7
            voted (x, y) = voted (x, y) + 1;
        end
        if second > grid (i, j) * 1.7
            voted (sx, sy) = voted (sx, sy) + 1;
        end
    end
end
voted (grid < 10) = 0;
end