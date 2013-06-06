function bw = lineup (bw, gray)
change = 1;
used = zeros (size (bw), 'uint32');
bw (bw > 0) = 1;
while change == 1
    change = 0;
    for i = 2:size (bw, 1)-1
        for j = 2:size (bw, 2)-1
            if bw (i,j) == 0 || used (i, j) == 1
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
            n = s - 1;% #neighbor
            if n <= 1
                rate = 0.4;
            else
                rate = 1.5;
            end
            if maxv > gray (i, j) * rate
                bw(maxx, maxy) = 1;
                if maxv < gray (i, j)                    
                    gray (maxx, maxy) = gray (i, j);
                end
                change = 1;
                used (i, j) = 1;
            end
        end
    end
end
end
