function bw = connect_labeled (labeled, gray)
    

bw = zeros (size (labeled));
    for i = 2:size (labeled, 1) - 1
        for j = 2:size (labeled, 2) - 1
            if labeled (i, j) ~= 0
                continue
            end
            neighbor = 0;
            point = 0;
            for x = i-1:i+1
                for y = j-1:j+1
                    if labeled (x, y) == 0
                        continue
                    end
                    if neighbor == 0
                        neighbor = labeled (x, y);
                    else
                        if neighbor ~= labeled (x, y)
                            point = 1;
                        end
                    end
                end
            end
            if point == 1
                bw(i, j) = 1;
            end
        end
    end
        figure, imshow (bw);
    title ('points');
    
    for i = 2:size (labeled, 1) - 1
        for j = 2:size (labeled, 2) -1
            if bw(i,j) == 0
                continue
            end
            for x = i-1:i+1
                for y = j - 1:j+1
                    if bw(x, y) == 0
                        continue;
                    end
                    if gray(x, y) > gray (i, j)
                        bw(i, j) = 0;
                    else
                        bw (x, y) = 0;
                    end
                end
            end
        end
    end
    figure, imshow (bw);
    title ('points');
    bw = bw + (labeled > 0);
end