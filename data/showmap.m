function showmap (data, t)
map = 1 - data;
figure, imshow (map);
title (t);
end