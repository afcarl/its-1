function v = neighbor (data)

center = data (floor (size (data) + 1) / 2);
data = data .* 1.1;
v = all (data (:) < center );
end