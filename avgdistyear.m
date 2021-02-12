function output = avgdistyear(data, r,n)
%return the average similarity of the year r to previous n years.

dists = [];
for i = 1:n;
    dists = [dists distyear(data,r,r-i)];
end

output = mean(dists);