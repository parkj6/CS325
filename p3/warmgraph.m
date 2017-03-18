%P3 Warm Up

X = [1,2,3,5,7,8,10]
Y = [3,5,7,11,14,15,19]

a = 1.7142857 
b = 1.8571429 
max = 0.57142857 
x=1:10
z = a * x + b


xlabel('')
ylabel('')

plot(X,Y,'gs','LineWidth',2,'MarkerSize',10,'MarkerEdgeColor','g')
title('Warm Up' )
hold
plot(z, '-b','LineWidth',2)
