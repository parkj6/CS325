%%% Matlab is available through the CoE:
%%% http://engineering.oregonstate.edu/computing/personal/149#matlab
%%% 
%%% Octave is an open-source version of Matlab.  
%%% http://www.gnu.org/software/octave/
%%% The code below has not been tested with Octave, but should work.

%%% What happens to a straight line on logarithmic axes? %%%

x = [10:10:100]
y = [10:10:100]

figure
subplot(2,2,1)
plot(x,y,'ro')
title('linear axes, y = x')

% if the x axis is logarithmic, then y = 2^"(log x)"
subplot(2,2,2)
semilogx(x,y,'ro')
title('logarithmic x axis, y  = x')

% if the y axis is logarithmic then "log(y)" = log(x) 
subplot(2,2,3)
semilogy(x,y,'ro')
title('logarithmic y axis, y  = x')

% if both axes are logarithmic, then "log(y)" = "log(x)"
subplot(2,2,4)
loglog(x,y,'ro')
title('logarithmic axes, y  = x')

%%% What would happen to a polynomial dependence? %%%

% y = x^d --> "log(y)" = log(x^d) = d "log(x)"  
% should be linear!

% Is the following polynomial?
x = [7.0605    0.3183    2.7692    0.4617    0.9713    8.2346    6.9483    3.1710    9.5022]
y = [49.9313    0.0632    7.7818    0.1716    1.0042   68.4333   48.9710    9.9926   88.7169]

figure;
loglog(x,y,'ro')

% what is the slope of this line?  should be ~2:
polyfit(log(x),log(y),1)

%%% What would happen to an exponential dependence? %%%

% y = b^x --> "log(y)" = log(b^x) = "x" log b
% semilogy should be linear

% Is the following exponential?
x = [5.8527    2.2381    7.5127    2.5510    5.0596    6.9908 ...
     8.9090    9.5929    5.4722]
y = [1.2058e+04 41.8573 1.6094e+05   56.2411   3.0687e+03   6.8467e+04 ...
     1.9000e+06   5.2035e+06   6.7901e+03]
figure;
semilogy(x,y,'ro')
exp(polyfit(x,log(y),1))  




