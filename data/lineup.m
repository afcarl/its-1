function bw = lineup (bw, gray)
change = 1;
while change == 1
    change = 0;
    for i = 2:size (bw, 1)-1
        for j = 2:size (bw, 2)-1
            if bw (i,j) == 0
                continue
            end
            s = 0;
            maxx = 0;
            maxy = 0;
            maxv = 0;
            for x = i-1:i+1
                for y = j-1:j+1
                    if gray (x, y) > maxv && bw (x, y) == 0
                        maxv = gray (x, y);
                        maxx = x;
                        maxy = y;
                    end
                    s = s + bw (x, y);
                end
            end
            if s ~= 2% #neighbor is not 1
                continue
            end
            if maxv > gray (i, j) * 0.6
                bw(maxx, maxy) = 1;
                change = 1;
            end
        end
    end
end
end
