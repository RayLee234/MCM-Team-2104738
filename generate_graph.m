n = 3;
X = years(n+1:98)
Y = []
for i = n+1:98
    Y = [Y distyear(group_by_year,i,i-n)];
end
Y = smooth(Y.');
plot(X,Y);