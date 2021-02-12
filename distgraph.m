function output = distgraph(data,n)
%returns the array: distances of years to the average of n previous years.

global years 

X = years(n+1:98);
Y = [];
for i = n+1:98;
    Y = [Y avgdistyear(data,i,n)];
end
figure(1)
hold on

Y = smooth(Y.')

scatter(X,Y);
plot(X,Y);
output = [X Y];