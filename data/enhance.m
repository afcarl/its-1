function data = enhance (gray, leng)
data = gray;
for i = 1:leng:size (gray,1) - 1
    for j = 1:leng:size (gray, 2) - 1
        histeq (data (i:i + leng - 1, j:j + leng - 1));
    end
end
end