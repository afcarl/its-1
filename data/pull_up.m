function map = pull_up (remain, down, gray, rate)
    map = remain;   
    used = zeros (size (remain));
    change = 1;
    while change ~= 0
        change = 0;
        for i = 2:size (remain,1) -1
            for j = 2:size(remain,2) -1
                if remain(i,j) == 0 || used (i, j) == 1
                    continue
                end
                maxv = 0;
                maxx = 0;
                maxy = 0;
                for x = i-1:i+1
                    for y = j-1:j+1
                        if gray (x, y) > gray(i,j) * rate && ...
                                map (x, y) == 0 && down(x,y) == 1
                            if gray (x, y) > maxv
                                maxx = x;
                                maxy = y;
                                maxv = gray (x, y);
                            end
                        end
                    end
                end
                if maxv > 0
                    map (maxx, maxy) = 1;
                    used (i, j) = 1;
                    change = 1;
                end
            end
        end
        %rate = rate * 1.05;
    end
end